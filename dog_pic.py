import requests
from PIL import Image
import matplotlib.pyplot as plt
import io

def fetch_dog_pic():
    url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(url)

    if response.status_code == 200:
        dog_data = response.json()
        img_data = requests.get(dog_data['message']).content
        img = Image.open(io.BytesIO(img_data))
        plt.imshow(img)
        plt.show()
    else:
        print(f"Failed to fetch dog picture")

fetch_dog_pic()
