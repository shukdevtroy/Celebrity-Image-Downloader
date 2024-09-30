import os
import requests
import webbrowser
import streamlit as st
from bs4 import BeautifulSoup

# List of celebrity names and their Wikipedia URLs
celebrities = {
    "Adriana Lima": "https://en.wikipedia.org/wiki/Adriana_Lima",
    "Alex Lawther": "https://en.wikipedia.org/wiki/Alex_Lawther",
    "Alexandra Daddario": "https://en.wikipedia.org/wiki/Alexandra_Daddario",
    "Alvaro Morte": "https://en.wikipedia.org/wiki/Álvaro_Morte",
    "Alycia Debnam-Carey": "https://en.wikipedia.org/wiki/Alycia_Debnam-Carey",
    "Amanda Crew": "https://en.wikipedia.org/wiki/Amanda_Crew",
    "Amber Heard": "https://en.wikipedia.org/wiki/Amber_Heard",
    "Andy Samberg": "https://en.wikipedia.org/wiki/Andy_Samberg",
    "Anne Hathaway": "https://en.wikipedia.org/wiki/Anne_Hathaway",
    "Anthony Mackie": "https://en.wikipedia.org/wiki/Anthony_Mackie",
    "Avril Lavigne": "https://en.wikipedia.org/wiki/Avril_Lavigne",
    "Barack Obama": "https://en.wikipedia.org/wiki/Barack_Obama",
    "Barbara Palvin": "https://en.wikipedia.org/wiki/Barbara_Palvin",
    "Ben Affleck": "https://en.wikipedia.org/wiki/Ben_Affleck",
    "Bill Gates": "https://en.wikipedia.org/wiki/Bill_Gates",
    "Bobby Morley": "https://en.wikipedia.org/wiki/Bobby_Morley",
    "Brenton Thwaites": "https://en.wikipedia.org/wiki/Brenton_Thwaites",
    "Brian J. Smith": "https://en.wikipedia.org/wiki/Brian_J._Smith",
    "Brie Larson": "https://en.wikipedia.org/wiki/Brie_Larson",
    "Camila Mendes": "https://en.wikipedia.org/wiki/Camila_Mendes",
    "Chris Evans": "https://en.wikipedia.org/wiki/Chris_Evans",
    "Chris Hemsworth": "https://en.wikipedia.org/wiki/Chris_Hemsworth",
    "Chris Pratt": "https://en.wikipedia.org/wiki/Chris_Pratt",
    "Christian Bale": "https://en.wikipedia.org/wiki/Christian_Bale",
    "Cristiano Ronaldo": "https://en.wikipedia.org/wiki/Cristiano_Ronaldo",
    "Danielle Panabaker": "https://en.wikipedia.org/wiki/Danielle_Panabaker",
    "Dominic Purcell": "https://en.wikipedia.org/wiki/Dominic_Purcell",
    "Dwayne Johnson": "https://en.wikipedia.org/wiki/Dwayne_Johnson",
    "Eliza Taylor": "https://en.wikipedia.org/wiki/Eliza_Taylor",
    "Elizabeth Lail": "https://en.wikipedia.org/wiki/Elizabeth_Lail",
    "Elizabeth Olsen": "https://en.wikipedia.org/wiki/Elizabeth_Olsen",
    "Ellen Page": "https://en.wikipedia.org/wiki/Elliot_Page",
    "Elon Musk": "https://en.wikipedia.org/wiki/Elon_Musk",
    "Emilia Clarke": "https://en.wikipedia.org/wiki/Emilia_Clarke",
    "Emma Stone": "https://en.wikipedia.org/wiki/Emma_Stone",
    "Emma Watson": "https://en.wikipedia.org/wiki/Emma_Watson",
    "Gal Gadot": "https://en.wikipedia.org/wiki/Gal_Gadot",
    "Grant Gustin": "https://en.wikipedia.org/wiki/Grant_Gustin",
    "Gwyneth Paltrow": "https://en.wikipedia.org/wiki/Gwyneth_Paltrow",
    "Henry Cavill": "https://en.wikipedia.org/wiki/Henry_Cavill",
    "Hugh Jackman": "https://en.wikipedia.org/wiki/Hugh_Jackman",
    "Inbar Lavi": "https://en.wikipedia.org/wiki/Inbar_Lavi",
    "Irina Shayk": "https://en.wikipedia.org/wiki/Irina_Shayk",
    "Jake McDorman": "https://en.wikipedia.org/wiki/Jake_McDorman",
    "Jason Momoa": "https://en.wikipedia.org/wiki/Jason_Momoa",
    "Jeff Bezos": "https://en.wikipedia.org/wiki/Jeff_Bezos",
    "Jennifer Lawrence": "https://en.wikipedia.org/wiki/Jennifer_Lawrence",
    "Jeremy Renner": "https://en.wikipedia.org/wiki/Jeremy_Renner",
    "Jessica Barden": "https://en.wikipedia.org/wiki/Jessica_Barden",
    "Jimmy Fallon": "https://en.wikipedia.org/wiki/Jimmy_Fallon",
    "Johnny Depp": "https://en.wikipedia.org/wiki/Johnny_Depp",
    "Josh Radnor": "https://en.wikipedia.org/wiki/Josh_Radnor",
    "Katharine McPhee": "https://en.wikipedia.org/wiki/Katharine_McPhee",
    "Katherine Langford": "https://en.wikipedia.org/wiki/Katherine_Langford",
    "Keanu Reeves": "https://en.wikipedia.org/wiki/Keanu_Reeves",
    "Kiernan Shipka": "https://en.wikipedia.org/wiki/Kiernan_Shipka",
    "Krysten Ritter": "https://en.wikipedia.org/wiki/Krysten_Ritter",
    "Leonardo DiCaprio": "https://en.wikipedia.org/wiki/Leonardo_DiCaprio",
    "Lili Reinhart": "https://en.wikipedia.org/wiki/Lili_Reinhart",
    "Lindsey Morgan": "https://en.wikipedia.org/wiki/Lindsey_Morgan",
    "Lionel Messi": "https://en.wikipedia.org/wiki/Lionel_Messi",
    "Logan Lerman": "https://en.wikipedia.org/wiki/Logan_Lerman",
    "Madelaine Petsch": "https://en.wikipedia.org/wiki/Madelaine_Petsch",
    "Maisie Williams": "https://en.wikipedia.org/wiki/Maisie_Williams",
    "Margot Robbie": "https://en.wikipedia.org/wiki/Margot_Robbie",
    "Maria Pedraza": "https://en.wikipedia.org/wiki/Maria_Pedraza",
    "Marie Avgeropoulos": "https://en.wikipedia.org/wiki/Marie_Avgeropoulos",
    "Mark Ruffalo": "https://en.wikipedia.org/wiki/Mark_Ruffalo",
    "Mark Zuckerberg": "https://en.wikipedia.org/wiki/Mark_Zuckerberg",
    "Megan Fox": "https://en.wikipedia.org/wiki/Megan_Fox",
    "Melissa Fumero": "https://en.wikipedia.org/wiki/Melissa_Fumero",
    "Miley Cyrus": "https://en.wikipedia.org/wiki/Miley_Cyrus",
    "Millie Bobby Brown": "https://en.wikipedia.org/wiki/Millie_Bobby_Brown",
    "Morena Baccarin": "https://en.wikipedia.org/wiki/Morena_Baccarin",
    "Morgan Freeman": "https://en.wikipedia.org/wiki/Morgan_Freeman",
    "Nadia Hilker": "https://en.wikipedia.org/wiki/Nadia_Hilker",
    "Natalie Dormer": "https://en.wikipedia.org/wiki/Natalie_Dormer",
    "Natalie Portman": "https://en.wikipedia.org/wiki/Natalie_Portman",
    "Neil Patrick Harris": "https://en.wikipedia.org/wiki/Neil_Patrick_Harris",
    "Pedro Alonso": "https://en.wikipedia.org/wiki/Pedro_Alonso",
    "Penn Badgley": "https://en.wikipedia.org/wiki/Penn_Badgley",
    "Rami Malek": "https://en.wikipedia.org/wiki/Rami_Malek",
    "Rebecca Ferguson": "https://en.wikipedia.org/wiki/Rebecca_Ferguson",
    "Richard Harmon": "https://en.wikipedia.org/wiki/Richard_Harmon",
    "Rihanna": "https://en.wikipedia.org/wiki/Rihanna",
    "Robert De Niro": "https://en.wikipedia.org/wiki/Robert_De_Niro",
    "Robert Downey Jr": "https://en.wikipedia.org/wiki/Robert_Downey_Jr.",
    "Sarah Wayne Callies": "https://en.wikipedia.org/wiki/Sarah_Wayne_Callies",
    "Scarlett Johansson": "https://en.wikipedia.org/wiki/Scarlett_Johansson",
    "Selena Gomez": "https://en.wikipedia.org/wiki/Selena_Gomez",
    "Shakira Isabel Mebarak": "https://en.wikipedia.org/wiki/Shakira",
    "Sophie Turner": "https://en.wikipedia.org/wiki/Sophie_Turner",
    "Stephen Amell": "https://en.wikipedia.org/wiki/Stephen_Amell",
    "Taylor Swift": "https://en.wikipedia.org/wiki/Taylor_Swift",
    "Tom Cruise": "https://en.wikipedia.org/wiki/Tom_Cruise",
    "Tom Ellis": "https://en.wikipedia.org/wiki/Tom_Ellis",
    "Tom Hardy": "https://en.wikipedia.org/wiki/Tom_Hardy",
    "Tom Hiddleston": "https://en.wikipedia.org/wiki/Tom_Hiddleston",
    "Tom Holland": "https://en.wikipedia.org/wiki/Tom_Holland",
    "Tuppence Middleton": "https://en.wikipedia.org/wiki/Tuppence_Middleton",
    "Ursula Corbero": "https://en.wikipedia.org/wiki/Ursula_Corberó",
    "Wentworth Miller": "https://en.wikipedia.org/wiki/Wentworth_Miller",
    "Zac Efron": "https://en.wikipedia.org/wiki/Zac_Efron",
    "Zendaya": "https://en.wikipedia.org/wiki/Zendaya",
    "Zoe Saldana": "https://en.wikipedia.org/wiki/Zoe_Saldana",
}

