from LCS import *


lcs1 = LCS("cantiere")
sequence2 = "armiere"

length = lcs1.recursive(sequence2, len(lcs1.sequence1)-1, len(sequence2)-1)
print(length)
