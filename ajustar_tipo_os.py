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
with open(r"C:/gitlocal/protheus/ordens.txt","r") as arquivo:
    ordens = arquivo.readlines()
n = len(ordens)
print(ordens)


try:
    # Abre o navegador com a URL
    subprocess.Popen([caminho_edge, "--new-window", url_totvs])
    print("TOTVS WebApp aberto com sucesso!")
        
    # Aguarda alguns segundos para carregar a pagina inicial do app
    time.sleep(20)
    pyautogui.write("jlemos")
    pyautogui.press("tab", presses=1, interval=1.0)
    pyautogui.write("Jo@0509_rio")
    pyautogui.press("enter")
    time.sleep(10)
    pyautogui.press("tab", presses=9, interval=1.0)
    pyautogui.write("28")
    pyautogui.press("tab", presses=5, interval=1.0)
    pyautogui.press("enter")
    time.sleep(10)
    pyautogui.press("tab", presses=1, interval=1.0)
    pyautogui.write("TECA450")
    pyautogui.press("F3")
    time.sleep(20)

    
    for i in range(0, n):
        
        osatual = ordens[i]

    
        pyautogui.press("p")
        time.sleep(2.0)
        pyautogui.press("enter", presses=1, interval=1.0)
    
        pyautogui.write(osatual)
        pyautogui.press("enter", presses=2, interval=1.0)
        time.sleep(2.0)
        pyautogui.press("a", presses=1, interval=1.0)
        time.sleep(2.0)
        pyautogui.write("23")          #MODIFIQUE PARA O COD DE TIPO DESEJADO
        time.sleep(1.0)
        #pyautogui.press("enter", presses=1, interval=1.0)
        #time.sleep(1.0)
        pyautogui.write("03")          #MODIFIQUE PARA O COD DE TIPO DESEJADO
        time.sleep(1.0)
    
        pyautogui.hotkey('ctrl', 's')
        time.sleep(3)

    
    print("Login acionado automaticamente.")
except Exception as e:
    print(f"Erro ao abrir o TOTVS WebApp: {e}")
