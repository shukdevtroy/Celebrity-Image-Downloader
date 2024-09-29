# Celebrity Image Downloader

## Overview
The Celebrity Image Downloader is a Python application that allows users to download images of various celebrities from Google Images and view their Wikipedia profiles. The application features a simple graphical user interface (GUI) built using Tkinter.

## Features
- Search for celebrities by name.
- Select multiple celebrities to download images.
- Specify the number of images to download per celebrity.
- Automatically creates directories for storing downloaded images.
- Links to each celebrity’s Wikipedia page 

## Requirements
To run this application, you need:
- Python 3.x
- The following Python packages:
  - `requests`
  - `beautifulsoup4`
  - `tkinter` (usually included with Python installations)

You can install the required packages using pip:

```bash
pip install requests beautifulsoup4
```

## Installation
1. Clone the repository:

   ```bash
   git clone https://github.com/shukdevtroy/Celebrity-Image-Downloader.git
   cd Celebrity-Image-Downloader
   ```

2. Run the application:

   ```bash
   python download.py
   ```

## User Guide

### How to Use the Application

1. **Search for a Celebrity:**
   - In the "Search Celebrity" entry field, type the name of the celebrity you wish to find. The list will filter in real-time based on your input.

2. **Select Celebrities:**
   - Click on the celebrity's name in the list. If you want to select multiple celebrities, check the "Select Multiple Celebrity Names" checkbox.

3. **Specify the Number of Images:**
   - In the "Number of Images to Download" entry field, enter the number of images you want to download for each selected celebrity.

4. **Download Images:**
   - Click the "Download Images" button. The application will start downloading the specified number of images for the selected celebrities and save them in a folder named `Celebrity_Images` within the current directory.

5. **Refresh Selection:**
   - If you want to clear your current selections, click the "Refresh Selection" button.

6. **View Wikipedia Profiles:**
   - You can double-click on any celebrity name in the list to open their Wikipedia page in your default web browser.

### Important Notes
- Ensure that you have a stable internet connection for downloading images.
- The application uses web scraping to fetch images, which may be subject to Google's policies. Please use responsibly.
- The downloaded images will be stored in a folder named after the celebrity's name inside the `Celebrity_Images` directory.

## Contributing
If you'd like to contribute to the project, feel free to submit a pull request or open an issue.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Thanks to [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) for the web scraping capabilities.
- Special thanks to Tkinter for providing the GUI toolkit.

## Contact

For any questions or issues, please contact:

- **Email**: shukdevdatta@gmail.com
- **GitHub**: [Click to here to access the Github Profile](https://github.com/shukdevtroy)
- **WhatsApp**: [Click here to chat](https://wa.me/+8801719296601)

---

Feel free to reach out if you have any questions or feedback!
