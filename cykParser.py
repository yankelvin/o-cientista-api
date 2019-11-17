from re import findall
from math import floor, ceil


class CykParser:
    def __init__(self, word, grammar):
        self.word = list(word)
        self.grammar = grammar
        self.matrix = [list() for i in range(len(word))]

    def filling_matrix(self, row=0):
        base = self.matrix[len(self.matrix) - 1]
        if (len(base) != 0):
            return self.matrix

        combinations = self.generate_combinations(self.word, row)
        if len(combinations[0]) > 2:
            for i, comb in enumerate(combinations):
                combinations[i] = []
                for j in range(len(comb) - 1):
                    combinations[i].append([comb[:j+1], comb[j+1:]])

        for comb in combinations:
            if type(comb[0]) is list:
                calc = list()
                result = ''
                for j in comb:
                    verif = []
                    for k in j:
                        if len(k) > 1:
                            w = ''.join(self.word)
                            concat = ''.join(k)
                            position = w.find(concat)
                            no_termminal = self.matrix[len(concat)-1][position]
                            verif.append(no_termminal)
                        else:
                            no_termminal = self.verify_production(
                                k, self.grammar)
                            verif.append(no_termminal)
                    verif = self.distribuction(verif[0], verif[1])
                    result = self.verify_production(verif, self.grammar)
                    calc.append(result)
                    result = ''
                found = ''
                for c in calc:
                    found += c
                self.matrix[row].append(found)
            else:
                verif = ''
                no_termminal = self.verify_production(comb, self.grammar)
                if len(no_termminal) > 1:
                    verif = self.distribuction(no_termminal[:ceil(
                        len(no_termminal)/2)], no_termminal[ceil(len(no_termminal)/2):])
                    verif = list(dict.fromkeys(verif))
                    result = self.verify_production(verif, self.grammar)
                    if result == '':
                        result = no_termminal
                    self.matrix[row].append(result)
                else:
                    self.matrix[row].append(no_termminal)

        row += 1
        return self.filling_matrix(row)

    def verify_production(self, w, grammar):
        prod = ''
        if (type(w) is list):
            for i in w:
                prod += self.verify_production(i, grammar)
        else:
            for key, values in grammar.items():
                if w in values:
                    prod += key
        return prod

    def generate_combinations(self, w, row):
        step = row + 1
        combinations = []
        for i in range(len(w)):
            symbol = []
            try:
                if (row > 0):
                    for j in range(i, step + i):
                        symbol.append(w[j])
                    combinations.append(symbol)
                else:
                    combinations.append(w[i:step][0])
                    step += 1
            except:
                pass
        return combinations

    def distribuction(self, ve, node):
        dist = []
        for i in ve:
            for n in node:
                dist.append(f'{i}{n}')
        return dist
