from LCS import *


#lcs1 = LCS("quaderno")
#sequence2 = "quadro"

lcs1 = LCS("10010110")
sequence2 = "1001011000123"


#alfa
#omega

#una sorta di pretest per capire se i metodi funzionino
lcs1.brute_force(sequence2)
print("Risultato con brute-force: ", lcs1.length)
lcs1.recursive(sequence2)
print("Risultato con ricorsione: ", lcs1.length)
lcs1.recursive_memo(sequence2)
print("Risultato con ricorsione con memoization: ", lcs1.length)
lcs1.bottom_up(sequence2)
print("Risultato con ricorsione con bottom-up: ", lcs1.length)
