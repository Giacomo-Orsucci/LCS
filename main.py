from LCS import *


lcs1 = LCS("quaderno")
sequence2 = "quadro"
#
#length = lcs1.recursive(sequence2, len(lcs1.sequence1)-1, len(sequence2)-1)
#print(length)
#print(lcs1.result)

length = lcs1.brute_force(sequence2)
print(lcs1.length)
print(lcs1.result)