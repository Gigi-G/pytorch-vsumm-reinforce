import os
import glob
import zipfile
from tqdm import tqdm
from setup.download_datasets import download_file_from_google_drive

def main():
    new_dir = ["log", "output/frames"]
    file_id = '11xq3MANiUYKt36-mpNHwIx9gFx4siL4X'
    destination = 'datasets.zip'
    files = [(f.replace(".\\", "").replace("./", "")) for f in glob.glob(pathname="./*")]
    for dir in new_dir:
        if dir not in files:
            try:
                os.makedirs(name=dir)
            except:
                continue
    if "datasets.zip" not in files:
        download_file_from_google_drive(file_id, destination)
    if "datasets" not in files:
        with zipfile.ZipFile("datasets.zip", 'r') as zip_ref:
            for member in tqdm(zip_ref.infolist(), desc='Extracting datasets '):
                try:
                    zip_ref.extract(member, ".")
                except zipfile.error as e:
                    pass
    print("Setup is successfull finished.")

if __name__ == '__main__':
    main()