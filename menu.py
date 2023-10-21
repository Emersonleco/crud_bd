import bd

while True:
    print('-- Bem vindo ao menu --')
    print('1 - Adicionar aluno')
    print('2 - Editar aluno')
    print('3 - Deletar aluno')
    print('4 - listar todos alunos')
    print('5 - sair')
    opcao = int(input('Selecione uma opção: '))
    if opcao == 1:
        nome = input('Digite o nome do aluno: ')
        idade = input('Digite a idade do aluno: ')
        nota = float(input('Digite a nota do aluno: '))
        bd.insert(nome, idade, nota)
    elif opcao == 2:
        nome = input('Digite o nome do aluno: ')
        idade = input('Digite a idade do aluno: ')
        nota = float(input('Digite a nota do aluno: '))
        matricula = int(input('Digite a matricula do aluno: '))
        bd.update(nome, idade, nota, matricula)
    elif opcao == 3:
        matricula = int(input('Digite a matricula do aluno: '))
        bd.delete(matricula)
    elif opcao == 4:
        bd.select()
    else:
        break
