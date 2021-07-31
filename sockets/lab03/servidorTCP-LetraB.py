# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
# COMPONENTES DO GRUPO:
# FRANCISCO DANIEL DAVI - 20180035037
# LUIZ HENRIQUE ARAUJO DANTAS - 20180109005
#
# SCRIPT: Servidor de sockets TCP modificado para receber texto minusculo do cliente enviar resposta em maiuscula  (python 3)
#

# importacao das bibliotecas
from socket import *  # sockets

# definicao das variaveis
serverName = ''  # ip do servidor (em branco)
serverPort = 61000  # porta a se conectar
serverSocket = socket(AF_INET, SOCK_STREAM)  # criacao do socket TCP
serverSocket.bind((serverName, serverPort))  # bind do ip do servidor com a porta
serverSocket.listen(1)  # socket pronto para 'ouvir' conexoes
print('Servidor TCP esperando conexoes na porta %d ...' % (serverPort))
while 1:
  connectionSocket, addr = serverSocket.accept()  # aceita as conexoes dos clientes

  sentence = connectionSocket.recv(1024)  # recebe dados do cliente
  sentence = sentence.decode('utf-8')

  if sentence == 'Obter arquivo.txt':
    with open('arquivo.txt', 'rb') as file:
      for data in file.readlines():
        connectionSocket.send(data)
  else:
    data = 'ERRO'
    connectionSocket.send(data.encode())
  print('Cliente %s enviou: %s, o servidor respondeu com : %s' % (addr, sentence, data))
  # connectionSocket.send(ler_arquivo.encode('utf-8')) # envia para o cliente o texto transformado
  connectionSocket.close()  # encerra o socket com o cliente
serverSocket.close()  # encerra o socket do servidor