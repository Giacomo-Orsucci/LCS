from LCS import *


#lcs1 = LCS("quaderno")
#sequence2 = "quadro"

lcs1 = LCS("10010110")
sequence2 = "1001011000123"


#alfa
#omega
#
#length = lcs1.recursive(sequence2, len(lcs1.sequence1)-1, len(sequence2)-1)

#print(length)

lcs1.brute_force(sequence2)
#lcs1.bottom_up(sequence2)
#lcs1.recursive_memo(sequence2)
print(lcs1.length)
#print(lcs1.length)
#print(lcs1.result)