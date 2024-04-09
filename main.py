import os
import random
import time

import requests
from bs4 import *


def get_imgs(aspect_ratio, URL):
    os.system(
        f"""notify-send -a "Wallpaper Changer" -i "daily-wallpaper" "The wallpaper will change to another one" """)
    aspect_ratio = aspect_ratio
    URL = URL
    print(URL)
    website = requests.get(URL).content
    img_array = []

    soup = BeautifulSoup(website, 'html.parser')

    all_links = soup.find_all('img', class_="wallpapers__image")

    for link in all_links:
        img_link = link['src']
        img_array.append(img_link.replace("300x188", aspect_ratio))

    with open("./wallpapers_num", "r") as filez:
        num_of_wallpapers_used = int(filez.read().strip())

    img_to_get = (num_of_wallpapers_used - ((num_of_wallpapers_used // 15) * 15))
    download = requests.get(img_array[img_to_get])
    print(img_array[img_to_get])

    with open(f'/home/abc/Pictures/art-{num_of_wallpapers_used}.jpg', 'wb') as filey:
        filey.write(download.content)

    os.system(f"rm '/home/abc/Pictures/art-{num_of_wallpapers_used - 1}.jpg' ")

    os.system(f"""plasma-apply-wallpaperimage "/home/abc/Pictures/art-{num_of_wallpapers_used}.jpg" """)

    with open("wallpapers_num", "w") as new_file:
        new_file.write(str(num_of_wallpapers_used + 1))


img_aspect_ratio = "3840x2400"
page_url = f"https://wallpaperscraft.com/catalog/art/{img_aspect_ratio}"

with open("/home/abc/Scripts/Wallpaper-art-trial/wallpapers_num", "r") as file:
    num_of_walls = int(file.read()) + 1

if (num_of_walls // 15) > 0:
    page_url = f"https://wallpaperscraft.com/catalog/art/{img_aspect_ratio}/page{(num_of_walls // 15) + 1}"

get_imgs(img_aspect_ratio, page_url)
