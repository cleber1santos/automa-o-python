import pyautogui
from time import sleep
import csv
import pandas as pd


pyautogui.click(123,253,duration=5)
pyautogui.write('treinando python ate ser um senior')

pyautogui.click(133,276,duration=5)
pyautogui.write('ter foco e objetivo')

pyautogui.click(135,286,duration=5)
pyautogui.write('ser determinado')


with open ("teste.python.txt",'r') as csvfile:
    for linha in csvfile:
        csvreader = csv.DictReader(csvfile)
        nome =  linha.split(',')[0]
        nome1 =  linha.split(',')[1]
        nome2 =  linha.split(',')[2]

#apertar para digitar nome     
pyautogui.click(113,304,duration=5)
pyautogui.write(nome)
#apertar no nome da pessoa 
pyautogui.click(125,321,duration=2)
pyautogui.write(nome1)
#apertar em forma de acesso
pyautogui.click(131,336,duration=2)
pyautogui.write(nome2)
sleep(2)