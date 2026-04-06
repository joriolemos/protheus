# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 09:23:53 2022

@author: jlemos
"""

import time
#import subprocess
#import pandas as pd
import pyautogui as pa
import win32clipboard as wc
import webbrowser

#%%
wc.OpenClipboard()
wc.EmptyClipboard()
wc.CloseClipboard()

with open(r"C:/gitlocal/protheus/seriais.txt","r") as arquivo:
    orcamentos = arquivo.readlines()
n = len(orcamentos)
print(orcamentos)


#%%
# URL to be opened
url = "https://orthoheadinstrumentais119660.protheus.cloudtotvs.com.br:4010/webapp/?P=SIGAMDI&E=PROD"

# Open the URL in the default web browser
webbrowser.open(url)



time.sleep(20)
pa.write("jlemos")
time.sleep(1)
pa.press("tab")
pa.write("Jo@0509_rio")
time.sleep(1)
pa.press('enter',   presses=1, interval=0.5)

#%%
time.sleep(10)
pa.press('tab',     presses=9, interval=0.5)
pa.write("28",      interval=0.5)
pa.press('tab',     presses=5, interval=0.5)
pa.press('enter',   presses=1, interval=0.5)
time.sleep(60)

#%%
pa.press('tab',     presses=1, interval=1)
pa.write('TECA400')
pa.press('f3',      presses=1,  interval=1)
time.sleep(15)

#%%

time.sleep(5)
for i in range(0, n):
    
    time.sleep(2)
    pa.press('p')
    time.sleep(1)
    pa.press('tab',      presses=1, interval=1)
#   time.sleep(2)
    pa.write(orcamentos[i])
    print(i)
    print(orcamentos[i])
    pa.press('enter',    presses=2, interval=1)
    time.sleep(2)
    pa.press('a')
    time.sleep(2)
    pa.write('12')
    pa.press('tab',      presses=5, interval=0.1)
    pa.write('008')
    pa.press('f2',       presses=1, interval=1)
    time.sleep(0.5)
    pa.press('right',    presses=1, interval=0.25)
    pa.press('enter',    presses=1, interval=0.25)
    pa.press('3',        presses=1, interval=0.25)
    pa.press('right',    presses=3, interval=0.25)
    pa.press('enter',    presses=3, interval=0.25)
    pa.press('up',       presses=2, interval=0.25)
    pa.write("Encerrado por prazo prolongado de resposta do cliente")
    pa.press('tab',      presses=1, interval=0.5)
    pa.press('enter',    presses=1, interval=0.5)
    time.sleep(2)
    pa.hotkey('ctrl','s')

