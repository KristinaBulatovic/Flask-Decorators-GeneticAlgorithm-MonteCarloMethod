import time

def dekor(func):
    def nova():
        time_start = time.time()
        name = func.__name__
        rezultat = func()
        time_end = time.time()
        start_end = time_end - time_start
        return "Vreme ulaska: " + str(time_start) + ", <br> Naziv funkcije: " + str(name) + ", <br> Rezultat: "\
               + str(rezultat) + ", <br> Vreme izlaska: " + str(time_end) + \
               ", <br> Vreme provedeno u dekorativnoj funkciji: " + str(start_end)
    return nova

niz = []
@dekor
def fib():
    global niz
    # niz.append(1)
    # niz.append(1)
    #
    # for i in range(30):
    #     niz.append(niz[-1] + niz[-2])

    if(len(niz) < 2):
        niz.append(1)
        fib()
    if(len(niz) < 32):
        niz.append(niz[-1] + niz[-2])
        fib()

    return  niz

print(fib())

