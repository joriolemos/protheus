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

# Indique a da data desejada para o registro do atendimento
date = "07042026"

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
    pyautogui.press("tab", presses=9, interval=0.5)
    pyautogui.write("28")
    pyautogui.press("tab", presses=5, interval=0.5)
    pyautogui.press("enter")
    time.sleep(10)
    pyautogui.press("tab", presses=1, interval=1.0)
    pyautogui.write("TECA460")
    pyautogui.press("F3")
    time.sleep(20)
    pyautogui.press("i")
    time.sleep(6    )
    
    for i in range(0, n):
        
        osatual = ordens[i]
    
        pyautogui.write(osatual)
    #   pyautogui.write("01")
        pyautogui.write("JORIO")
        time.sleep(1.0)
        pyautogui.press("enter", presses=1, interval=1.0)
        pyautogui.write(date)
        time.sleep(1.0)
        pyautogui.write("0800")
        time.sleep(1.0)
        pyautogui.write(date)
        time.sleep(1.0)
        pyautogui.write("1700")
        time.sleep(1.0)
        pyautogui.write(date)
        time.sleep(1.0)
        pyautogui.write("0800")
        time.sleep(1.0)
        pyautogui.write(date)
        time.sleep(1.0)
        pyautogui.write("1700")
        time.sleep(1.0)
        pyautogui.write("0000")
        time.sleep(2)
        pyautogui.press("enter", presses=1, interval=1.0)
        pyautogui.press("s")
        pyautogui.press("enter", presses=1, interval=1.0)
        
        
        if i != 0:
              pyautogui.press("enter")
              time.sleep(1.0)
           
        #pyautogui.press("enter", presses=1, interval=1.0)
        time.sleep(2)
        pyautogui.press("space", presses=1, interval=1.0)
        time.sleep(2)
        pyautogui.press("up", presses=1, interval=1.0)
        time.sleep(2)
        pyautogui.press("enter", presses=1, interval=1.0)
        
        
        pyautogui.press("enter", presses=3, interval=1.0)
        pyautogui.write("ATENDIMENTO DE INSTALACAO")
        pyautogui.press("enter", presses=1, interval=1.0)
        pyautogui.write("EQUIPAMENTO EM CONFORMIDADE")
        
        pyautogui.press("tab")
        pyautogui.write("0000")
        pyautogui.press("enter", presses=1, interval=1.0)
        pyautogui.press("f2")
        pyautogui.press("enter", presses=1, interval=1.0)    
        pyautogui.press("tab", presses=3, interval=1.0)
        
        pyautogui.press("enter", presses=1, interval=1.0)
        pyautogui.press("enter", presses=1, interval=1.0)
        
    
        pyautogui.press("down", presses=1, interval=1.0)
        pyautogui.press("right", presses=1, interval=1.0)
        pyautogui.write("SG04000018")
        pyautogui.press("enter", presses=3, interval=1.0)
        pyautogui.write("1")
        time.sleep(2)
        pyautogui.press("enter", presses=6, interval=1.0)
        pyautogui.write("000002")
        
        pyautogui.press("down", presses=1, interval=1.0)
        pyautogui.press("right", presses=1, interval=1.0)
        pyautogui.write("SM01000257")
        pyautogui.press("enter", presses=3, interval=1.0)
        pyautogui.write("1")
        time.sleep(2)
        pyautogui.press("enter", presses=6, interval=1.0)
        pyautogui.write("000002")
        
        pyautogui.press("down", presses=1, interval=1.0)
        pyautogui.press("right", presses=1, interval=1.0)
        pyautogui.write("S002000004")
        pyautogui.press("enter", presses=3, interval=1.0)
        pyautogui.write("1")
        time.sleep(2)
        pyautogui.press("enter", presses=6, interval=1.0)
        pyautogui.write("000002")
        
        
        pyautogui.press("up", presses=3, interval=1.0)
        pyautogui.press("left", presses=7, interval=1.0)
        pyautogui.press("del", presses=1, interval=1.0)
        
        
        pyautogui.hotkey('ctrl', 's')
        time.sleep(5)
        pyautogui.hotkey('ctrl', 's')
        time.sleep(5)
            
    
    print("Login acionado automaticamente.")
except Exception as e:
    print(f"Erro ao abrir o TOTVS WebApp: {e}")
