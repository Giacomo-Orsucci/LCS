class LCS:

    def __init__(self, sequence1):
        self.sequence1 = sequence1
        self.result = ""
        self.length = 0

    def brute_force(self, sequence2): #wrong, to fix
        if len(self.sequence1) <= len(sequence2):
            m = len(self.sequence1)
            n = len(sequence2)
        else:
            m = len(sequence2)
            n = len(self.sequence1)
        for i in range(m):
            j = i
            temp = ""
            temp_length = 0
            for j in range(m):
                found = False
                for k in range(n):
                    if len(self.sequence1) <= len(sequence2): #posso farlo in maniera più pulita?
                        if self.sequence1[j] == sequence2[k] and found is False:
                            temp += sequence2[k]
                            temp_length += 1
                            found = True
                    else:
                        if self.sequence1[k] == sequence2[j] and found is False:
                            temp += sequence2[k]
                            temp_length += 1
                            found = True
            if temp_length > len(self.result):
                self.result = temp
                self.length = temp_length

    def recursive(self, sequence2, i, j):
        if i < 0 or j < 0:
            return 0
        if self.sequence1[i] == sequence2[j]:
            return 1+self.recursive(sequence2, i-1, j-1)

        else:
            return max(self.recursive(sequence2, i, j-1), self.recursive(sequence2, i-1, j))

    def memoization(self, sequence2):
        m = len(self.sequence1)
        n = len(sequence2)
        b = [[0 for x in range(m)] for y in range(n)]
        c = [[0 for x in range(m+1)] for y in range(n+1)]

        for i in range(m):
            c[0][i] = 0
        for j in range(n):
            c[j][0] = 0
        for j in range(m):
            for i in range(n):
                if self.sequence1[j] == sequence2[i]:
                    c[i][j] = c[i-1][j-1]+1
                    b[i][j] = "\\"
                elif c[i-1][j] >= c[i][j-1]:
                    c[i][j] = c[i-1][j]
                    b[i][j] = "|"
                else:
                    c[i][j] = c[i][j-1]
                    b[i][j] = "-"
        self.length = c[n-1][m-1]











