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
    print(wi + rd + "Tool that can generate charts, using the module matplotlib")

def random():
  print(wi + yl + 'Bar=0, Line=1, scatter=2, pie=3')
  commandhere = input("Choose Graph Type: ")
  if commandhere == "1":
    title = input("Title Of Graph: ")
    label1 = input("Input 2 Titles: ")
    label2 = input("Input 1 More Title: ")
    plt.style.use('dark_background')
    fig, ax = plt.subplots()
    L = 6
    x = np.linspace(0, L)
    ncolors = len(plt.rcParams['axes.prop_cycle'])
    shift = np.linspace(0, L, ncolors, endpoint=False)
    for s in shift:
      ax.plot(x, np.sin(x + s), 'o-')
    ax.set_xlabel(label1)
    ax.set_ylabel(label2)
    ax.set_title(title)

    plt.show()
  elif commandhere == "0":
    title1 = input("Input Title For stepfilled Graph: ")
    title2 = input("Input Title For step Graph: ")
    title3 = input("Input Title For barstacked Graph: ")
    title4 = input("Input Title For unequal bins Graph: ")
    np.random.seed(19680801)

    mu_x = 200
    sigma_x = 25
    x = np.random.normal(mu_x, sigma_x, size=100)

    mu_w = 200
    sigma_w = 10
    w = np.random.normal(mu_w, sigma_w, size=100)

    fig, axs = plt.subplots(nrows=2, ncols=2)

    axs[0, 0].hist(x, 20, density=True, histtype='stepfilled', facecolor='g',
                   alpha=0.75)
    axs[0, 0].set_title(title1)

    axs[0, 1].hist(x, 20, density=True, histtype='step', facecolor='g',
                   alpha=0.75)
    axs[0, 1].set_title(title2)

    axs[1, 0].hist(x, density=True, histtype='barstacked', rwidth=0.8)
    axs[1, 0].hist(w, density=True, histtype='barstacked', rwidth=0.8)
    axs[1, 0].set_title(title3)

    # Create a histogram by providing the bin edges (unequally spaced).
    bins = [100, 150, 180, 195, 205, 220, 250, 300]
    axs[1, 1].hist(x, bins, density=True, histtype='bar', rwidth=0.8)
    axs[1, 1].set_title(title4)

    fig.tight_layout()
    plt.show()
  elif commandhere == "2":
    np.random.seed(19680801)
    fig, ax = plt.subplots()
    for color in ['tab:blue', 'tab:orange', 'tab:green']:
      n = 750
      x, y = np.random.rand(2, n)
      scale = 200.0 * np.random.rand(n)
      ax.scatter(x, y, c=color, s=scale, label=color,
                 alpha=0.3, edgecolors='none')

    ax.legend()
    ax.grid(True)

    plt.show()
  elif commandhere == "3":
    fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

    recipe = ["225 g flour",
              "90 g sugar",
              "1 egg",
              "60 g butter",
              "100 ml milk",
              "1/2 package of yeast"]

    data = [225, 90, 50, 60, 100, 5]

    wedges, texts = ax.pie(data, wedgeprops=dict(width=0.5), startangle=-40)

    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
    kw = dict(arrowprops=dict(arrowstyle="-"),
              bbox=bbox_props, zorder=0, va="center")

    for i, p in enumerate(wedges):
      ang = (p.theta2 - p.theta1) / 2. + p.theta1
      y = np.sin(np.deg2rad(ang))
      x = np.cos(np.deg2rad(ang))
      horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
      connectionstyle = "angle,angleA=0,angleB={}".format(ang)
      kw["arrowprops"].update({"connectionstyle": connectionstyle})
      ax.annotate(recipe[i], xy=(x, y), xytext=(1.35 * np.sign(x), 1.4 * y),
                  horizontalalignment=horizontalalignment, **kw)

    ax.set_title("Matplotlib bakery: A donut")

    plt.show()
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

