import glob

FOLDER = "C:/Users/Vitor/Documents/Faculdade/FLP0472 - Governo Representativo/Artigo/FLP0472-Artigo/arquivos/extracted_TXT/Lula"
FILE = "/Relatorio.txt"

anos = glob.glob(FOLDER + "/*")

def cleanse_word(word):
    return word.lower().strip(',').strip('.').strip('\'').strip('"').strip('*').strip('?').strip('!').strip(';').strip(':')

word_freq = dict()
report_file = open(FOLDER + FILE, "w")
for ano in anos:
    arquivos = glob.glob(ano + "/*.txt")
    for arquivo in arquivos:
        file = open(arquivo, "r")
        for palavra in file.read().split():
            palavra = cleanse_word(palavra)
            try:
                word_freq[palavra] += 1
            except:
                word_freq.setdefault(palavra, 0)
sorted_word_freq = dict(sorted(word_freq.items(), key=lambda item: item[1], reverse=True))
report_file.write("\n".join("{!r}: {!r},".format(k, v) for k, v in sorted_word_freq.items()))
report_file.close()