# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 21:33:00 2026

@author: Jorio
"""

import subprocess
import time
import pyautogui
#import os

# URL do TOTVS WebApp
url_totvs = "https://orthoheadinstrumentais119660.protheus.cloudtotvs.com.br:6700/webapp/"


# Caminho do navegador (exemplo com Edge, ajuste se necessário)
caminho_edge = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

# arquivo com os seriais a serem incluidos
with open(r"C:/gitlocal/protheus/seriais.txt","r") as arquivo:
    seriais = arquivo.readlines()
n = len(seriais)
print(seriais)

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
        pyautogui.write('10005Z')# Cliente
        time.sleep(1)
        pyautogui.write('03')# Loja do Cliente
        time.sleep(1)
        pyautogui.write('3801000420') # Código do produto
        time.sleep(2)
        pyautogui.press('enter',   presses=1, interval=1.0)
        time.sleep(2)
        pyautogui.write(seriais[i])
        #pyautogui.press('enter',   presses=1, interval=1.0)
        print(i)
        print(seriais[i])
        time.sleep(1)
        pyautogui.write('18062026') #data da venda, ver nota fiscal
        time.sleep(1)
        pyautogui.write('16072026') #data da instalação, aproximada se não houver
        time.sleep(1)
        pyautogui.write('16072027') #data da garantia, verificar edital ou 1 ano
        pyautogui.press('tab', presses=4, interval=2.0)
        pyautogui.write('JORIO') #nome do técnico
        pyautogui.press('tab', presses=1, interval=2.0)
        pyautogui.write('CA00DG') # codigo do fornecedor
        time.sleep(1)
        pyautogui.write('01')
        pyautogui.press('tab', presses=2, interval=2.0)
        pyautogui.write('8000WD') #código do fabricante
        time.sleep(1)
        pyautogui.write('01')
        time.sleep(1)
        pyautogui.write('39046') #numero da NF de venda
        pyautogui.press('tab', presses=1, interval=2.0)
        
        if i in {0, 12, 23, 34, 45, 56, 67, 78, 89}:
            pyautogui.write('Pregao numero 582/2025 ATA RP N 1299/2025') #observacao
            #pyautogui.press('tab', presses=1, interval=1.0)
        
        pyautogui.press('tab', presses=3, interval=1.0)
        
        pyautogui.write('HSJC') #sigla do hospital
        
        pyautogui.hotkey('ctrl','s')
        time.sleep(3)
        
        if i in {11, 22, 33, 44, 55, 66, 77, 88}:
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
