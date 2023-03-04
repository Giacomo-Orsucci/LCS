class LCS:

    def __init__(self, sequence1):
        self.sequence1 = sequence1
        self.result = ""
        self.length = 0

    def brute_force(self, sequence2): #wrong, to fix
        LCS_length = 0
        for i in range(len(self.sequence1)):
            j = i
            temp = ""
            temp_length = 0
            for j in range(len(self.sequence1)):
                found = False
                for k in range(len(sequence2)):
                    if self.sequence1[j] == sequence2[k] and found is False:
                        temp += sequence2[k]
                        temp_length += 1
                        found = True
            if temp_length > len(self.result):
                self.result = temp
                self.length = temp_length

        return LCS_length
    def recursive(self, sequence2, i, j):
        if i < 0 or j < 0:
            return 0
        if self.sequence1[i] == sequence2[j]:
            return 1+self.recursive(sequence2, i-1, j-1)

        else:
            return max(self.recursive(sequence2, i, j-1), self.recursive(sequence2, i-1, j))










