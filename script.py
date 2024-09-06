#Definindo a função para a execução de listagem dos contatos.
def lista_de_contatos(contatos):
  if not contatos:
    print('Lista vazia')
  else:
    for contato in contatos:
      print(contato)
#Inicio do progama.
print('Bem vindo a sua lista telefonica virtual.')
print('Deseja iniciar') 
iniciar = input('')
if iniciar == ('sim' or 'Sim' or 'sIM' or 'SIm' or 'sIm' or 'siM' or 'SIM'): 
#Criando uma lista e um sistema while para mostrar as opções.
 contatos = []
while True:
 print('1.Adicionar contato')
 print('2.Listar contato')
 print('3.Remover contatos')
 print('4.Sair') 
 opcao = input('Digite a opção desejada:')
#Sistema de escolhas.
 if opcao == '1':
  nome = input('Nome:')
  numero = input('Numero:')
  contatos.append({'nome': nome, 'numero': numero})
  print('Contato adicionado com sucesso')
 elif opcao == '2':
  print('Listando contatos') 
  lista_de_contatos(contatos) 
 elif opcao == '3': 
    nome = input('Nome do contato que deseja remover:')
    contatos = [contato for contato in contatos if contato['nome'] != nome]
    print('Contato removido com sucesso')
#Saindo.
 elif opcao == '4':
  print('Saindo do programa')
  break 
else: 
 print('Opção inválida')