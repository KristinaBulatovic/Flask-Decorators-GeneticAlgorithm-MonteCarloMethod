from flask import Flask, render_template, request

import time

import matplotlib.pyplot as plt
import numpy as np
import random

app = Flask(__name__)
niz = []

@app.route('/')
def index():
    # app.logger.error('test')
    return render_template('index.html')


@app.route('/btn', methods=['POST'])
def btn():
    btn = request.form['lista']
    # app.logger.warn(btn)
    if(btn == "zad1"):
        return render_template('dec.html')
    elif(btn == "zad2"):
        return  render_template('povrsina.html')
    else:
        return render_template('ga.html')

@app.route('/dec',  methods=['POST'])
def dec():
    def dekor(func):
        def nova():
            time_start = time.time()
            name = func.__name__
            rezultat = func()
            time_end = time.time()
            start_end = time_end - time_start
            return "Vreme ulaska: " + str(time_start) + " <br> Naziv funkcije: " + str(name) + " <br> Rezultat: " \
                   + str(rezultat) + " <br> Vreme izlaska: " + str(time_end) + \
                   " <br> Vreme provedeno u dekorativnoj funkciji: " + str(start_end)

        return nova

    @dekor
    def fib():
        global niz

        if (len(niz) < 2):
            niz.append(1)
            fib()
        if (len(niz) < 32):
            niz.append(niz[-1] + niz[-2])
            fib()

        return niz

    return fib()

@app.route('/povrsina', methods=['POST'])
def povrsina():
    x = np.arange(0.0, 7.0, 1.0)
    y1 = []
    y2 = x

    for i in np.arange(0.0, 7.0, 1.0):
        y1.append((1 / 4 * (x - 4) ** 3) + 4)

    y1 = y1[0]

    plt.figure(1)
    plt.subplot(111)
    plt.plot(x, y1)

    plt.figure(1)
    plt.plot(x, y2)
    ax = plt.gca()
    plt.show()

    def f(n):
        pog1 = 0;
        pog2 = 0;
        for i in range(n):
            xrand1 = random.uniform(2, 4)
            yrand1 = random.uniform(2, 4)
            xrand2 = random.uniform(4, 6)
            yrand2 = random.uniform(4, 6)
            y1 = (1 / 4 * (xrand1 - 4) ** 3) + 4
            y2 = xrand1
            y3 = (1 / 4 * (xrand2 - 4) ** 3) + 4
            y4 = xrand2
            if (y1 > yrand1 > y2):
                pog1 += 1
            if (y4 > yrand2 > y3):
                pog2 += 1

        return str(((4 * pog1 / n) + (4 * pog2 / n)))

    return f(1000000)

@app.route('/ga',  methods=['POST'])
def ga():
    return "GA"

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5001)
