import os #serve para interagir com o sistema operacional
import shutil #serve para manipulção de arquivos e pastas

categorias = {
    "Documentos": [".txt", ".docx", ".pdf", ],
    "Músicas": [".mp3", ".wav"],
    "Imagens": [".jpg", ".jpeg", ".png", ".gif"],
    "Vídeos": [".mp4", ".avi", ".mkv"]
}

pasta_inicial = os.getcwd() #recebe o diretório atual de onde o programa ta rodando

#Listar os arquivos
for pasta_atual, subpastas, lista_arquivos in os.walk(pasta_inicial): #percorre todos os diretórios e subdiretórios da pasta inicial.
    for arquivo in lista_arquivos:
        caminho_arquivo = os.path.join(pasta_atual, arquivo) #junta o caminho da pasta com o nome do arquivo

        #Pegar  do arquivo
        _, extensao = os.path.splitext(arquivo) #_ ignora o nome, pois só a extensão é necessária || os.path.splitext erve para separar o nome do arquivo da sua extensão

        for categoria, extensoes in categorias.items():
            if extensao.lower() in extensoes:
                # Criar pasta se não existir
                pasta_destino = os.path.join(pasta_inicial, categoria) #Cria o caminho completo da pasta de destino

                os.makedirs(pasta_destino, exist_ok=True)

                # Mover arquivo
                shutil.move(caminho_arquivo, os.path.join(pasta_destino, arquivo)) #Move o arquivo para a pasta de destino.

                print(f"Movido: {arquivo} → {categoria}")
                break # Arquivo já movido, não precisa continuar no loop de categorias