import sqlite3, os, time

# Criando banco de dados
#banco = sqlite3.connect('banco_de_dados2.db')

# Criando objeto para receber o banco
#cursor = banco.cursor() # comando sql para criar tabela, excluir, inserir registros e outras operações dentro do banco

# Criando tabela, onde sera organizado os dados e salvar, SOMENTE uma vez
#cursor.execute("CREATE TABLE tabela_nova (nome text,idade integer)")

# Inserir dados, SOMENTE UMA VEZ
#cursor.execute("INSERT INTO tabela_nova VALUES('Maria', 20)")

# Verificar dados inseridos, ver o que está no banco
#cursor.execute("SELECT * FROM pessoas") # Selecionar todos os dados da tabela pessoas
#print(cursor.fetchall())

# Deletar um parâmetro
#cursor.execute("DELETE from tabela_nova WHERE idade = 20")

# Enviar os dados pro banco
#banco.commit()
def inserir_dados(nome,idade):
    cursor.execute(f"INSERT INTO tabela_nova VALUES('{nome}', {idade})")
    banco.commit()
    print("\nDados inseridos com sucesso!")

def deletar_usuario(deletar, parametro):
    try:
        banco = sqlite3.connect('banco_de_dados2.db')
        cursor = banco.cursor()
        cursor.execute(f"DELETE from tabela_nova WHERE {parametro} = '{deletar}' ")
        banco.commit()
        banco.close()
        print("Os dados foram excluídos com sucesso!")
        time.sleep(2)
        

    except sqlite3.Error as erro:
        print("Erro ao excluir os dados:", erro)
        time.sleep(2)

while True:
    banco = sqlite3.connect('banco_de_dados2.db')
    cursor = banco.cursor()
    os.system("cls")
    fazer = int(input("\nO que deseja fazer?\n1- adicionar usuário\n2- deletar usuário\n3- SAIR\n\n--> "))

    if fazer == 1:
        nome = str(input("\nInsira o nome para registrar no banco de dados: "))
        idade = int(input("\nInsira a idade para registrar no banco de dados: "))
        inserir_dados(nome,idade)

    elif fazer == 2:
        cursor.execute("SELECT * FROM tabela_nova") # Selecionar todos os dados da tabela pessoas
        print(cursor.fetchall())
        parametro_deletar = str(input("\nInsira qual parametro quer DELETAR (nome, idade): "))
        dado_deletar = input("\nInsira o dado para DELETAR do banco de dados: ")
        deletar_usuario(dado_deletar, parametro_deletar)
        
    elif fazer == 3:
        break
    else:
        print("Erro, insira um valor válido!")
        continue