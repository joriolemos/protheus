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
    pyautogui.write("22")
    pyautogui.press("tab", presses=5, interval=0.5)
    pyautogui.press("enter")
    time.sleep(8)
    pyautogui.press("tab", presses=1, interval=1.0)
    pyautogui.write("QMTA140")
    pyautogui.press("F3")
    time.sleep(20)
    
    pyautogui.press("i")
    time.sleep(5)

    
    for i in range(0, n):
        
        serialatual = seriais[i]

    
        #pyautogui.press("p")
        #time.sleep(2.0)
        #pyautogui.press("enter", presses=1, interval=1.0)
    
        pyautogui.write(serialatual)
        pyautogui.press("enter", presses=4, interval=1.0)
        time.sleep(2.0)
        
        pyautogui.write("0400")
        pyautogui.write("25ºC +/- 5ºC / 60% +/- 15%")
        
            
        pyautogui.press("enter", presses=2, interval=1.0)
        pyautogui.press("n", presses=2, interval=1.0)
        time.sleep(2.0)
        
        
        
        pyautogui.press("a", presses=1, interval=1.0)
        time.sleep(2.0)
        
        pyautogui.press("tab", presses=2, interval=1.0)
        pyautogui.write(serialatual)
        pyautogui.press("enter", presses=1, interval=1.0)

        pyautogui.write("MONITOR BEIRA LEITO BSM-3763 T")
        pyautogui.press("enter", presses=1, interval=1.0)

        pyautogui.write("30")
        
        pyautogui.write("01302127")
        pyautogui.press("enter", presses=1, interval=1.0)
        time.sleep(2.0)

        pyautogui.write("07042026")
        time.sleep(2.0)
        pyautogui.write("365")
        
        pyautogui.press("enter", presses=2, interval=1.0)
           
        pyautogui.hotkey('ctrl', 's')
        time.sleep(5)

    
    print("Login acionado automaticamente.")
except Exception as e:
    print(f"Erro ao abrir o TOTVS WebApp: {e}")
