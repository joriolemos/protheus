# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 11:43:52 2026

@author: jlemos
"""

import time
import pyautogui

# arquivo com os seriais a serem incluidos
with open(r"C:/gitlocal/protheus/ordens.txt","r") as arquivo:
    ordens = arquivo.readlines()
n = len(ordens)
print(ordens)



# Indique a da data desejada para o registro do atendimento
date = "07042026"

time.sleep(5.0)

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
    