import glob
import json

palavras_povo = ["amiga", "amigas", "amigo", "amigos", "brasileiras", "brasileiros", "média", "popular", "cristã", "cristão",
"cristãos", "cristãs", "família", "Nordeste", "nordestina", "nordestinas", "nordestino", "nordestinos", "Norte", "pobre", "pobres",
"pobreza", "povo", "trabalhador", "trabalhadora", "trabalhadoras", "trabalhadores"]

palavras_elite = ["ambiental", "ambientalista", "ambientalistas", "banco", "bancos", "banqueiro", "banqueiros", "bandeira",
"classe alta", "classe política", "comunismo", "comunista", "comunistas", "corrupção", "corrupta", "corruptas", "corrupto",
"corruptos", "direita", "direitista", "demagogia", "dinheiro", "ditadura", "elite", "elites", "empreendedor", "empreendedora",
"empreendedoras", "empreendedores", "empresária", "empresarial", "empresárias", "empresário", "empresários", "esquerda",
"esquerdista", "Estado", "gay", "gays", "globalista", "globalistas", "ideologia", "ideologias", "ideológico", "índio", "índios",
"inimigo", "lgbt", "marajá", "marajás", "mercado," "minoria", "minorias", "ong", "pátria", "petista", "petistas", "petralha",
"petralhas", "populismo", "privilegiada", "privilegiadas", "privilegiado", "privilegiados", "privilégio", "privilégios", "PT",
"rica", "ricas", "rico", "ricos", "setor privado", "setor público", "socialismo", "socialista", "socialistas", "Sudeste", "Sul",
"totalitarismo"]

FOLDER = "C:/Users/Vitor/Documents/Faculdade/FLP0472 - Governo Representativo/FLP0472-Artigo/arquivos/extracted_TXT/FHC"

cont_povo = 0
cont_elite = 0

relatorio_file = open(FOLDER + "/Relatorio.txt", "r")
relatorio_string = ""
lines = relatorio_file.readlines()
for line in lines:
    new_line = line
    if '"' in line:
        new_line = new_line.replace("'", "")
    relatorio_string = relatorio_string + new_line
print(relatorio_string)
relatorio_dict = json.loads("{" + relatorio_string[0:-1].replace("'", '"') + "}")
for key in relatorio_dict:
    if key in palavras_povo:
        cont_povo = cont_povo + relatorio_dict[key]
    if key in palavras_elite:
        cont_elite = cont_elite + relatorio_dict[key]
analise = open(FOLDER + "/Analise.txt", "w")
analise.write("Povo:" + str(cont_povo))
analise.write("\nElite:" + str(cont_elite))
analise.close()
print("cont_povo:", cont_povo)
print("cont_elite:", cont_elite)
