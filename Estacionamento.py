#Aluno: Rafael Costa
#Curso: Análise e Desenvolvimento de Sistemas

tipoVeiculo = []
horaEntrada = []
minutoEntrada = []
totalArrecadado = []
opcao = -1



def cadastrarVeiculo():
  print("1 - Moto")
  print("2 - Carro")
  print("3 - Caminhonete")
  tiposV = int(input("informe o tipo do veiculo: "))
  match tiposV:
    case 1:
      tipoVeiculo.append("Moto")
    case 2:
      tipoVeiculo.append("Carro")
    case 3:
      tipoVeiculo.append("Caminhonete")

  horaEntrada.append(int(input("Informe hora de entrada: ")))
  minutoEntrada.append(int(input("Informe o minuto da entrada: ")))

def condicaoPagamento(tempoPermanecido):
  if(tempoPermanecido<=15):
    print("Isento")
  elif(tempoPermanecido<=60):
    print("Total a Pagar: R$ 1,50")
    totalArrecadado.append(1.50)
  elif(tempoPermanecido>60):
    horas_extras = tempoPermanecido // 60
    valor_a_pagar = 1.50 + (horas_extras*1)
    print(f"Total a pagar: R${valor_a_pagar}") 
    totalArrecadado.append(valor_a_pagar) 
  else:
    print("ERRO")

def pagamento():
  horaSaida = 0
  minutoSaida = 0
  print(tipoVeiculo)
  vaga = int(input(f"Qual vaga você quer calcular o preço? 1 a {len(tipoVeiculo)}\n"))
  vaga = vaga-1
  horaSaida = int(input("Digite a hora da saída: "))
  minutoSaida = int(input("Digite o minuto da saida: "))
  print("Hora Entrada:", horaEntrada[vaga], "| Hora Saida:", horaSaida, "| Minuto Entrada:", minutoEntrada[vaga], "| Minuto Saida:", minutoSaida)
  #Calculo do tempo permanecido
  diferenca_horas = horaSaida-horaEntrada[vaga]
  diferenca_minutos = minutoSaida-minutoEntrada[vaga]

  if(diferenca_minutos<0):
      diferenca_minutos += 60
      diferenca_horas -= 1
  
  tempo_total_minutos = (diferenca_horas*60) + diferenca_minutos

  print(f"Tempo permanecido: {diferenca_horas}h{diferenca_minutos}")

  #horasemMinutos = (horaSaida*60)-(horaEntrada[vaga]*60)+(minutoSaida-minutoEntrada[vaga])
  condicaoPagamento(tempo_total_minutos)
  del tipoVeiculo[vaga]

def qtdVeiculo(tipoVeiculo):
  Moto = 0
  Carro = 0
  Caminhonete = 0
  for tipo in tipoVeiculo:
    if(tipo=="Moto"):
      Moto += 1
    elif(tipo=="Carro"):
      Carro += 1
    elif(tipo=="Caminhonete"):
      Caminhonete += 1
  print(f"Motos: {Moto}")
  print(f"Carros: {Carro}")
  print(f"Caminhonetes: {Caminhonete}")

while(opcao!=0):
  print("Estacionamento Sempre Bom\n-----------------------")
  print("Total de Isentos ", len(tipoVeiculo))
  qtdVeiculo(tipoVeiculo)
  print("Total Arredacado R$: ", sum(totalArrecadado))
  print("-----------------------")
  print("1 - Cadastrar Veiculo")
  print("2 - Calcular valor a pagar")
  print("3 - Estornar Cobrança")
  print("0 - Sair do sistema")
  opcao = int(input("Escolha a opcao: "))

  match opcao:
    case 1:
      cadastrarVeiculo()

    case 2:
      pagamento()

    case 3:
      valorEstorno = float(input("Digite o valor do estorno: "))
      if(sum(totalArrecadado)<valorEstorno):
        print("Não temos esse valor de cobrança")
        print("O total que temos é de: ", sum(totalArrecadado))
      else:
        totalArrecadado.append(-valorEstorno)