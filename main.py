import random
from timeit import default_timer as timer
import matplotlib.pyplot as plt
from LCS import *
import datetime

def random_string_generator(length=2, min_value=0, max_value=1): # metodo per la generazione casuale delle sequenze da testare
    sequence = ""
    for i in range(length):
        sequence += str(random.randint(min_value, max_value))
    return sequence


maxLength = 12
minLength = 1
step = 1
timeArrayBruteForce = []
timeArrayRecursive = []
timeArrayRecursiveMemo = []
timeArrayBottomUp = []
stepArray = []

for i in range(minLength, maxLength+1, step):
    sequence1 = random_string_generator(i, 0, 9) # sequenza X generata casualmente
    sequence2 = random_string_generator(i, 0, 9) # sequenza Y generata casualmente

    stepArray.append(i) # array con la dimensione delle sequenze per le ascisse dei grafici

    lcs1 = LCS(sequence1) # creazione dell'oggetto LCS a cui verrà passata X come attributo e Y come parametro di volta in volta

    # misurazioni sull'algoritmo brute force
    start = timer()
    lcs1.brute_force(sequence2)
    end = timer()
    timeArrayBruteForce.append(end - start)

    # misurazioni sull'algoritmo puramente ricorsivo
    start = timer()
    lcs1.recursive(sequence2)
    end = timer()
    timeArrayRecursive.append(end - start)

    # misurazioni sull'algoritmo ricorsivo con memoization
    start = timer()
    lcs1.recursive_memo(sequence2)
    end = timer()
    timeArrayRecursiveMemo.append(end - start)

    # misurazioni sull'algoritmo bottom-up
    start = timer()
    lcs1.bottom_up(sequence2)
    end = timer()
    timeArrayBottomUp.append(end - start)

# si plottano 4 grafici per confrontare i metodi
figure, axis = plt.subplots(2, 2)

figure.suptitle("Method perfomance comparison")

axis[0, 0].plot(stepArray, timeArrayBruteForce)
axis[0, 0].set_title("Brute-Force")

axis[0, 1].plot(stepArray, timeArrayRecursive)
axis[0, 1].set_title("Recursive")

axis[1, 0].plot(stepArray, timeArrayRecursiveMemo)
axis[1, 0].set_title("Recursive with Memoization")

axis[1, 1].plot(stepArray, timeArrayBottomUp)
axis[1, 1].set_title("Bottom-Up")

for ax in axis.flat:
    ax.set(xlabel='sequence size', ylabel='execution time')

plt.tight_layout()
plt.show()
