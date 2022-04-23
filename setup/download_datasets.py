import requests
from tqdm import tqdm

def download_file_from_google_drive(id, destination):
    URL = f"https://drive.google.com/u/0/uc?id={id}&export=download&confirm=t"
    session = requests.Session()
    response = session.post(URL, stream = True)
    save_response_content(response, destination)    

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None

def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in tqdm(response.iter_content(CHUNK_SIZE)):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
    