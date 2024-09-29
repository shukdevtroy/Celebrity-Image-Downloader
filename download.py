import os
import requests
import webbrowser
from tkinter import *
from tkinter import messagebox
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

def download_images(celebrity_names, num_images):
    for celebrity_name in celebrity_names:
        output_dir = os.path.join(os.getcwd(), "Celebrity_Images", celebrity_name.replace(" ", "_"))
        os.makedirs(output_dir, exist_ok=True)

        search_url = f"https://www.google.com/search?hl=en&tbm=isch&q={celebrity_name.replace(' ', '+')}"
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(search_url, headers=headers)

        soup = BeautifulSoup(response.text, 'html.parser')
        image_elements = soup.find_all('img', limit=num_images + 1)[1:]

        downloaded = 0
        for img in image_elements:
            img_url = img.get('src')
            if not img_url or not img_url.startswith('http'):
                continue

            try:
                img_data = requests.get(img_url).content
                img_name = os.path.join(output_dir, f"{celebrity_name.replace(' ', '_')}_{downloaded + 1}.jpg")
                with open(img_name, 'wb') as img_file:
                    img_file.write(img_data)
                downloaded += 1
                print(f"Downloaded {img_name}")
                if downloaded >= num_images:
                    break
            except Exception as e:
                print(f"Could not download {img_url}. Error: {e}")

        if downloaded == 0:
            print(f"No images found for {celebrity_name}.")
        else:
            print(f"Downloaded {downloaded} images for {celebrity_name} into '{output_dir}'.")

def get_selected_celebrities():
    selected_indices = listbox.curselection()
    selected_celebrities = [listbox.get(i) for i in selected_indices]
    return selected_celebrities

def open_wikipedia(celebrity_name):
    url = celebrities[celebrity_name]
    webbrowser.open(url)

def on_download():
    num_images = int(num_images_entry.get())
    selected_celebrities = get_selected_celebrities()
    if selected_celebrities:
        download_images(selected_celebrities, num_images)
        messagebox.showinfo("Download Complete", f"Download has been finished. Please check the directory:\n{os.path.join(os.getcwd(), 'Celebrity_Images')}")
        root.quit()
    else:
        print("No celebrities selected.")

def toggle_selection_mode():
    if select_multiple_var.get():
        listbox.config(selectmode=MULTIPLE)
    else:
        listbox.config(selectmode=SINGLE)

def refresh_selection():
    listbox.selection_clear(0, END)  # Clear all selections

def filter_celebrities():
    search_query = search_entry.get().lower()
    listbox.delete(0, END)
    for celebrity in celebrities.keys():
        if search_query in celebrity.lower():
            listbox.insert(END, celebrity)

def on_enter(event):
    if event.widget == download_button:
        event.widget['background'] = '#0056b3'  # Darker blue for hover
    elif event.widget == refresh_button:
        event.widget['background'] = '#218838'  # Darker green for hover
    event.widget['foreground'] = 'white'

def on_leave(event):
    if event.widget == download_button:
        event.widget['background'] = '#007BFF'  # Original blue for download button
    elif event.widget == refresh_button:
        event.widget['background'] = '#28A745'  # Original green for refresh button
    event.widget['foreground'] = 'white'

# Tkinter GUI setup
root = Tk()
root.title("Celebrity Image Downloader")
root.geometry("400x600")  # Set a fixed window size
root.configure(bg="#f0f0f0")

# Search entry
search_label = Label(root, text="Search Celebrity:", bg="#f0f0f0", font=("Arial", 12))
search_label.pack(pady=(10, 2))

search_entry = Entry(root, font=("Arial", 12))
search_entry.pack(pady=(0, 10), padx=10)
search_entry.bind("<KeyRelease>", lambda event: filter_celebrities())  # Call filter function on key release

# Checkbox for selecting multiple celebrities
select_multiple_var = BooleanVar()
select_multiple_checkbox = Checkbutton(root, text="Select Multiple Celebrity Names", variable=select_multiple_var, command=toggle_selection_mode, bg="#f0f0f0", font=("Arial", 12))
select_multiple_checkbox.pack(pady=(5, 5))

# Frame for Listbox and Scrollbar
frame = Frame(root, bg="#f0f0f0")
frame.pack(pady=(5, 10))

# Listbox for celebrity selection
listbox = Listbox(frame, selectmode=SINGLE, height=15, width=50, font=("Arial", 10), bg="#ffffff", fg="#333333")
for celebrity in celebrities.keys():
    listbox.insert(END, celebrity)

scrollbar = Scrollbar(frame, orient=VERTICAL, command=listbox.yview)
listbox.config(yscrollcommand=scrollbar.set)

listbox.pack(side=LEFT, fill=BOTH, padx=(10, 0), pady=(0, 10))
scrollbar.pack(side=RIGHT, fill=Y)

# Entry for number of images to download
num_images_label = Label(root, text="Number of Images to Download:", bg="#f0f0f0", font=("Arial", 12))
num_images_label.pack(pady=(5, 2))

num_images_entry = Entry(root, font=("Arial", 12))
num_images_entry.pack(pady=(0, 10), padx=10)

# Download button
download_button = Button(root, text="Download Images", command=on_download, bg="#007BFF", fg="white", font=("Arial", 12), relief=FLAT)
download_button.pack(pady=(5, 5))
download_button.bind("<Enter>", on_enter)
download_button.bind("<Leave>", on_leave)

# Refresh button
refresh_button = Button(root, text="Refresh Selection", command=refresh_selection, bg="#28A745", fg="white", font=("Arial", 12), relief=FLAT)
refresh_button.pack(pady=(5, 10))
refresh_button.bind("<Enter>", on_enter)
refresh_button.bind("<Leave>", on_leave)

# Adding clickable icons next to the celebrity names
for index, celebrity in enumerate(celebrities.keys()):
    listbox.insert(END, celebrity)  # Add the celebrity name
    # Here you could add an icon next to the name, but Listbox doesn't support images directly
    listbox.bind('<Double-Button-1>', lambda event: open_wikipedia(listbox.get(listbox.curselection())))

# Run the application
root.mainloop()
