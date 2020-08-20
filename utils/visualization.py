import matplotlib.pyplot as plt
import requests
import seaborn as sns
import numpy as np

def download_image(url, filename="image.jpg"):
    r = requests.get(url)
    
    with open(filename, "wb") as f:
        f.write(r.content)
    return

def visualize(img, title, figsize: tuple=None):
    fig: plt.Figure = plt.figure()
    plt.gray()
    if figsize:
        fig.set_figwidth(figsize[0])
        fig.set_figheight(figsize[1])
    plt.imshow(img)
    plt.title(title)
    plt.axis("off")

def visualize_subplot(imgs: list, titles: list, division: tuple, figsize: tuple=None):
    fig: plt.Figure = plt.figure(figsize=figsize)
    if figsize:
        fig.set_figwidth(figsize[0])
        fig.set_figheight(figsize[1])

    plt.gray()
    assert len(imgs) == len(titles), "La lista de imágenes y de títulos debe ser del mismo tamaño"
    assert np.prod(division) >= len(imgs)

    for index, title in enumerate(titles):
        ax: plt.Axes = fig.add_subplot(division[0], division[1], index+1)
        ax.imshow(imgs[index])
        ax.set_title(titles[index])
        plt.axis("off")
    plt.show()