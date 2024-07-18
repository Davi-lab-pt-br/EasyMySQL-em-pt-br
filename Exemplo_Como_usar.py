from EasyMySQL import *

# Criando a conexão
conectar = Conectar()

# Criando o cursor
cursor = CURSOR()

# Comando SQL
comando = 'INSERT INTO bdyoutube.vendas_dois (nome, valor) VALUES ("Todynho", 3)'

# Executando o comando
cursor.executar_comando(comando)

# Lembre-se de commit se necessário
cursor.conexao.commit()

conect.conexao.close()
cursor.close()
