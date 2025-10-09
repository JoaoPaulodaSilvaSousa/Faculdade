import os
import pandas as pd
from docx import Document
from PyPDF2 import PdfReader
from collections import Counter

# --- Caminho das pastas ---
pasta_estoque = r'C:\Users\João Paulo\Documents\GitHub\Faculdade\Trabalho_PM\Exportar_estoque'
cadastros = r'C:\Users\João Paulo\Documents\GitHub\Faculdade\Trabalho_PM\Cadastros_produtos'

# --- Extensões que o script vai ler ---
extensoes_estoque = [".txt", ".log", ".csv", ".docx", ".pdf"]

# --- Função para listar arquivos de uma pasta com determinadas extensões ---
def listar_arquivos(pasta, extensoes):
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
                    linhas.append(' '.join(linha.split()).lower())

    # CSV
    elif ext == ".csv":
        df = pd.read_csv(caminho, dtype=str).fillna('')
        for row in df.values:
            produto = ' '.join(str(v).strip() for v in row if v)
            if produto:
                linhas.append(produto.lower())

    # DOCX
    elif ext == ".docx":
        doc = Document(caminho)
        for p in doc.paragraphs:
            linha = p.text.strip()
            if linha and not linha.lower().startswith("produto"):
                linhas.append(' '.join(linha.split()).lower())

    # PDF
    elif ext == ".pdf":
        reader = PdfReader(caminho)
        for page in reader.pages:
            text = page.extract_text()
            if text:
                for linha in text.split("\n"):
                    linha = linha.strip()
                    if linha and not linha.lower().startswith("produto"):
                        linhas.append(' '.join(linha.split()).lower())
    else:
        return []

    return linhas

# --- Lê arquivos de estoque ---
arquivos_estoque = listar_arquivos(pasta_estoque, extensoes_estoque)
todos_produtos = []

if arquivos_estoque:
    print("📦 Arquivos de estoque encontrados:")
    for arq in arquivos_estoque:
        print(f"\n{arq}:")
        caminho = os.path.join(pasta_estoque, arq)
        conteudo = ler_arquivo(caminho)
        todos_produtos.extend(conteudo)
        for item in conteudo:
            print(f" - {item}")

    # --- Detectar duplicados ---
    contagem = Counter(todos_produtos)
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
arquivos_cadastros = listar_arquivos(cadastros, extensoes_estoque)
produtos_cadastros = []

for arq in arquivos_cadastros:
    caminho = os.path.join(cadastros, arq)
    conteudo = ler_arquivo(caminho)
    produtos_cadastros.extend(conteudo)

# --- Detecta produtos cadastrados que não estão no estoque ---
estoque_set = set(todos_produtos)
produtos_faltando = [p for p in produtos_cadastros if p not in estoque_set]

if produtos_faltando:
    print("\n⚠️ Produtos cadastrados que não estão no estoque:")
    for p in sorted(set(produtos_faltando)):
        print(f" - {p}")
else:
    print("\n✅ Todos os produtos cadastrados estão presentes no estoque.")
