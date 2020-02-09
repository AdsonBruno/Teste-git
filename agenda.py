# Agenda simples utilizando listas com python

# Criando variáveis necessárias
agenda = [] #Armazena as variáveis na lista
vref = False #Verificador de condição
achou = False #Será utilizando quando for preciso encontrar algo
x = 0 # controlando o índice

#loop para executar enquanto não for solicitado a parada e ir adicionando os contatos
while True:
    
    #Menú de opções
    print()
    print('\t------Menú de opções------')
    print()
    print('''\t(1) - Adicionar novo contato
    \t(2) - Modificar Contato
    \t(3) - Excluir contato
    \t(4) - Mostrar contatos
    \t(5) - Sair''')
    try:
        menu = int(input('\tInforme a opção: '))
    except:
        print('Apenas valores inteiros são aceitos!')
    print()

    #iniciando o algoritmo
    #Adicionando contato
    if menu == 1:
        nome = input('Nome: ')
        while not vref: #Verifica enquanto o tipo não for do valor inteiro
            try: #verificando se o tipo é o correto
                numero = int(input('Número: '))
                vref = True #Fica verdade quando a condição é satisfeita
            except:
                print('Formato incorreto!')
            #adicionando os contatos na lista "agenda"
        agenda.append([nome, numero])
        #ordenando agenda
        agenda.sort()  
        vref = False
        print(agenda)
        print()

    # Modificando contato
    elif menu == 2: 
        busca = input('Pesquisar: ')
        print()
        #convertendo para um inteiro se for possível
        try:
            convercao = int(busca)
            busca = convercao
        except:
            pass

        if len(agenda) > 0:
            #percorrendo a lista
            while x < len(agenda):
                while x < len(agenda):
                    # print(x)
                    if agenda[x][0] == busca or agenda[x][1] == busca:
                        print()
                        print('-'*25)
                        print(f'Contato encontrado\nNome: {agenda[x][0]}\nNúmero: {agenda[x][1]}')
                        print('-'*25)
                        print()
                        achou = True # Será ativado se o contato for encontrado
                        pos = x
                        # Caso o contato desejado seja encontrado, a variável de x receberá o tamanho da lista "agenda", encerrando
                        # a execução
                        if achou:
                            x = len(agenda)

                        print('\tOpções')
                        print('\t1 - Editar Nome')
                        print('\t2 - Editar Número')
                        print('\t3 - Sair')
                        while not vref:
                            opc = int(input('\tO que deseja fazer?: '))
                            if opc == 1 or opc == 2 or opc == 3:
                                vref = True  
                            else:
                                print('Opção inválida')  
                        # print(agenda[pos])
                        # modificando o nome
                        if opc == 1:
                            print()
                            novo = input('Nome: ')
                            #recebendo a modificação do nome, pos é o índice que foi encontrado. [0] é o índice do nome
                            agenda[pos][0] = novo 
                            print('Nome modificado com sucesso!') 
                            print()
                            print('-'-25)
                            print(f'Nome: {agenda[pos][0]} \nNúmero: {agenda[pos][1]}')
                            print('-'-25)
                            print()
                        
                        #Modificando o número
                        elif opc == 2:
                            while not vref:
                                try:
                                    novo = int(input('Número: ')) 
                                    vref = True # Se a condição for satisfeita, vref será ativada
                                except:
                                    print('Apenas números')
                            vref = False # Desativando vref para outras possíveis
                            #recebendo a modificação do número, que dentro da segunda lista, é a posição 1
                            agenda[pos][1] = novo
                            print()
                            print('Número modificado com sucesso!')
                            print('-'*25)
                            print(f'Nome: {agenda[pos][0]} \nNúmero: {agenda[pos][1]}')
                            print('-'*25)
                            print()
                        elif opc == 3:
                            break

                    x += 1 #incrementa 1 a cada passagem do looping

            if not achou: #Se achou for False, então ele diz que o contato não existe
                print('Contato não existe.')
            #fazendo com que achou volte a ser False
            achou = False
            break
        else:
            print('Agenda vazia!')
    
    # Excluindo contato
    elif menu == 3:
        #buscando contato
        busca = input('Pesquisar: ')
        #convertendo para int
        try:
            convercao = int(busca)
            busca = convercao
        except:
            pass
        
        #verificando se a lista está vazia
        if len(agenda) > 0:
            # percorrendo a lista agenda
            while x < len(agenda):
                while x < len(agenda):
                    if agenda[x][0] == busca or agenda[x][1] == busca:
                        print(f'Nome: {agenda[x][0]} \nNúmero: {agenda[x][1]}')
                        achou = True
                        del(agenda[x])

                        if achou:
                            x = len(agenda)
                        print('Contato excluído com sucesso.')
                    x += 1

    #mostrando todos os contatos da agenda
    elif menu == 4:
        #percorrendo a agenda e mostrando os contatos
        if len(agenda) > 0:
            for e in agenda:
                # print()
                print('-'*25)
                print(f'Nome: {e[0]} \nNúmero: {e[1]}')
                print('-'*25)
                print()
        else:
            print('Agenda vazia')
    #encerrando a execução do programa
    elif menu == 5:
        print('Execução encerrada.')
        break
    else:
        print('Opção inválida!')