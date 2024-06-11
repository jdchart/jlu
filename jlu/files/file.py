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
    if os.path.isdir(path) == False:
        os.makedirs(path)

    # Unzip:
    with zipfile.ZipFile(temp_zip, 'r') as zip_ref:
        zip_ref.extractall(path)
    
    # Remove temporary ip file:
    os.remove(temp_zip)