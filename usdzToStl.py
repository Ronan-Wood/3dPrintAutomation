import requests
from dotenv import load_dotenv
import os, requests

# Set the API endpoint and token
url = os.getenv('convert3dwebsite')
token = os.getenv('CONVERT3D_TOKEN')

# Set the file paths
input_file = "/Users/ronanwood/All Code/Python/3dPrintAutomation/Tb-messed-up-plane.usdz"  # Path to the USDZ file in the project folder
output_file = "/Users/ronanwood/All Code/Python/3dPrintAutomation/Tb-messed-up-plane.stl"  # Path to save the STL file

# Prepare the files and data for the request
files = {'file': open(input_file, 'rb')}
data = {
    'from_format': 'usdz',
    'to_format': 'stl'
}
headers = {
    'Authorization': f'Token {token}'
}

# Make the POST request to convert the file
response = requests.post(url, files=files, data=data, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Save the converted file
    with open(output_file, 'wb') as f:
        f.write(response.content)
    print(f"File converted and saved as {output_file}")
else:
    print(f"Error: {response.status_code}")
    print(response.text)
