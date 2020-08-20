# -*- coding: utf-8 -*-
import requests
from skimage import io
from skimage import color
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

url = "https://cdn.images.express.co.uk/img/dynamic/130/590x/Can-I-drive-to-exercise-or-walk-dog-coronavirus-rules-1262564.jpg?r=1587021728582"

def download_image(url, filename="image.jpg"):
    r = requests.get(url)
    with open(filename, "wb") as f:
        f.write(r.content)
    return io.imread(filename)

img = download_image(url)

def segmentation_demo(img):
    if img.max() == 255:
        img = img / 255
    X = img.reshape(-1, 3)
    segmented_imgs = []
    n_colors = (10, 8, 6, 4, 2)

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

def segmentation_grayscale(img):
    img_gray = color.rgb2gray(img)
    X = img_gray.reshape(-1, 1)

    segmented_imgs = []
    n_colors = (10, 8, 6, 4, 2)

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

segmented_imgs = segmentation_demo(img)

