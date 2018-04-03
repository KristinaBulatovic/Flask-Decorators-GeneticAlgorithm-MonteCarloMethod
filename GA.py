import random
OPTIMAL = "Python is the best"
DNA_SIZE = len(OPTIMAL)
POP_SIZE = 20
GENERATIONS = 5000
ELITE_PERCENT=5
def weighted_choice(items):
    weight_total = sum((item[1] for item in items))
    n = random.uniform(0, weight_total)
    for item, weight in items:
        if n < weight:
            return item
        n = n - weight
    return item
def random_char(): return chr(int(random.randrange(32, 126, 1)))
def random_population(): # kreiranje populacije
    pop = []
    for i in range(POP_SIZE):
        dna = ""
        for c in range(DNA_SIZE):
            dna += random_char()
        pop.append(dna)
    return pop
def fitness(dna): # funcija dobrote (prilagodljivosti)
    fitness = 0
    for c in range(DNA_SIZE):
        fitness += abs(ord(dna[c]) - ord(OPTIMAL[c]))
    return fitness
def mutate(dna): # izbegavanje zarobljavanja u lokalnom "dobrom" resenju
    dna_out = ""
    mutation_chance = 100
    for c in range(DNA_SIZE):
        if int(random.random()*mutation_chance) == 1:
            dna_out += random_char()
        else:
            dna_out += dna[c]
    return dna_out
def crossover(dna1, dna2): # ukrstanje
    pos = int(random.random()*DNA_SIZE)
    return (dna1[:pos]+dna2[pos:], dna2[:pos]+dna1[pos:])
def population_sorted(items):
    new_items =[]
    for item in items:
        new_item=list(item)
        new_item[0],new_item[1]=new_item[1],new_item[0]
        new_item=tuple(new_item)
        new_items.append(new_item)
    new_items.sort(reverse=True)
    population_sorted=list(dict(new_items).values())
    return population_sorted

# generisanje inicijalne populacije (sekvanca slucajnih karaktera)
population = random_population()
# simulacija svih generacija
for generation in range(GENERATIONS):
    print ('Generacija {:06} > Najbolji hromozom: {}'.format(generation,population[0]))
    weighted_population = []
    for individual in population:
        fitness_val = fitness(individual)
        # generisanje para (individual,fitness),
        # pazeci da se izbegne deljenje sa nulom
        # sto je slucaj sa poklapanjem ciljnog niza karaktera.
        if fitness_val == 0:
            pair = (individual, 1.0)
        elif fitness_val==1:
            pair = (individual, 0.75)
        else:
            pair = (individual, 1.0/fitness_val)


        weighted_population.append(pair)

    population = []
    ELITE=int(POP_SIZE*ELITE_PERCENT/100)
    elite_population=population_sorted(weighted_population)
    for item in range(ELITE):
        population.append(elite_population[item])
    # selekcija dva hromozoma (roditelja) prema njigovom kvaliteteu,
    # ukrstanje u slucajnoj tacki (kreiranje 2 potomka), njihova
    # mutacija i dodavanje novoj generaciji
    for _ in range((POP_SIZE-ELITE) // 2):
        # Selection
        ind1 = weighted_choice(weighted_population)
        ind2 = weighted_choice(weighted_population)
        # Crossover
        ind1, ind2 = crossover(ind1, ind2)
        # Mutate and add back into the population.
        population.append(mutate(ind1))
        population.append(mutate(ind2))


# najbolji hromozom
fittest_string = population[0]
minimum_fitness = fitness(population[0])

for individual in population:
    ind_fitness = fitness(individual)
    if ind_fitness <= minimum_fitness:
        fittest_string = individual
        minimum_fitness = ind_fitness
print ("Fittest String: %s" % fittest_string)