def download_images(celebrity_name, num_images, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    search_url = f"https://www.google.com/search?hl=en&tbm=isch&q={celebrity_name.replace(' ', '+')}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(search_url, headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser')
    image_elements = soup.find_all('img', limit=num_images + 1)[1:]

    downloaded = 0
    total_images = min(num_images, len(image_elements))

    # Initialize progress bar
    progress_bar = st.progress(0)

    for index, img in enumerate(image_elements):
        img_url = img.get('src')
        if not img_url or not img_url.startswith('http'):
            continue

        try:
            img_data = requests.get(img_url).content
            img_name = os.path.join(output_dir, f"{celebrity_name.replace(' ', '_')}_{downloaded + 1}.jpg")
            with open(img_name, 'wb') as img_file:
                img_file.write(img_data)
            downloaded += 1
            progress_bar.progress((downloaded / total_images))  # Update progress bar
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
            if os.path.isdir(output_directory):
                total_downloaded = 0
                for celebrity in selected_celebrities:
                    celebrity_dir = os.path.join(output_directory, celebrity.replace(" ", "_"))
                    downloaded = download_images(celebrity, num_images, celebrity_dir)
                    total_downloaded += downloaded
                if total_downloaded > 0:
                    st.success("Download has been finished! 🎉")
                    st.balloons()  # Celebratory effect
                    st.info(f"Images saved in:\n{output_directory}")
                else:
                    st.warning("No images were downloaded.")
            else:
                st.error("The specified directory does not exist. Please enter a valid directory.")
        else:
            st.warning("No celebrities selected.")

    # Wikipedia links
    if selected_celebrities:
        st.subheader("Open Wikipedia Pages:")
        for celebrity in selected_celebrities:
            st.markdown(f"[{celebrity}]({celebrities[celebrity]})")

if __name__ == "__main__":
    main()
