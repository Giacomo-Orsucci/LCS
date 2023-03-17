import random
from timeit import default_timer as timer
import matplotlib.pyplot as plt
from LCS import *

def random_string_generator(length=2, minValue=0, maxValue=1):
    sequence = ""
    for i in range(length):
        sequence += str(random.randint(minValue, maxValue))
    return sequence


#sequence1 = "502233"
#lcs1 = LCS("502233")
#sequence2 = "0030351"

maxLength = 15
minLength = 1
step = 1
timeArrayBruteForce = []
timeArrayRecursive = []
timeArrayRecursiveMemo = []
timeArrayBottomUp = []
stepArray = []

for i in range(minLength,maxLength+1,step):
    sequence1 = random_string_generator(i,0,9)
    sequence2 = random_string_generator(i,0,9)

    print(sequence1)
    print(sequence2)

    stepArray.append(i)

    lcs1 = LCS(sequence1)

    start = timer()
    lcs1.brute_force(sequence2)
    end = timer()
    timeArrayBruteForce.append(end - start)

    start = timer()
    lcs1.recursive(sequence2)
    end = timer()
    timeArrayRecursive.append(end - start)

    start = timer()
    lcs1.recursive_memo(sequence2)
    end = timer()
    timeArrayRecursiveMemo.append(end - start)

    start = timer()
    lcs1.bottom_up(sequence2)
    end = timer()
    timeArrayBottomUp.append(end - start)

#print(stepArray[0])
#print(timeArrayBruteForce)

plt.plot(stepArray, timeArrayBruteForce)
plt.plot(stepArray, timeArrayRecursive)
plt.plot(stepArray, timeArrayRecursiveMemo)
plt.plot(stepArray, timeArrayBottomUp)
plt.xlabel("Sequences size")
plt.ylabel("Execution time (s)")
plt.title("Method Confrontation Graphic")
plt.legend(["Brute-Force", "Recursive", "Memoization Recursive", "Bottom-Up"])
plt.show()

#mettendo tutti i grafici a confronto, il brute force vieni troppo assottigliato. Vedi di fare quattro graficini bellini tutti a confronto, ma separati
plt.plot(stepArray, timeArrayBruteForce)
plt.plot(stepArray, timeArrayBruteForce)
plt.show()

"""
lcs1 = LCS(sequence1)

print(sequence1)
print(sequence2)


#alfa
#omega

#una sorta di pretest per capire se i metodi funzionino
lcs1.brute_force(sequence2)
print("Risultato con brute-force: ", lcs1.length)
print(lcs1.result)
print(lcs1.result)
lcs1.recursive(sequence2)
print("Risultato con ricorsione: ", lcs1.length)
lcs1.recursive_memo(sequence2)
print("Risultato con ricorsione con memoization: ", lcs1.length)
lcs1.bottom_up(sequence2)
print("Risultato con ricorsione con bottom-up: ", lcs1.length)

"""