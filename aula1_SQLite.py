import sqlite3

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

try:
    banco = sqlite3.connect('banco_de_dados2.db')
    cursor = banco.cursor()
    deletar = "joao"
    cursor.execute(f"DELETE from tabela_nova WHERE nome = '{deletar}' ")
    banco.commit()
    banco.close()
    print("Os dados foram excluídos com sucesso!")

except sqlite3.Error as erro:
    print("Erro ao excluir os dados:", erro)
