import os
import shutil

categorias = {
    "Documentos": [".txt", ".docx", ".pdf"],
    "Músicas": [".mp3", ".wav"],
    "Imagens": [".jpg", ".jpeg", ".png", ".gif"],
    "Vídeos": [".mp4", ".avi", ".mkv"]
}

pasta_inicial = r"C:\Users\João Paulo\Desktop"

# Obter caminhos completos das pastas de destino
pastas_destino = [os.path.join(pasta_inicial, cat) for cat in categorias]

# Listar arquivos
for pasta_atual, subpastas, lista_arquivos in os.walk(pasta_inicial):
    # Ignorar pastas de destino
    subpastas[:] = [p for p in subpastas if os.path.join(pasta_atual, p) not in pastas_destino]

    for arquivo in lista_arquivos:
        caminho_arquivo = os.path.join(pasta_atual, arquivo)
        _, extensao = os.path.splitext(arquivo)

        for categoria, extensoes in categorias.items():
            if extensao.lower() in extensoes:
                pasta_destino = os.path.join(pasta_inicial, categoria)
                os.makedirs(pasta_destino, exist_ok=True)
                shutil.move(caminho_arquivo, os.path.join(pasta_destino, arquivo))
                print(f"Movido: {arquivo} → {categoria}")
                break
