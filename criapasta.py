import os

def cria(nomearquivo):
	try:
		comando =f"touch {nomearquivo}"
		retorno = os.system(comando)
		if retorno == 0:
			print(f"Arquivo {nomearquivo} criado")
		else:
			print(f"Falha ao criar o arquivo {nomearquivo}")
	except OSError as e:
		print(f"Erro ao tentar criar o arquivo {nomearquivo}: {e}")

def cria_pasta(nomepasta):	
	try:
		if not os.path.exists(nomepasta):
			os .makedirs(nomepasta)
			print(f"A pasta {nomepasta} foi criada")
		else:
			print(f"A pasta {nomepasta} JA EXISTE")
	except OSError as e:
		print(f"Erro ao tentar criar {nomepasta}: {e}")

if __name__ == "__main__":
	nomepasta = input("Digite o nome da pasta: ")
	cria_pasta(nomepasta)
	n = int(input("Digite a quantidade de arquivos: "))
	i = 0
	while (i < n):
		nomearquivo = "arquivo"+str(i)+".txt"
		cria(nomearquivo)
		i+=1
