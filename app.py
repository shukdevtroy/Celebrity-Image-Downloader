import os
import requests
import streamlit as st
from bs4 import BeautifulSoup

# List of celebrity names and their Wikipedia URLs
celebrities = {
    "Adriana Lima": "https://en.wikipedia.org/wiki/Adriana_Lima",
    "Alex Lawther": "https://en.wikipedia.org/wiki/Alex_Lawther",
    "Alexandra Daddario": "https://en.wikipedia.org/wiki/Alexandra_Daddario",
    # Add more celebrities as needed
}

def download_images(celebrity_name, num_images, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    search_url = f"https://www.google.com/search?hl=en&tbm=isch&q={celebrity_name.replace(' ', '+')}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(search_url, headers=headers)

    if response.status_code != 200:
        st.error(f"Failed to retrieve images for {celebrity_name}. Status code: {response.status_code}")
        return 0

    soup = BeautifulSoup(response.text, 'html.parser')
    image_elements = soup.find_all('img', limit=num_images + 1)[1:]

    downloaded = 0
    total_images = min(num_images, len(image_elements))

    # Initialize progress bar
    progress_bar = st.progress(0)

    for index, img in enumerate(image_elements):
        img_url = img.get('src')
        if not img_url or not img_url.startswith('http'):
            st.warning(f"Skipping invalid image URL: {img_url}")
            continue

        try:
            img_data = requests.get(img_url).content
            img_name = os.path.join(output_dir, f"{celebrity_name.replace(' ', '_')}_{downloaded + 1}.jpg")
            with open(img_name, 'wb') as img_file:
                img_file.write(img_data)
            downloaded += 1
            progress_bar.progress(downloaded / total_images)  # Update progress bar
            if downloaded >= num_images:
                break
        except Exception as e:
            st.error(f"Could not download {img_url}. Error: {e}")

    return downloaded

def main():
    st.title("Celebrity Image Downloader")
    st.subheader("Select a celebrity and download images")

    selected_celebrities = st.multiselect("Select Celebrity Names:", list(celebrities.keys()))
    num_images = st.number_input("Number of Images to Download:", min_value=1, value=5)

    # Input for output directory
    output_directory = st.text_input("Enter Output Directory:", value=os.path.join(os.getcwd(), "Celebrity_Images"))

    if st.button("Download Images"):
        if selected_celebrities:
            # Check if the specified directory exists
            if os.path.isdir(output_directory):
                total_downloaded = 0
                for celebrity in selected_celebrities:
                    celebrity_dir = os.path.join(output_directory, celebrity.replace(" ", "_"))
                    downloaded = download_images(celebrity, num_images, celebrity_dir)
                    total_downloaded += downloaded
                if total_downloaded > 0:
                    st.success("Download completed successfully! 🎉")
                    st.info(f"Images saved in:\n{output_directory}")
                else:
                    st.warning("No images were downloaded.")
            else:
                st.error("The specified directory does not exist. Please create the directory or enter a valid path.")
        else:
            st.warning("No celebrities selected.")

    # Wikipedia links
    if selected_celebrities:
        st.subheader("Open Wikipedia Pages:")
        for celebrity in selected_celebrities:
            st.markdown(f"[{celebrity}]({celebrities[celebrity]})")

if __name__ == "__main__":
    main()
