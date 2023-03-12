import random

from LCS import *

def random_string_generator(length, minValue=0, maxValue=1):
    sequence = ""
    for i in range(length):
        sequence += str(random.randint(minValue, maxValue))
    return sequence

#sequence1 = "502233"
#lcs1 = LCS("502233")
#sequence2 = "0030351"

sequence1 = random_string_generator(15,0,8)
sequence2 = random_string_generator(10,0,8)

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

