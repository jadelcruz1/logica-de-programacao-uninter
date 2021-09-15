while True :
    # esse codigo foi criado para imprimir o nome do aluno a nota o conceito da nota.
    Aluno = input('Nome do aluno:')
    if Aluno == 'sair': # esse condição  foi criado para finalizar o progrma a qualquer momento pelo usuário.
        print('você finalizou o sistema')
        break
    Nota = float(input('Nota final:'))

    while True :


        if Nota < 2.0:
            print('O aluno {} tirou a nota {} e se enquadra no conceito E.'.format(Aluno, Nota) )

        else:
          if Nota < 4.9:
            print('O aluno {} tirou a nota {} e se enquadra no conceito D.' .format(Aluno, Nota) )
            break

          if Nota < 6.9:
            print('O aluno {} tirou a nota {} e se enquadra no conceito C.'.format(Aluno, Nota) )
            break

          if Nota < 8.9:
            print('O aluno {} tirou a nota {} e se enquadra no conceito B.'.format(Aluno, Nota) )
            break
          if Nota < 10:
            print('O aluno {} tirou a nota {} e se enquadra no conceito A.'.format(Aluno, Nota) )
            break


