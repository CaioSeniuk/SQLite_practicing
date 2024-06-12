import sqlite3

# Criando banco de dados
banco = sqlite3.connect('banco_de_dados.db')

# Criando objeto para receber o banco
cursor = banco.cursor() # comando sql para criar tabela, excluir, inserir registros e outras operações dentro do banco

# Criando tabela, onde sera organizado os dados e salvar, SOMENTE uma vez
#cursor.execute("CREATE TABLE pessoas (nome text,idade integer, email text)")

# Inserir dados, SOMENTE UMA VEZ
#cursor.execute("INSERT INTO pessoas VALUES('Maria', 8, 'maria_123@gmail.com')")

# Verificar dados inseridos, ver o que está no banco
'''cursor.execute("SELECT * FROM pessoas") # Selecionar todos os dados da tabela pessoas
print(cursor.fetchall())'''

# Inserindo novo registro no banco

'''cursor.execute("INSERT INTO pessoas VALUES('joao', 10, 'joao@gmail.com')")
cursor.execute("SELECT * FROM pessoas")
print(cursor.fetchall())'''

cursor.execute("DELETE FROM pessoas WHERE nome = 'joao'")
cursor.execute("SELECT * FROM pessoas")
print(cursor.fetchall())
'''# Confirmando se o banco está funcionando
banco.commit()'''
