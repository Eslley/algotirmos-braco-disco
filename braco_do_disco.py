import fileinput

arquivo = []

for line in fileinput.input():
    arquivo.append(line.rstrip())

QTD_CILINDROSG = int(arquivo[0])
ATUAL_CILINDROG = int(arquivo[1])

arquivo = arquivo[2:len(arquivo)]

def fcfs():
    ATUAL_CILINDRO = ATUAL_CILINDROG
    soma = 0

    for linha in arquivo:
        cilindro = int(linha)
        soma += abs(cilindro - ATUAL_CILINDRO)
        ATUAL_CILINDRO = cilindro

    print("FCFS " + str(soma))


def sstf():
    ATUAL_CILINDRO = ATUAL_CILINDROG
    list = []
    distances = []
    soma = 0
    indexMin = -1    

    for linha in arquivo:
        list.append({'cilindro': int(linha), 'visitado': False})
        distances.append(0)

    for n in range(len(list)):
        minimum = 999999999
        for i in range(0, len(list)):
            distances[i] = abs(list[i]['cilindro'] - ATUAL_CILINDRO)
        
        for i in range(0, len(distances)):
            if(distances[i] < minimum and list[i]['visitado'] == False):
                indexMin = i
                minimum = distances[i]
        
        soma += distances[indexMin]

        ATUAL_CILINDRO = list[indexMin]['cilindro']

        list[indexMin]['visitado']= True
    

    print("SSTF " + str(soma))


def elevador():
    ATUAL_CILINDRO = ATUAL_CILINDROG
    soma = 0

    list = []
    maiores = []
    menores = []

    for linha in arquivo:
        list.append(int(linha))

    for i in list:
        if i < ATUAL_CILINDRO:
            menores.append(i)
        else:
            maiores.append(i)

    maiores.sort()
    menores.sort()
    menores.reverse()

    for i in maiores:
        soma += abs(i - ATUAL_CILINDRO)
        ATUAL_CILINDRO = i

    for i in menores:
        soma += abs(i - ATUAL_CILINDRO)
        ATUAL_CILINDRO = i

    print("ELEVADOR " + str(soma))

fcfs()

sstf()

elevador()