from LCS import *


#lcs1 = LCS("quaderno")
#sequence2 = "quadro"

lcs1 = LCS("1000100123")
sequence2 = "10001"


#alfa
#omega
#
#length = lcs1.recursive(sequence2, len(lcs1.sequence1)-1, len(sequence2)-1)

#print(length)

#lcs1.brute_force(sequence2)
lcs1.memoization(sequence2)
print(lcs1.length)
#print(lcs1.length)
#print(lcs1.result)