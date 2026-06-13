import subprocess
import sys

def download_dataset():
    command = f"{sys.executable} -m kaggle datasets download -d berkeleyearth/climate-change-earth-surface-temperature-data -p data/ --unzip"
    subprocess.run(command, shell=True)

if __name__ == "__main__":
    download_dataset()