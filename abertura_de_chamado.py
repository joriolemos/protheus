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
    pyautogui.write("TECA300")
    pyautogui.press("F3")
    time.sleep(30)
    pyautogui.press("i")
    time.sleep(6    )
    
    for i in range(0, n):
        
        time.sleep(2)
        pyautogui.press('enter',   presses=1, interval=1.0)
        pyautogui.write('10005Z')# Cliente
        time.sleep(1.0)
        pyautogui.write('03')# Loja do Cliente
        time.sleep(1.0)
        pyautogui.write('001414') # Código do produto
        time.sleep(1.0)
        pyautogui.press('tab',   presses=1, interval=1.0)
        pyautogui.press('2',   presses=1, interval=1.0)
        time.sleep(1.0)
        #pyautogui.press('tab',   presses=1, interval=1.0)
        pyautogui.write('JORIO') #nome do técnico
        time.sleep(1.0)
        #pyautogui.press('tab',   presses=8, interval=1.0)
        pyautogui.press('f2',   presses=1, interval=1.0)
        time.sleep(1.0)
        pyautogui.press('right',   presses=1, interval=1.0)
        pyautogui.press('3',   presses=1, interval=1.0)
        time.sleep(1.0)
        pyautogui.write('002')
        time.sleep(1.0)
        pyautogui.press('f3',   presses=1, interval=6.0)
        pyautogui.press('tab',   presses=4, interval=1.0)
        pyautogui.write(seriais[i])
        time.sleep(1.0)
        print(i)
        print(seriais[i])
        pyautogui.press('enter',   presses=1, interval=1.0)
        time.sleep(1.0)
        pyautogui.press('enter',   presses=1, interval=1.0)
        time.sleep(1.0)
        pyautogui.press('right',   presses=2, interval=1.0)
        time.sleep(1.0)
        pyautogui.write('0003')
        time.sleep(1.0)
        pyautogui.press('enter',   presses=1, interval=1.0)
        time.sleep(1.0)
        pyautogui.press('right',   presses=1, interval=1.0)
        pyautogui.press('enter',   presses=1, interval=1.0)
        pyautogui.write('MANUTENCAO PREVENTIVA')
        time.sleep(1.0)
        pyautogui.press('tab',   presses=1, interval=1.0)
        pyautogui.press('enter',   presses=1, interval=1.0)
        pyautogui.press('up',   presses=2, interval=1.0)
        pyautogui.hotkey('ctrl','s')
        time.sleep(7) 
            
    
    print("Login acionado automaticamente.")
except Exception as e:
    print(f"Erro ao abrir o TOTVS WebApp: {e}")
