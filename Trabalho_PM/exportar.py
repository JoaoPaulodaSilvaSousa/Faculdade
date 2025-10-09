import os
import pandas as pd # Ler arquivos .csv, .xlsx, .json, etc.,
from docx import Document # Lê/cria documentos do Word (.docx)
from PyPDF2 import PdfReader # Usado para ler o texto de arquivos PDF.
from collections import Counter # Conta quantas vezes algo aparece (palavras, números, etc.)

# --- Caminho das pastas ---
pasta_estoque = r'C:\Users\João Paulo\Documents\GitHub\Faculdade\Trabalho_PM\Exportar_estoque'
cadastros = r'C:\Users\João Paulo\Documents\GitHub\Faculdade\Trabalho_PM\Cadastros_produtos'

# --- Extensões que o script vai ler ---
extensoes_estoque = [".txt", ".log", ".csv", ".docx", ".pdf"]

# --- Função para listar arquivos de uma pasta com determinadas extensões ---
def listar_arquivos_estoque(pasta, extensoes):
    return [arquivo for arquivo in os.listdir(pasta)
            if any(arquivo.lower().endswith(ext) for ext in extensoes)]

# --- Função para ler arquivos de diferentes formatos ---
def ler_arquivo(caminho):
    _, ext = os.path.splitext(caminho)
    ext = ext.lower()
    linhas = []

    # TXT e LOG
    if ext in [".txt", ".log"]:
        with open(caminho, "r", encoding="utf-8") as f:
            for linha in f:
                linha = linha.strip()
                if linha and not linha.lower().startswith("produto"):
                    linha = ' '.join(linha.split())  # remove múltiplos espaços
                    linhas.append(linha)

    # CSV
    elif ext == ".csv":
        df = pd.read_csv(caminho)
        # Garantir que o CSV tenha pelo menos 2 colunas
        if df.shape[1] >= 2:
            for row in df.values:
                # Normaliza espaços e junta colunas
                produto = f"{str(row[0]).strip()} {str(row[1]).strip()}"
                linhas.append(' '.join(produto.split()))
        else:
            # Se tiver apenas uma coluna, pega só ela
            for row in df.values:
                produto = str(row[0]).strip()
                linhas.append(produto)

    # DOCX
    elif ext == ".docx":
        doc = Document(caminho)
        for p in doc.paragraphs:
            linha = p.text.strip()
            if linha and not linha.lower().startswith("produto"):
                linha = ' '.join(linha.split())
                linhas.append(linha)

    # PDF
    elif ext == ".pdf":
        reader = PdfReader(caminho)
        for page in reader.pages:
            text = page.extract_text()
            if text:
                for linha in text.split("\n"):
                    linha = linha.strip()
                    if linha and not linha.lower().startswith("produto"):
                        linha = ' '.join(linha.split())
                        linhas.append(linha)

    # Caso a extensão não seja suportada
    else:
        return []

    return linhas

# --- Lê arquivos de estoque ---
if arquivos_encontrados:
    print("📦 Arquivos de estoque encontrados:")
    for arq in arquivos_encontrados:
        print(f"\n {arq}:")
        caminho = os.path.join(pasta_estoque, arq)
        conteudo = ler_arquivo(caminho)
        todos_produtos.extend(conteudo)
        for item in conteudo:
            print(f" - {item}")

    # --- Detectar duplicados ---
    # Normaliza tudo em minúsculas para evitar falsos negativos
    contagem = Counter([p.lower() for p in todos_produtos])
    duplicados = [item for item, qtd in contagem.items() if qtd > 1]

    if duplicados:
        print("\n⚠️ Produtos duplicados encontrados no estoque:")
        for item in duplicados:
            print(f" - {item} ({contagem[item]} vezes)")
    else:
        print("\n✅ Nenhum produto duplicado encontrado.")
else:
    print("⚠️ Nenhum arquivo de estoque encontrado na pasta.")

# --- Lê arquivos de cadastros ---
arquivos_cadastros = listar_arquivos_estoque(cadastros, extensoes_estoque)
produtos_cadastros = []

for arq in arquivos_cadastros:
    caminho = os.path.join(cadastros, arq)
    conteudo = ler_arquivo(caminho)
    produtos_cadastros.extend(conteudo)

# --- Detecta produtos cadastrados que não estão no estoque ---
# Normaliza strings para evitar problemas com maiúsculas/minúsculas e espaços
estoque_normalizado = [p.lower().strip() for p in todos_produtos]
produtos_faltando = [p for p in produtos_cadastros if p.lower().strip() not in estoque_normalizado]

if produtos_faltando:
    print("\n⚠️ Produtos cadastrados que não estão no estoque da planiha de exportação do estoque!")
    for p in set(produtos_faltando):  # mostra apenas únicos
        print(f" - {p}")
else:
    print("\n✅ Todos os produtos cadastrados estão presentes no estoque.")
