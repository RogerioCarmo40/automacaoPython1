#!/usr/bin/env python
# coding: utf-8

# In[269]:


import pyautogui
import pyperclip
import time

pyautogui.PAUSE = 1

#Analista
pyautogui.click(x=-1208, y=415, clicks=1)

time.sleep(1.5)

pyautogui.click(x=-1214, y=578, clicks=1)

time.sleep(1.5)

#Origem da demanda
pyautogui.click(x=-1209, y=580, clicks=1)

time.sleep(1.5)

pyautogui.click(x=-1203, y=646, clicks=1)

time.sleep(1.5)

#Município demandante
pyautogui.click(x=-1257, y=742, clicks=1)
pyautogui.write("Cuiaba")

time.sleep(1.5)

#Setor de Origem da Demanda 
pyautogui.click(x=-1224, y=916, clicks=1)

time.sleep(1.5)

pyautogui.click(x=-1218, y=870, clicks=1)

time.sleep(1.5)

#rolagem da página 
pyautogui.scroll(-800)  # scroll down 800 "clicks"

time.sleep(1.5)

#Número do processo
pyautogui.click(x=-1252, y=142, clicks=1)
pyautogui.write("NA2308019000100073-3")

time.sleep(1.5)

#Mês de Referência
pyautogui.click(x=-1212, y=295, clicks=1)

time.sleep(1.5)

#escolha do mês
#pyautogui.click(x=-1225, y=606, clicks=1) junho
#pyautogui.click(x=-1239, y=653, clicks=1) julho
pyautogui.click(x=-1237, y=700, clicks=1)

time.sleep(1.5)

#Relatório produzido
pyautogui.click(x=-1191, y=459, clicks=1)

time.sleep(1.5)

pyautogui.click(x=-1167, y=526, clicks=1)

time.sleep(1.5)

#Número do Relatório
pyautogui.click(x=-1262, y=623, clicks=1)
pyautogui.write("REL 189-2023")

time.sleep(1.5)

#Busca de arquivo
pyautogui.click(x=-1219, y=784, clicks=1)

time.sleep(20)

#Botão enviar
pyautogui.click(x=-1270, y=871, clicks=1)


# In[233]:


time.sleep(3)
pyautogui.position()


# In[ ]:





# In[ ]:




