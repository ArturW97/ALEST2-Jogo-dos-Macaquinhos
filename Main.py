import time

tempoInicio = time.time()
arquivo = 'caso1000.txt'
with open("casos/" + arquivo) as f:

    print("\nExecutando arquivo: " + arquivo)
    rodadasTotal = 0
    listaMacacos = []
    for palavra in f.readlines():
        # Extrair dados do texto
        palavra = palavra.split(" ")
        if ('Macaco' in palavra):
            direcaoPar = palavra[4]
            direcaoImpar = palavra[7]
            numCocos = int(palavra[9])
            numCocosPar = 0
            for i in range(11, numCocos + 11):
                numero = int(palavra[i])
                if numero % 2 == 0:
                    numCocosPar = numCocosPar + 1
            listaMacacos.append(
                [direcaoPar, direcaoImpar, numCocosPar, numCocos - numCocosPar])
        # Pegar o número de rodadasTotal
        elif rodadasTotal == 0:
            rodadasTotal = int(palavra[1])

    # Laços responsáveis pelas rodadas
    for i in range(0, rodadasTotal):
        for j in range(0, len(listaMacacos)):
            # Transferência de cocos pares do remetente para o destinatário
            if listaMacacos[j][2] != 0:
                direcaoPar = int(listaMacacos[j][0])
                listaMacacos[direcaoPar][2] += listaMacacos[j][2]
                listaMacacos[j][2] = 0
            # Transferência de cocos ímpares do remetente para o destinatário
            if listaMacacos[j][3] != 0:
                direcaoImpar = int(listaMacacos[j][1])
                listaMacacos[direcaoImpar][3] += listaMacacos[j][3]
                listaMacacos[j][3] = 0

    numCampeao = 0
    qtdCampeao = 0
    for i in range(0, len(listaMacacos)):
        if listaMacacos[i][2] + listaMacacos[i][3] > qtdCampeao:
            qtdCampeao = listaMacacos[i][2] + listaMacacos[i][3]
            numCampeao = i
    print("O macaco campeão é o de número " + str(numCampeao) + "! " + "Com um total de " + str(qtdCampeao) + " cocos!")

    segundos = (time.time() - tempoInicio)
    print(str(int(segundos / 60)) + " minutos e " + str(segundos % 60) + " segundos.")
