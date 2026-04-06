# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 21:33:00 2026

@author: Jorio
"""

import subprocess
import time
import pyautogui

# URL do TOTVS WebApp
url_totvs = "https://orthoheadinstrumentais119660.protheus.cloudtotvs.com.br:4010/webapp/#/login"

# Caminho do navegador (exemplo com Edge, ajuste se necessário)
caminho_edge = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

try:
    # Abre o navegador com a URL
    subprocess.Popen([caminho_edge, "--new-window", url_totvs])
    print("TOTVS WebApp aberto com sucesso!")

    # Aguarda alguns segundos para carregar a pagina inicial do app
    time.sleep(3)

    # Pressiona Tab 3 vezes de uma vez
    pyautogui.press("tab", presses=3, interval=0.5)

    # Pressiona Enter
    pyautogui.press("enter")
    
    # Aguarda alguns segundos para carregar a pagina boas-vindas
    time.sleep(10)
    
    pyautogui.write("jlemos")

    # Pressiona Tab 3 vezes de uma vez
    pyautogui.press("tab", presses=1, interval=0.5)
    
    pyautogui.write("Jo@0509_rio")

    # Pressiona Enter
    pyautogui.press("enter")
    
    # Aguarda alguns segundos para carregar a pagina inicial do app
    time.sleep(8)

    # Pressiona Tab 3 vezes de uma vez
    pyautogui.press("tab", presses=9, interval=0.5)
    
    pyautogui.write("28")
    
    pyautogui.press("tab", presses=5, interval=0.5)

    # Pressiona Enter
    pyautogui.press("enter")
    
    time.sleep(5)
    
    # Pressiona Tab 3 vezes de uma vez
    pyautogui.press("tab", presses=1, interval=0.5)
    
    pyautogui.write("TECA300")
    
    pyautogui.press("F3")
    
    
    print("Login acionado automaticamente.")
except Exception as e:
    print(f"Erro ao abrir o TOTVS WebApp: {e}")
