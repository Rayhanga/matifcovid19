import tabula
import math
import json
import os
from tabulate import tabulate
import platform
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

OS = platform.system()
scriptDir = os.path.dirname(os.path.abspath(__file__))

def kasus(x, N, R, P):
    RP = float(R)*float(P)
    total = ((1+RP)**float(x))*float(N)
    return(math.floor(total))

def getTable(src):
    percobaan = []
    df = tabula.read_pdf(src, output_format="json", pages='all')
    rows = df[0]['data']
    for row in rows:
        data = row
        p = []
        for datum in data:
            p.append(datum['text'])

        percobaan.append(p)

    return percobaan

def completeTable(table):
    for row in table[1:]:
        for i, data in enumerate(row[1:]):
            if '?' in data:
                row[i+1] = calculateAnswer(i, row[1:])

def calculateAnswer(question, data):
    ans = 'None'
    if question == 5:
        ans = kasus(data[4], data[0], data[1], data[2])
    elif question == 3:
        ans = '1 + {}'.format(float(data[1])*float(data[2]))
    return '{}'.format(ans)

def createGraph(data):
    if OS == 'Windows':
        if not os.path.exists(scriptDir+'\Grafik'):
            os.makedirs(scriptDir+'\Grafik')
    else:
        if not os.path.exists(scriptDir+'/Grafik/'):
            os.makedirs(scriptDir+'/Grafik/')
        

    info = 'Percobaan Ke-{}'.format(data[0])
    filename = 'pcbk{}'.format(data[0])
    N = float(data[1])
    R = float(data[2])
    P = float(data[3])
    mx = int(data[5])

    x = []
    y = []
    for i in range(mx):
        y.append(kasus(i, N, R, P))
        x.append(i+1)

    fig, ax = plt.subplots()
    ax.plot(x, y)

    plt.xticks(x)

    ax.set(xlabel='Hari', ylabel='Jumlah Kasus',
       title=info)
    ax.grid()

    if OS == 'Windows':
        fig.savefig('Grafik\{}.png'.format(filename))
    else:
        fig.savefig('Grafik/{}.png'.format(filename))

table = getTable('source.pdf')
os.system('cls' if OS == 'Windows' else 'clear')
completeTable(table)

print(tabulate(table[1:], headers=table[0], tablefmt="github"))

for row in table[1:]:
    createGraph(row)