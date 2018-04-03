import math
import random
POP_SIZE = 50
ELIMINATION_PERCENT=50
ELIMINATION_NUMBER=int(ELIMINATION_PERCENT*POP_SIZE/100)
SURVIVERS=POP_SIZE-ELIMINATION_NUMBER
DNA_SIZE = 32
MUTATIONS_PERCENT=20
MUTATIONS_NUMBER=int(MUTATIONS_PERCENT*POP_SIZE/100)
N=2**DNA_SIZE-1
GENERATIONS = 1000
BB=1.0    #DONJA GRANICA ISPITIVANJA FUNKCIJE
TB=2.0     #GORNJA GRANICA ISPITIVANJA FUNKCIJE


#traži se globalni maksimum zadate funkcije
#F(X)=SIN(10*PI*X**2)/X  FMAX(0.19262)=4.771199
def f(x):
    return x**2*math.sin(10*math.pi*x**2)

def bintoint(word): #string od nula i jedinica u integer
    word=word[::-1]
    b=0;weight=0
    for bit in word:
        b+=int(bit)*2**weight
        weight+=1
    return b

def inttofloat(b): #celi broj u float
    return BB+b*(TB-BB)/N

def bintofloat(word): #binarni string u float
    return inttofloat(bintoint(word))

def floattoint(x):
    return int((x-BB)*N/(TB-BB))

def inttobin(b):
    bstr=bin(b)[2:]
    dna="0"*(DNA_SIZE -len(bstr))+bstr
    return dna

def random_item():  #kreiranje jednog hromozoma
    binranstr = bin(int(random.randrange(0,N+1,1)))[2:]
    dna = "0" * (DNA_SIZE - len(binranstr)) + binranstr
    return dna

def random_population(): # kreiranje populacije hromozoma
    pop = []
    for i in range(POP_SIZE):
        pop.append(random_item())
    return pop

def fitness(pop): #definisanje dobrote  i kazne cele populacije
    quality=[]
    for word in pop:
        x=bintofloat(word)
        quality.append(f(x))
    dmin=min(quality)
    for i in range(len(quality)):
        quality[i]-=dmin
    dmax=max(quality)
    penals=[]
    for i in range(len(quality)):
        penals.append(dmax-quality[i])
    return quality, penals

def cumulative_quality(pop):
    s = []
    for i in range(len(pop)):
        s.append(sum(item[0] for item in pop[:i]))
    return s

def elimination(pop):
    for j in range(ELIMINATION_NUMBER):
        s=cumulative_quality(pop)
        n = random.uniform(0, s[len(pop)-1])
        for i in range(len(pop)):
            if n<s[i] and pop[i][0]:
                del pop[i]
                break
    return pop

def crossover(dna1, dna2): # ukrstanje

    pos = int(random.random()*DNA_SIZE)
    return (dna1[:pos]+dna2[pos:])

    # pos = []
    # for i in range(3):
    #     pos.append(int(random.random()*DNA_SIZE))
    # pos.sort()
    # return (dna1[:pos[0]] + dna2[pos[0]:pos[1]] + dna1[pos[1]:pos[2]] + dna[pos[2]:])


#ako je  kazna 0, nema mutacije, vraca se isti hromozom.
#ako nije, kreira se maska koja ima 1 do 3 bita jednaka 1 slučajno rasporedjena
#operacijom XOR menja se vrednost bita u originalnom hromozomu na tim mestima
def mutation(pair):
    if pair[0]:
        gene_num=random.randrange(1,4,1)
        mask=0
        for i in range(gene_num):
            mask+=2**random.randrange(0,DNA_SIZE,1)
        muted_int=bintoint(pair[1])^mask
        return inttobin(muted_int)
    else:
        return pair[1]

def evaluation_pairs(population):
    quality, penals = fitness(population)  # racuna dobrotu i kazne za sve hromozome
    eval_population = []
    for i in range(POP_SIZE): #generisanje parova kazna, hromozom
        pair=(penals[i], population[i] )
        eval_population.append(pair)
    return eval_population






#POCETAK*******************************************************************************
population=random_population()

for k in range(GENERATIONS):

    eval_population=evaluation_pairs(population) #kreiranje parova kazna, hromozom
    for penal, hromosome in eval_population: #trazenje najboljeg para-kazna=0
        if penal:
            continue
        else:
            best=hromosome
            break
    x=bintofloat(best)

    print(k, best, x , f(x) ) #stampanje najboljeg u svakoj iteraciji

    eval_population=elimination(eval_population)  #eliminacija losih


#kreiranje nove populacije
    population=[]
    for penal, dna in eval_population: #oni koji nisu eliminisani, ulaze u novu generaciju
        population.append(dna)
    for i in range(ELIMINATION_NUMBER): #oni koji su eliminisani nadomešćuju se ukrštanjem preostalih
        i1=int(random.randrange(0, ELIMINATION_NUMBER, 1))
        i2=int(random.randrange(0, ELIMINATION_NUMBER, 1))
        parent1 = eval_population[i1]
        parent2 = eval_population[i2]
        if parent1!=parent2:
            child=crossover(parent1[1],parent2[1])
            population.append(child)
        else:
            child=random_item()
            population.append(child)
            if parent2[0]:
                mparent=mutation(parent2)
                del population[i2]
                del eval_population[i2]
                population.append(mparent)
                eval_population.append((0.,mparent))


    eval_population = evaluation_pairs(population)

    for i in range(MUTATIONS_NUMBER):
        index=random.randrange(0, POP_SIZE,1)
        population[index]=mutation(eval_population[index])














