# -*- coding: utf-8 -*-
"""Color Segmentation Demo.ipynb
# **Documentar**
"""

import requests
from skimage import io
from skimage import color
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Planetas
# url = "https://github.com/PacktPublishing/Python-Image-Processing-Cookbook/blob/master/Chapter%2004/images/planets.png?raw=true"
# Loto
# url = "https://github.com/PacktPublishing/Python-Image-Processing-Cookbook/blob/master/Chapter%2004/images/lotus.png?raw=true"
# Flor
# url = "https://red-viajes.com/wp-content/uploads/2019/09/8-flores-tropicales-encontradas-en-tahiti.jpg"
# Flor del beso
# url = "https://www.guiadejardineria.com/wp-content/uploads/2015/04/Psychotria-elata-1.jpg"
# Colibrí 1
# url = "https://hablemosdeaves.com/wp-content/uploads/2017/06/colibr%C3%AD-azul-5-300x166.jpg"
# Colibrí 2
# url = "https://i.blogs.es/e56933/colibri/450_1000.jpg"

def download_image(url, filename="image.jpg"):
    r = requests.get(url)
    with open(filename, "wb") as f:
        f.write(r.content)
    img = io.imread(filename)
    print(f"The shape of the image is: {img.shape}")
    return img

def segmentation_demo(img, n_colors=(10, 8, 6, 4, 2)):
    if img.max() == 255:
        img = img / 255
    X = img.reshape(-1, 3)
    segmented_imgs = []

    for n_clusters in n_colors:
        kmeans = KMeans(n_clusters=n_clusters, random_state=1234).fit(X)
        segmented_img = kmeans.cluster_centers_[kmeans.labels_]
        segmented_imgs.append(segmented_img.reshape(img.shape))

    plt.figure(figsize=(10, 5))

    plt.subplot(231)
    plt.imshow(img)
    plt.title("Imagen Original")
    plt.axis("off")

    for idx, n_clusters in enumerate(n_colors):
        plt.subplot(2, 3, 2 + idx)
        plt.imshow(segmented_imgs[idx])
        plt.title(f"{n_clusters} Colores")
        plt.axis("off")

    plt.show()
    return segmented_imgs

def segmentation_grayscale(img, n_colors=(10, 8, 6, 4, 2)):
    plt.gray()
    img_gray = color.rgb2gray(img)
    X = img_gray.reshape(-1, 1)

    segmented_imgs = []

    for n_clusters in n_colors:
        kmeans = KMeans(n_clusters=n_clusters, random_state=1234).fit(X)
        segmented_img = kmeans.cluster_centers_[kmeans.labels_]
        segmented_imgs.append(segmented_img.reshape(img_gray.shape))

    plt.figure(figsize=(10, 5))

    plt.subplot(231)
    plt.imshow(img_gray)
    plt.title("Imagen Original")
    plt.axis("off")

    for idx, n_clusters in enumerate(n_colors):
        plt.subplot(2, 3, 2 + idx)
        plt.imshow(segmented_imgs[idx])
        plt.title(f"{n_clusters} Colores")
        plt.axis("off")

    plt.show()
    return segmented_imgs
