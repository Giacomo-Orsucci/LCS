class LCS:

    def __init__(self, sequence1):
        self.sequence1 = sequence1
        self.result = ""


    def brute_force(self, sequence2): #wrong, to fix
        for x in self.sequence1:
            for y in sequence2:
                if x == y:
                    self.result += x
            sequence2 = sequence2[1:]
        print(self.result)

    def recursive(self, sequence2, i, j):
        if i < 0 or j < 0:
            return 0
        if self.sequence1[i] == sequence2[j]:
            return 1+self.recursive(sequence2, i-1, j-1)
        else:
            return max(self.recursive(sequence2, i, j-1), self.recursive(sequence2, i-1, j))









