from itertools import combinations
class LCS:

    def __init__(self, sequence1):
        self.sequence1 = sequence1
        self.length = 0
        self.result = ""

    def all_subsequences(self, s): #metodo per generare tutte le possibili sottosequenze di una sequenza s
        out = set()
        for r in range(1, len(s) + 1):
            for c in combinations(s, r):
                out.add(''.join(c))
        return sorted(out)

    def brute_force(self, sequence2):
        # si creano tutte le possibili sottosequenze della prima stringa
        substrings = self.all_subsequences(self.sequence1)
        self.length = 0

        for i in range(len(substrings)): # si cicla per ogni sottosequenza generata
            substring = substrings[i]
            last_index = -1
            temp_length = 0
            temp_sub = ""

            for j in range(len(substring)):
                found = False
                for k in range(len(sequence2)): # confronto ogni carattere di ogni sottosequenza con i caratteri della seconda stringa
                    # se i caratteri sono uguali e il carattere è successivo all'ultimo risultato essere uguale
                    if substring[j] == sequence2[k] and last_index < k and found == False:
                        temp_length += 1
                        last_index = k
                        temp_sub += substring[j]
                        found = True
            if temp_length > self.length: # alla fine sarà contenuta la lunghezza della LCS
                self.length = temp_length
                self.result = temp_sub
    def recursive(self, sequence2):
        m = len(self.sequence1)-1
        n = len(sequence2)-1
        self.length = self.__recursive_aux(sequence2, m, n)

    def __recursive_aux(self, sequence2, i, j):  # dalla definizione ricorsiva del problema della LCS
        if i < 0 or j < 0: # condizione di uscita dalla ricorsione; caso base
            return 0
        if self.sequence1[i] == sequence2[j]:
            return 1+self.__recursive_aux(sequence2, i-1, j-1)

        else:
            return max(self.__recursive_aux(sequence2, i, j-1), self.__recursive_aux(sequence2, i-1, j))

    def recursive_memo(self, sequence2):
        m = len(self.sequence1)
        n = len(sequence2)

        c = [[0 for x in range(m+1)] for y in range(n+1)]  # matrice per la memorizzazione dei risultati già calcolati
        self.length = self.__recursive_memo_aux(sequence2, c, m, n)

    def __recursive_memo_aux(self, sequence2, c, i, j):
        if c[j][i] != 0:  # se il risultato è già stato calcolato, ritorno il valore ritrovato
            return c[j][i]

        elif i <= 0 or j <= 0:  # condizione di uscita dalla ricorsione; caso base
            return 0
        # quanto segue è identico alla soluzione ricorsiva
        elif self.sequence1[i-1] == sequence2[j-1]:
            c[j][i] = 1+self.__recursive_memo_aux(sequence2, c, i-1, j-1)
            return c[j][i]

        else:
            c[j][i] = max(self.__recursive_memo_aux(sequence2, c, i, j-1), self.__recursive_memo_aux(sequence2, c, i-1, j))
            return c[j][i]

    def bottom_up(self, sequence2):
        m = len(self.sequence1)
        n = len(sequence2)
        c = [[0 for x in range(m+1)] for y in range(n+1)]  # matrice per la memorizzazione dei risultati già calcolati

        # le stringhe vuote avranno LCS nulla
        for i in range(1, m+1):
            c[0][i] = 0
        for j in range(1, n+1):
            c[j][0] = 0

        """ si calcola la LCS partendo dai primi caratteri (approccio bottom-up) 
            ed usando una matrice c che contiene le lunghezze delle CS 
            calcolate passo dopo passo
        """
        for i in range(1, m+1):
            for j in range(1, n+1):
                if self.sequence1[i-1] == sequence2[j-1]:
                    c[j][i] = c[j-1][i-1]+1
                elif c[j-1][i] >= c[j][i-1]:
                    c[j][i] = c[j-1][i]
                else:
                    c[j][i] = c[j][i-1]
        self.length = c[n][m]











