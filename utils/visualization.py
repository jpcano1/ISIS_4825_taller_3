import matplotlib.pyplot as plt
import requests

def download_image(url, filename="image.jpg"):
    r = requests.get(url)
    
    with open(filename, "wb") as f:
        f.write(r.content)
    return

def visualize(img, title):
    plt.figure()
    if len(img.shape) == 2:
        plt.imshow(img, cmap="gray")
    else:
        plt.imshow(img)
        
    plt.title(title)
    plt.axis("off")