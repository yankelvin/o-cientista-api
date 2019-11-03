from re import findall

grammar = dict()

# Getting productions from the file
with open('gramatica.txt', 'r') as file:
    for row in file.readlines():
        left = findall(r'[a-zA-Z]+\s\=\>', row)[0]
        key = left.replace('=>', '').strip()
        productions = row.replace(left, '').strip().split('|')
        grammar[key] = productions


word = 'abaab'

# Creating the matrix
matrix = [list() for i in range(len(word))]
word = list(word)


# Filling the matrix
def filling_matrix(word, grammar, matrix, row):
    base = matrix[len(matrix) - 1]
    if (len(base) != 0):
        return matrix

    combinations = generate_combinations(word, row)

    for comb in combinations:
        no_termminal = verify_production(comb, grammar)
        if len(no_termminal) > 1:
            prods = verify_production(no_termminal, grammar)
            matrix[row].append(prods)
        else:
            matrix[row].append(no_termminal)

    row += 1
    return filling_matrix(word, grammar, matrix, row)


def verify_production(w, grammar):
    prod = ''
    if (type(w) is list):
        for i in w:
            prod += verify_production(i, grammar)
    else:
        for key, values in grammar.items():
            if w in values:
                prod += key
    return prod


def generate_combinations(w, row):
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


result = filling_matrix(word, grammar, matrix, 0)
print(result)
