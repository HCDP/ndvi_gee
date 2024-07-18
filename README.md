README
Overview
This repository contains two Python scripts and a Flask web application that together enable downloading of NDVI (Normalized Difference Vegetation Index) images from Google Earth Engine for specified regions and dates.
Files in the Repository

1.	fetch-ndvi.py - This script performs the following:
•	Authenticates with Google Earth Engine.
•	Defines regions of interest.
•	Fetches MODIS satellite data, processes it to calculate NDVI, and masks clouds.
•	Exports the processed NDVI images to local folders.

2.	app.py - This script sets up a Flask web server to:
•	Serve a simple "Hello, World!" message on the root route.
•	Provide endpoints for downloading the latest or specific dated NDVI images as ZIP archives.

Prerequisites
Ensure you have the following installed:
•	Python 3.x
•	Required Python packages (can be installed via pip install -r requirements.txt):
•	geemap
•	earthengine-api
•	seleniumbase
•	Flask

Google Earth Engine Authentication
Both scripts require authentication with Google Earth Engine. This involves using Selenium to automate the authentication process. Ensure you have a Google Earth Engine account and the necessary credentials.
Setup Instructions

1.	Install Python Packages
Create a requirements.txt file with the following content and install the required packages:
•	geemap
•	earthengine-api
•	seleniumbase
•	Flask

Then, install the packages using:
•	pip install -r requirements.txt

2.	Google Earth Engine Authentication
The ndvi.py script uses Selenium to handle Google authentication. Make sure you adjust the script to match your login credentials and follow the necessary steps to authenticate:
•	Replace your_gmail@gmail.com and password with your email and password.
Running the Scripts

1.	Running the NDVI Processing Script
Execute ndvi.py to start the NDVI image processing and export:
•	python ndvi.py
2.	Running the Flask Web Server
Run app.py to start the Flask web server:
•	python app.py

The server will start on http://127.0.0.1:5000/.
Flask Endpoints
•	Root Endpoint
Accessing http://127.0.0.1:5000/ will return a simple "Hello, World!" message.
•	Download Latest Folder
Accessing http://127.0.0.1:5000/download/latest will allow you to download the latest NDVI folder as a ZIP file.
•	Download Specific Folder
Accessing http://127.0.0.1:5000/download/spc_date/<date> will allow you to download the NDVI folder nearest to the specified date (format: YYYY-MM-DD) as a ZIP file.
Directory Structure
•	Exported Images
NDVI images are exported to folders named with the end date in the format YYYY-MM-DD under the NDVI final directory. Each region of interest will have its own subdirectory within this folder.
Additional Information
Error Handling
Both scripts have basic error handling to ensure the process completes even if some steps fail. Adjust the try-except blocks as necessary for more robust error reporting.
Customization
Modify the region coordinates, date ranges, and other parameters in ndvi.py as needed for your specific use case. The Flask app can also be extended with additional routes or functionality as required.


# NDVI
