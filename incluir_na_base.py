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
        
        pyautogui.write('10005Z')# Cliente
        pyautogui.write('03')# Loja do Cliente
        pyautogui.write('3801000420') # Código do produto
        pyautogui.press('enter',   presses=1, interval=1.0)
        pyautogui.write(seriais[i])
        #pyautogui.press('enter',   presses=1, interval=1.0)
        print(i)
        print(seriais[i])
        pyautogui.write('28042026') #data da venda, ver nota fiscal
        time.sleep(1)
        pyautogui.write('08062026') #data da instalação, aproximada se não houver
        time.sleep(1)
        pyautogui.write('08062027') #data da garantia, verificar edital ou 1 ano
        pyautogui.press('tab', presses=4, interval=1.0)
        pyautogui.write('RAMON') #nome do técnico
        pyautogui.press('tab', presses=1, interval=1.0)
        pyautogui.write('CA00DG') # codigo do fornecedor
        time.sleep(1)
        pyautogui.write('01')
        pyautogui.press('tab', presses=2, interval=1.0)
        pyautogui.write('8000WD') #código do fabricante
        time.sleep(1)
        pyautogui.write('01')
        time.sleep(1)
        pyautogui.write('38405') #numero da NF de venda
        pyautogui.press('tab', presses=1, interval=1.0)
        
        if i == 0:
            pyautogui.write('Pedido de venda Nihon Kohden 14808 Oportunidade ORD0133353 NF-e 2026NE03870 Pregao numero 582/2025 ATA RP N 1299/2025 Local de entrega HDAMF Hospital Doutora Rita de Cassia Rua Prefeito Manoel Goncalves numero 825 Centro Barra de Sao Francisco ES CEP 29800000 Telefone 2737568462 CNPJ 27080605001915 Dados para pagamento Banco do Brasil AG 3131-3 CC 119978-1 CNPJ 14365637000196 O item QP-914PK Licenca de software sera instalado nas maquinas Calibracao e seguranca eletrica das 23 unidades de BSM constantes nesse pedido Valor do ICMS para a UF de destino R$ 32493.81 Duplicata 1 Valor 249952.48 Vencimento 26/05/26 Monitor BSM-3763 Life Scope VS 15 NK SpO2 Numeros de serie 27863 27864 27867 27868 27869 27870 27871 27872 27874 27875 27876 27865 27877 27879 27880 27866 27873 27878 27881 27882 Bateria recarregavel para BSM-3000 BSM-6000 modelo SB-671P LT 94193 UN 20 Sensor de SpO2 tipo Y adulto pediatrico e neonatal reutilizavel TL-220T BluPRO Numeros de serie 131392 131393 131394 131395 131396 131397 131398 131399 131400 131401 131402 131403 131404 131405 131406 131407 131408 131409 131410 131411 Manguito PNI adulto 16 cm range 33 a 45 cm Yawara YP-714T reutilizavel LT 406079711 UN 19') #observacao
            #pyautogui.press('tab', presses=1, interval=1.0)
        
        pyautogui.press('tab', presses=3, interval=1.0)
        
        pyautogui.write('HDRC') #sigla do hospital
        
        pyautogui.hotkey('ctrl','s')
        time.sleep(2)       
        
    
    print("Login acionado automaticamente.")
except Exception as e:
    print(f"Erro ao abrir o TOTVS WebApp: {e}")
