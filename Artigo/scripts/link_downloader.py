import webbrowser
import glob
from time import sleep
import os
import sys

chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
path = 'C:/Users/Vitor/Documents/Faculdade/FLP0472 - Governo Representativo/Artigo/html_files/lula/*'
presidentes = glob.glob(path)

for presidente_ano in presidentes:
    file = open(presidente_ano + "/lista_download.txt", "r")
    lines = file.readlines()
    for line in lines:
        print(line)
        webbrowser.get(chrome_path).open(line)
