import os
import requests
import zipfile

def download_zip(url, path):
    """Download a zip file and unpack it's contents at the given path (a folder of the filename will be created)."""
    
    # Download file:
    response = requests.get(url)
    temp_zip = os.path.join(path, os.path.basename(url))
    with open(temp_zip, 'wb') as file:
        file.write(response.content)

    # Create the output folder:
    out_folder = os.path.splitext(temp_zip)[0]
    if os.path.isdir(out_folder) == False:
        os.makedirs(out_folder)

    # Unzip:
    with zipfile.ZipFile(temp_zip, 'r') as zip_ref:
        zip_ref.extractall(out_folder)
    
    # Remove temporary ip file:
    os.remove(temp_zip)