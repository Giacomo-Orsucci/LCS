
class LCS:

    def __init__(self, sequence1):
        self.sequence1 = sequence1
        self.length = 0

    def brute_force(self, sequence2):
        """per garantire la correttezza della funzione è necessario che
           il primo for cicli sulla sequenza di input più breve
        """
        if len(self.sequence1) <= len(sequence2):
            m = len(self.sequence1)
            n = len(sequence2)
        else:
            m = len(sequence2)
            n = len(self.sequence1)
            app = self.sequence1
            self.sequence1 = sequence2
            sequence2 = app

        # ciclo esterno per garantire che ogni carattere della stringa più breve venga confrontato con la stringa più lunga
        for i in range(m):
            j = i
            temp = ""
            temp_length = 0
            # confronto i caratteri successivi a quello preso in esame (e lui stesso compreso) per esaminare tutte le possibili CS
            for j in range(m):
                found = False
                for k in range(n):
                    # se il carattere è presente nella stringa più lunga
                    if self.sequence1[j] == sequence2[k] and found is False:
                        temp += sequence2[k]
                        temp_length += 1
                        found = True
            # alla fine avrò trovato la lunghezza della LCS
            if temp_length > self.length:
                self.length = temp_length

    def recursive(self, sequence2, i, j):  # dalla definizione ricorsiva del problema della LCS
        if i < 0 or j < 0: # condizione di uscita dalla ricorsione; caso base
            return 0
        if self.sequence1[i] == sequence2[j]:
            return 1+self.recursive(sequence2, i-1, j-1)

        else:
            return max(self.recursive(sequence2, i, j-1), self.recursive(sequence2, i-1, j))

    def recursive_memo(self, sequence2):
        m = len(self.sequence1)
        n = len(sequence2)

        c = [[0 for x in range(m + 1)] for y in range(n + 1)]  # matrice per la memorizzazione dei risultati già calcolati
        self.length = self.__recursive_memo_aux(sequence2, c, m-1, n-1)

    def __recursive_memo_aux(self, sequence2, c, i, j):
        if c[j][i] != 0:  # se il risultato è già stato calcolato, ritorno il valore ritrovato
            return c[j][i]

        elif i < 0 or j < 0:  # condizione di uscita dalla ricorsione; caso base
            return 0
        # quanto segue è identico alla soluzione ricorsiva
        elif self.sequence1[i] == sequence2[j]:
            return 1+self.recursive(sequence2, i-1, j-1)

        else:
            return max(self.recursive(sequence2, i, j-1), self.recursive(sequence2, i-1, j))

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











