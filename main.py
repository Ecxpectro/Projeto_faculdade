# Vetores
defunto = []
cova = []
flores = []
# Contador
i = 0
d = 0
c = 0
count = 0
# váriável pra indicar a leitura de dados
numDados = int(
    input('Informe a quantidade de dados a ser inserido no banco de dados: '))
# Estrutura para receber os dados e adicionar nas listas
while i < numDados:
    cova.append(i)
    nome = input(
        f'Informe o nome do defunto que será adicionado a cova {i}: ')
    defunto.append(nome)
    flor = input('Informe se a cova terá flores com sim/não: ')
    flores.append(f'{nome}, {flor} terá flores.')
    i += 1
print()
# informando se deseja alterar dados
print('Deseja realizar a alteração de dados?')
alteracaoDados = input('Se deseja alterar digite : S/N ')
# estrutura de repetição para alterar dados até o usuário pedir para parar
while 'S' or alteracaoDados == 'N' or alteracaoDados == 's' or alteracaoDados == 'n':
    # estrutura para não receber respostas diferentes de 'S' ou 'N'
    if alteracaoDados == 'S' or alteracaoDados == 's':
        # alteração dos dados fornecidos
        nomeD = input(
            'Informe o nome do defunto que deseja fazer a alteração de dados: ')
        if nomeD in list(defunto):
            while count < (numDados - d):
                if nomeD == defunto[count-1]:
                    altDadoCova = input(
                        'Deseja remover defunto da cova? S/N ')
                    if altDadoCova == 'S' or altDadoCova == 's':
                        del defunto[count - 1]
                        del cova[count - 1]
                        del flores[count - 1]
                        d += 1

                    else:
                        adicFlores = input(
                            'Deseja adicionar ou remover flores? Adicionar/Remover ')
                        if adicFlores == 'Adicionar':
                            flores[count] = f'{defunto[count]}, sim terá flores.'
                        else:
                            flores[count] = f'{defunto[count - 1]}, não terá flores.'
                        d += 1
                count += 1
        else:
            print('Esse nome não está registrado no banco de dados')
    elif alteracaoDados == 'N' or alteracaoDados == 'n':
        break
    else:
        print('Erro, escreva conforme o comunicado, não foi possível alterar os dados!')
    print()
    count = 0
    alteracaoDados = input('Deseja continuar alterando? digite S/N: ')
print()
# estrutura para adicionar mais dados caso desejado
print('Deseja adicionar dados? ')
adicionarDados = input('S/N ')
if adicionarDados == 'S' or adicionarDados == 'N' or adicionarDados == 's' or adicionarDados == 'n':
    if adicionarDados == 'S':
        qteDados = int(input('Quantos dados serão adicionados: '))
        while i < (qteDados + numDados):
            cova.insert(i, i)
            nome = input(
                f'Informe o nome do defunto que será colocado na cova {i}: ')
            defunto.insert(i, nome)
            flor = input('Informe se a cova terá flores com sim/não: ')
            flores.insert(i, f'{nome}, {flor} terá flores.')
            i += 1
else:
    print('Erro, escreva conforme o comunicado, não foi possível adicionar os dados!')
print()
# estrutura de repetição para percorrer o vetor
for n in defunto:
    print(f'{defunto[c]}, está na cova {cova[c]}. {flores[c]}')
    c += 1
print()
print('Trabalho feito por: ')
