# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 10:23:08 2026

@author: jlemos
"""

import pandas as pd
import subprocess
import time
import pyautogui


# URL do TOTVS WebApp
# url_totvs = "https://orthoheadinstrumentais119660.protheus.cloudtotvs.com.br:6700/webapp/"
url_totvs = "https://orthoheadinstrumentais119660.protheus.cloudtotvs.com.br:4010/webapp/"

# Caminho do navegador (exemplo com Edge, ajuste se necessário)
caminho_edge = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

# Ler Excel
df = pd.read_excel("cadastrar.xlsx")
print(df)

# Colunas texto
colunas_texto = [
    "CLIENTE",
    "LOJA",
    "COD_PRODUTO",
    "TECNICO",
    "FORNECEDOR",
    "LOJA_FORNECEDOR",
    "FABRICANTE",
    "LOJA_FABRICANTE",
    "OBSERVACAO",
    "SITE",
    "DESCRICAO",
    "SERIE",
    "NUM_NF"
]

for col in colunas_texto:
    df[col] = df[col].astype(str).str.strip()

# Datas
datas = [
    "DATA_VENDA",
    "DATA_INSTAL",
    "DATA_GARANTIA"
]

for col in datas:
    df[col] = pd.to_datetime(df[col], errors="coerce")

# Inteiros
inteiros = [
    "CNPJ",
    "PACK",
    "CHV_PRIM",
    "QTD"
]

for col in inteiros:
    df[col] = pd.to_numeric(df[col], errors="coerce").astype("Int64")

linhas = len(df)
lin = df.index.size
n = lin

print(lin)
print(linhas)
print()


D_CLIE = df["CLIENTE"]
D_LOJA = df["LOJA"].astype(str).str.zfill(2)
D_CODP = df["COD_PRODUTO"]
D_SERI = df["SERIE"]

    
D_VEND = df["DATA_VENDA"].dt.strftime("%d/%m/%Y")
D_INST = df["DATA_INSTAL"].dt.strftime("%d/%m/%Y")
D_GARA = df["DATA_GARANTIA"].dt.strftime("%d/%m/%Y")

D_TECN = df["TECNICO"]
D_FORN = df["FORNECEDOR"]
D_LFOR = df["LOJA_FORNECEDOR"].astype(str).str.zfill(2)
D_FABR = df["FABRICANTE"]
D_LFAB = df["LOJA_FABRICANTE"].astype(str).str.zfill(2)
D_NUNF = df["NUM_NF"]
D_OBSE = df["OBSERVACAO"]
D_SITE = df["SITE"]



print(D_CLIE[0])
print(D_LOJA[0])
print(D_VEND[0])
print(D_INST[0])
print(D_GARA[0])
print()


print(df.dtypes)

for _, linha in df.iterrows():

    registro = {
        "cliente": linha["CLIENTE"],
        "loja": linha["LOJA"],
        "cod_produto": linha["COD_PRODUTO"],
        "data_venda": linha["DATA_VENDA"],
        "data_instal": linha["DATA_INSTAL"],
        "data_garantia": linha["DATA_GARANTIA"],
        "nf": linha["NUM_NF"],
        "site": linha["SITE"],
        "descricao": linha["DESCRICAO"],
        "cnpj": linha["CNPJ"],
        "pack": linha["PACK"],
        "chave": linha["CHV_PRIM"],
        "qtd": linha["QTD"],
        "serie": linha["SERIE"]
    }

    # Aqui você salva em banco, API ou outra tela
    # print(registro)

try:
    # Abre o navegador com a URL
    #  subprocess.Popen([caminho_edge, "--new-window", url_totvs])
    proc = subprocess.Popen([caminho_edge, "--new-window", url_totvs])
    
    
    print("TOTVS WebApp aberto com sucesso!")
    
    # Aguarda alguns segundos para carregar a pagina inicial do app
    time.sleep(8)
    pyautogui.press("enter")    
    time.sleep(20)
    pyautogui.write("jlemos")
    pyautogui.press("tab", presses=1, interval=1.0)
    pyautogui.write("Jo@0509_rio")
    pyautogui.press("enter")
    time.sleep(8)
    pyautogui.press("tab", presses=9, interval=0.5)
    pyautogui.write("28")
    pyautogui.press("tab", presses=5, interval=0.5)
    pyautogui.press("enter")
    time.sleep(8)
    pyautogui.press("tab", presses=1, interval=1.0)
    pyautogui.write("TECA040")
    pyautogui.press("F3")
    time.sleep(20)
    pyautogui.press("i")
    time.sleep(3)
    
    for i in range(0, n):
        
        
        pyautogui.hotkey('ctrl','s')
        time.sleep(2)
        pyautogui.press("enter")
        time.sleep(2)
        pyautogui.write(D_CLIE[i])# Cliente
        time.sleep(1)
        pyautogui.write(D_LOJA[i])# Loja do Cliente
        time.sleep(1)
        pyautogui.write(D_CODP[i]) # Código do produto
        time.sleep(2)
        pyautogui.press('enter',   presses=1, interval=1.0)
        time.sleep(2)
        pyautogui.write(D_SERI[i])
        pyautogui.press('enter',   presses=1, interval=1.0)
        print(i)
        print(D_SERI[i])
        time.sleep(1)
        pyautogui.write(D_VEND[i]) #data da venda, ver nota fiscal
        time.sleep(1)
        pyautogui.write(D_INST[i]) #data da instalação, aproximada se não houver
        time.sleep(1)
        pyautogui.write(D_GARA[i]) #data da garantia, verificar edital ou 1 ano
        #time.sleep(1)
        pyautogui.press('tab', presses=4, interval=2.0)
        pyautogui.write(D_TECN[i]) #nome do técnico
        #time.sleep(1)
        pyautogui.press('tab', presses=1, interval=2.0)
        pyautogui.write(D_FORN[i]) # codigo do fornecedor
        time.sleep(2)
        pyautogui.write(D_LFOR[i])
        #time.sleep(2)
        pyautogui.press('tab', presses=2, interval=2.0)
        pyautogui.write(D_FABR[i]) #código do fabricante
        time.sleep(2)
        pyautogui.write(D_LFAB[i])
        time.sleep(1)
        pyautogui.write(D_NUNF[i]) #numero da NF de venda
        #time.sleep(1)
        pyautogui.press('tab', presses=1, interval=2.0)
        
        if i in {0, 12, 23, 34, 45, 56, 67, 78, 89, 100, 111, 122, 133, 144, 155}:
            pyautogui.write(D_OBSE[i]) #observacao
            #pyautogui.press('tab', presses=1, interval=1.0)
        
        pyautogui.press('tab', presses=3, interval=1.0)
        
        pyautogui.write(D_SITE[i]) #sigla do hospital
        time.sleep(1)
        
        pyautogui.hotkey('ctrl','s')
        time.sleep(3)
        
        if i in {11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 131, 143, 154}:
            #os.system("taskkill /im msedge.exe /f")
            time.sleep(5)
            proc.terminate()
            time.sleep(5)
            
            # Abre o navegador com a URL
            subprocess.Popen([caminho_edge, "--new-window", url_totvs])
            print("TOTVS WebApp aberto com sucesso!")
            
            # Aguarda alguns segundos para carregar a pagina inicial do app
            time.sleep(5)
            pyautogui.press("enter")    
            time.sleep(20)
            pyautogui.write("jlemos")
            pyautogui.press("tab", presses=1, interval=1.0)
            pyautogui.write("Jo@0509_rio")
            pyautogui.press("enter")
            time.sleep(8)
            pyautogui.press("tab", presses=9, interval=0.5)
            pyautogui.write("28")
            pyautogui.press("tab", presses=5, interval=0.5)
            pyautogui.press("enter")
            time.sleep(8)
            pyautogui.press("tab", presses=1, interval=1.0)
            pyautogui.write("TECA040")
            pyautogui.press("F3")
            time.sleep(20)
            pyautogui.press("i")
            time.sleep(3)         
            
               
    print("Login acionado automaticamente.")
except Exception as e:
    print(f"Erro ao abrir o TOTVS WebApp: {e}")