import matplotlib.pyplot as plt
import random
import time
import pandas as pd
import colorama
import os
import sys
import requests
import platform
import math
from bs4 import BeautifulSoup as soup
from colorama import Fore
import numpy as np
wi="\033[1;37m" #>>White#
rd="\033[1;31m" #>Red   #
gr="\033[1;32m" #>Green #
yl="\033[1;33m" #>Yellow#
#data = {
  #"calories": [420, 380, 390],
  #"duration": [50, 40, 45]
#}
#load data into a DataFrame object:
#df = pd.DataFrame(data)
#print(df)

#
#Country = ['USA','Canada','Germany','UK','France']
#GDP_Per_Capita = [45000,42000,52000,49000,47000]

#plt.bar(Country, GDP_Per_Capita)
#plt.title('Country Vs GDP Per Capita')
#plt.xlabel('Country')
#plt.ylabel('GDP Per Capita')
#plt.show()
sys = platform.system()
def banner():
    print(Fore.CYAN + '''
  ███████████                      █████                           █████   
░░███░░░░░███                    ░░███                           ░░███    
 ░███    ░███ █████ ████  ██████  ░███████    ██████   ████████  ███████  
 ░██████████ ░░███ ░███  ███░░███ ░███░░███  ░░░░░███ ░░███░░███░░░███░   
 ░███░░░░░░   ░███ ░███ ░███ ░░░  ░███ ░███   ███████  ░███ ░░░   ░███    
 ░███         ░███ ░███ ░███  ███ ░███ ░███  ███░░███  ░███       ░███ ███
 █████        ░░███████ ░░██████  ████ █████░░████████ █████      ░░█████ 
░░░░░          ░░░░░███  ░░░░░░  ░░░░ ░░░░░  ░░░░░░░░ ░░░░░        ░░░░░  
               ███ ░███                                                                               
    ''')

def random():
  print(wi + yl + 'Bar=0, Line=1, scatter=2, pie=3')
  commandhere = input("Choose Graph Type: ")
  if commandhere == "0":
    print('')

def update():
  url = 'https://github.com/FonderElite/chartgen'
  r = requests.get(url)
  soupi = soup(r.content, "html.parser")
  # font = soup.find("b", text="Past Movies:").find_next_sibling("font")
  dte = soupi.find(text="19 hours ago")
  print("Checking last commit date...")
  time.sleep(2)
  if dte != "19 hours ago":
    print("New Commit! kindly check:https://github.com/FonderElite/chartgen")
  else:
    print(rd + "No recent commits.")


def help():
  print(yl + '''
=============================================
+|      Chart-Gen    By  Fonder-Elite      |+
+|-----------------------------------------|+
+|      -h          Help                   |+
+|      -c          chart                  |+
+|      -r          random                 |+
+|      -s          Start                  |+
+|      -u          Update                 |+
+|      -q          Quit                   |+
+|Ex.  ./chartgen  -c -s (Generate Chart)  |+
+|Ex.  ./chartgen -c -r -s (Random Chart)  |+
+|=========================================|+
      ''')
banner()
time.sleep(2)
help()
try:
  import matplotlib
  import bs4
  import requests
  import colorama

except Exception:
    print(Fore.CYAN + "Missing Modules.")
    os.system('pip install matplotlib')
def chartgen():
  graphs = ["bar","line","scatter","pie"]
  print('Bar=0, Line=1, scatter=2, pie=3')
  datatype = input("Choose Graph Type: ")
  if datatype == "0":
    title = input("Title Of Graph: ")
    letters = input('Input 4 Titles: ')
    letters2 = input("Input 3 More Titles:")
    letters3 = input("Input 2 More Titles:")
    letters4 = input("Input 1 More Title:")
    numbers = input("Input 4 Values: ")
    numbers2 = input("Input 3 More Values: ")
    numbers3 = input("Input 2 More Values: ")
    numbers4 = input("Input 1 More Values: ")
    arr = [letters,letters2,letters3,letters4]
    numbersarr = [numbers,numbers2,numbers3,numbers4]
    plt.bar(arr, numbersarr)
    plt.title(title)
    plt.xlabel(arr)
    plt.ylabel(numbers)
    plt.show()
  elif datatype == "1":
    title = input("Title Of Graph: ")
    letters = input('Input 4 Titles: ')
    letters2 = input("Input 3 More Titles:")
    letters3 = input("Input 2 More Titles:")
    letters4 = input("Input 1 More Title:")
    numbers = input("Input 4 Values: ")
    numbers2 = input("Input 3 More Values: ")
    numbers3 = input("Input 2 More Values: ")
    numbers4 = input("Input 1 More Values: ")
    arr = [letters, letters2, letters3, letters4]
    numbersarr = [numbers, numbers2, numbers3, numbers4]
    fig, ax = plt.subplots()
    ax.plot(arr, numbersarr)
    ax.set(xlabel=arr, ylabel=numbersarr,
           title=title)
    ax.grid()
    plt.show()
  elif datatype == "2":
    title = input("Title Of Graph: ")
    letters = input('Input 4 Titles: ')
    letters2 = input("Input 3 More Titles:")
    letters3 = input("Input 2 More Titles:")
    letters4 = input("Input 1 More Title:")
    numbers = input("Input 4 Values: ")
    numbers2 = input("Input 3 More Values: ")
    numbers3 = input("Input 2 More Values: ")
    numbers4 = input("Input 1 More Values: ")
    arr = [letters, letters2, letters3, letters4]
    numbersarr = [numbers, numbers2, numbers3, numbers4]
    x = np.arange(0, math.pi * 2, 0.05)
    y = np.sin(x)
    plt.scatter(arr,numbersarr)
    plt.xlabel(arr)
    plt.ylabel(numbersarr)
    plt.title(title)
    plt.show()
  elif datatype == "3":
    title = input("Title Of Graph: ")
    letters = input('Input 4 Titles: ')
    letters2 = input("Input 3 More Titles:")
    letters3 = input("Input 2 More Titles:")
    letters4 = input("Input 1 More Title:")
    numbers = input("Input 4 Values: ")
    numbers2 = input("Input 3 More Values: ")
    numbers3 = input("Input 2 More Values: ")
    numbers4 = input("Input 1 More Values: ")
    arr = [letters, letters2, letters3, letters4]
    numbersarr = [numbers, numbers2, numbers3, numbers4]
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('equal')
    langs = ['C', 'C++', 'Java', 'Python', 'PHP']
    students = [23, 17, 35, 29, 12]
    ax.pie(numbersarr, labels=arr, autopct='%1.2f%%')
    plt.title(title)
    plt.show()

    plt.show()
while True:
  command = input(wi + sys + '-User: ')
  if command == './chartgen':
    help()
  elif command == "./chartgen -h":
    help()
  elif command == "./chartgen -u":
    update()
  elif command == "./chartgen -c -s":
    chartgen()
  elif command == "./chartgen -c -r -s":
    random()
  else:
    print(Fore.RED + '''
            ___  __   __   __    __           
           |__  |__) |__) /  \ |__)      
           |___ |  \ |  \ \__/ |  \      ''')
  print(Fore.BLUE + '''
                      __n__n__
               .------`-/00/-'
              /  ##  ## (oo)   Woops.
             / \## __   ./
                |//YY \|/
                |||   |||   \|/
                          ''')

