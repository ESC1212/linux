import os

def cria(nomepasta, nomearquivo):
    try:
        caminho_completo = os.path.join(nomepasta, nomearquivo)
        comando = f"touch {caminho_completo}"
        retorno = os.system(comando)
        if retorno == 0:
            print(f"Arquivo {nomearquivo} criado em {nomepasta}")
        else:
            print(f"Falha ao criar o arquivo {nomearquivo}")
    except OSError as e:
        print(f"Erro ao tentar criar o arquivo {nomearquivo}: {e}")

def cria_pasta(nomepasta):
    try:
        if not os.path.exists(nomepasta):
            os.makedirs(nomepasta)
            print(f"A pasta {nomepasta} foi criada")
        else:
            print(f"A pasta {nomepasta} JÁ EXISTE")
    except OSError as e:
        print(f"Erro ao tentar criar {nomepasta}: {e}")

if __name__ == "__main__":
    nomepasta = input("Digite o nome da pasta: ")
    cria_pasta(nomepasta)
    n = int(input("Digite o número de arquivos a serem criados: "))
    for i in range(n):
        nomearquivo = f"arquivo{i}.txt"
        cria(nomepasta, nomearquivo)

