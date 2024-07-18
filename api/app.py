from flask import Flask, send_from_directory
import os
import datetime
from zipfile import ZipFile

app = Flask(__name__)

download_folder = "/data/"

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route('/download/spc_date/<date1>')
# Define the download folder path on the server
def download_spc_date(date1):
    date1 = str(date1)
    folder_name = find_nearest_folder(date1)
    if folder_name is None:
      return "No folders found in download directory!", 404  
    """Downloads a folder from the server."""
    try:
      # Check if folder exists
      if not os.path.exists(os.path.join(download_folder, folder_name)):
        return "Folder not found!", 404

      # Send the entire folder as a compressed zip file (optional)
      # You can modify this to send individual files or a different archive format.
      archive_filename = f"{folder_name}.zip"
      archive_path = os.path.join(download_folder, archive_filename)
      with ZipFile(archive_path, 'w') as zip_file:
        for root, _, files in os.walk(os.path.join(download_folder, folder_name)):
          for file in files:
            file_path = os.path.join(root, file)
            zip_file.write(file_path, os.path.relpath(file_path, os.path.join(download_folder, folder_name)))
      return send_from_directory(download_folder, archive_filename, as_attachment=True)

    except Exception as e:
      return f"An error occurred: {str(e)}", 500    

@app.route('/download/latest')
def download_latest():
  """Downloads the folder with the latest date from the server."""
  folder_name = get_latest_folder(download_folder)
  if folder_name is None:
    return "No folders found in download directory!", 404  
  """Downloads a folder from the server."""
  try:
    # Check if folder exists
    if not os.path.exists(os.path.join(download_folder, folder_name)):
      return "Folder not found!", 404

    # Send the entire folder as a compressed zip file (optional)
    # You can modify this to send individual files or a different archive format.
    archive_filename = f"{folder_name}.zip"
    archive_path = os.path.join(download_folder, archive_filename)
    with ZipFile(archive_path, 'w') as zip_file:
      for root, _, files in os.walk(os.path.join(download_folder, folder_name)):
        for file in files:
          file_path = os.path.join(root, file)
          zip_file.write(file_path, os.path.relpath(file_path, os.path.join(download_folder, folder_name)))
    return send_from_directory(download_folder, archive_filename, as_attachment=True)

  except Exception as e:
    return f"An error occurred: {str(e)}", 500



def get_latest_folder():
  """
  Identifies the folder with the latest date in the download directory.

  Returns:
      str: Path to the latest folder, or None if no folders are found.
  """
  latest_folder = None
  latest_date = None
  for folder in os.listdir(download_folder):
    folder_path = os.path.join(download_folder, folder)
    if os.path.isdir(folder_path):
      try:
        # Extract date from folder name (assuming a specific format)
        folder_date = datetime.datetime.strptime(folder, "%Y-%m-%d")  # Adjust date format based on your folder names
        if latest_date is None or folder_date > latest_date:
          latest_folder = folder_path
          latest_date = folder_date
          latest_folder = latest_folder.replace('.\\','')
      except ValueError:
        # Handle folders without a valid date format (optional: log or skip)
        pass
  return latest_folder


def find_nearest_folder(date_str):
  folder_path = '.'
  """
  Finds the nearest folder (in date format) to the given date in the specified folder path.

  Args:
      date_str: The date to search for (format YYYY-MM-DD).
      folder_path: The path to the directory containing date folders.

  Returns:
      The path to the nearest folder, or None if no folders are found or the date is invalid.
  """

  try:
    # Parse the given date string
    target_date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
  except ValueError:
    print("Invalid date format. Please use YYYY-MM-DD format.")
    return None

  # Get all folder names within the directory
  folder_names = [f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))]

  # Check if there are any folders
  if not folder_names:
    print("No folders found in the specified path.")
    return None

  # Find the nearest date folder (consider both earlier and later dates)
  nearest_date_diff = None
  nearest_folder = None
  for folder_name in folder_names:
    try:
      # Assuming folder names are already in YYYY-MM-DD format
      folder_date = datetime.datetime.strptime(folder_name, "%Y-%m-%d")
      date_diff = abs(folder_date - target_date)
      if nearest_date_diff is None or date_diff < nearest_date_diff:
        nearest_date_diff = date_diff
        nearest_folder = folder_name
    except ValueError:
      # Ignore folders with invalid names (not in date format)
      pass

  # Return the path to the nearest folder or None if no valid folders were found
  return nearest_folder

if __name__ == "__main__":
  app.run(debug=True)
