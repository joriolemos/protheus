# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 21:33:00 2026

@author: Jorio
"""

import subprocess
import time
import pyautogui

# URL do TOTVS WebApp
url_totvs = "https://orthoheadinstrumentais119660.protheus.cloudtotvs.com.br:4010/webapp/?P=SIGAMDI&E=PROD"

# Caminho do navegador (exemplo com Edge, ajuste se necessário)
caminho_edge = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

# arquivo com os seriais a serem incluidos
with open(r"C:/gitlocal/protheus/seriais.txt","r") as arquivo:
    seriais = arquivo.readlines()
n = len(seriais)
print(seriais)

try:
    # Abre o navegador com a URL
    subprocess.Popen([caminho_edge, "--new-window", url_totvs])
    print("TOTVS WebApp aberto com sucesso!")

    # Aguarda alguns segundos para carregar a pagina inicial do app
    time.sleep(30)
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
    time.sleep(6    )
    
    for i in range(0, n):
        
        time.sleep(2)
        
        pyautogui.write('10007A')# Cliente
        pyautogui.write('01')# Loja do Cliente
        pyautogui.write('3801000420') # Código do produto
        pyautogui.press('enter',   presses=1, interval=1.0)
        pyautogui.write(seriais[i])
        #pyautogui.press('enter',   presses=1, interval=1.0)
        print(i)
        print(seriais[i])
        pyautogui.write('27032026') #data da venda, ver nota fiscal
        time.sleep(1)
        pyautogui.write('15042026') #data da instalação, aproximada se não houver
        time.sleep(1)
        pyautogui.write('15042027') #data da garantia, verificar edital ou 1 ano
        pyautogui.press('tab', presses=4, interval=1.0)
        pyautogui.write('JORIO') #nome do técnico
        pyautogui.press('tab', presses=1, interval=1.0)
        pyautogui.write('CA00DG') # codigo do fornecedor
        time.sleep(1)
        pyautogui.write('01')
        pyautogui.press('tab', presses=2, interval=1.0)
        pyautogui.write('8000WD') #código do fabricante
        time.sleep(1)
        pyautogui.write('01')
        time.sleep(1)
        pyautogui.write('38118') #numero da NF de venda
        pyautogui.press('tab', presses=1, interval=1.0)
        
        pyautogui.hotkey('ctrl','s')
        time.sleep(2)       
        
    
    print("Login acionado automaticamente.")
except Exception as e:
    print(f"Erro ao abrir o TOTVS WebApp: {e}")
