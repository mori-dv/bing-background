#! /usr/bin/python3
from bs4 import BeautifulSoup
import requests
import re
import os
def get_url():
    r = requests.get("https://www.bing.com")
    soup = BeautifulSoup(r.text, 'html.parser')
    text = ''
    for link in soup.find_all('link'):
        text = str(link.get('href')) + "\n" + text
    for url in re.findall(r'.*jpg', text):
        return ("https://www.bing.com"+url)
def os_changes():
    os.chdir('/home/Wallpapers')
    try:
        os.remove('*.jpg')
    except FileNotFoundError:
        os.system(f'wget --output-document=wallpaper.jpg {get_url()}')
    # changing gnome background
    os.system('gsettings set org.gnome.desktop.background picture-uri "/home/Wallpapers/wallpaper.jpg"')
    # make a log file that save a data everytime program run in this directory: /home/Wallpapers
    os.system('date >> /home/mori/Docs/log.txt')
 

os_changes()
