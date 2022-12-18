import re
import codecs
import glob

path = 'C:/Users/Vitor/Documents/Faculdade/FLP0472 - Governo Representativo/Artigo/html_files/*/*'
presidentes = glob.glob(path)

for presidente in presidentes:
    download_file = open(presidente + "/lista_download.txt", "w")
    files = glob.glob(presidente + '/*.html')
    for file in files:
        f=codecs.open(file, 'r', encoding="utf-8")
        txt = f.read()
        x = re.findall(r'summary url</span>" <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="(.*?)view', txt)
        for item in x:
            splitado = item.split("/")
            if (".pdf" in splitado[-2]):
                download_name = item + "@@download/file/" + splitado[-2]
            else:
                download_name = item + "@@download/file/" + splitado[-2] + ".pdf"

            download_file.write(download_name + "\n")
    download_file.close()
