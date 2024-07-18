import mysql.connector

class Conectar:
    @staticmethod
    def conexao():
        return mysql.connector.connect(
            host='Seu host',
            user='Seu usuário',
            password='Sua senha',
            database='Seu banco de dados'
            #Preencha essas informações que estão em aspas simples de acordo com seu host, usuário, senha, e banco de dados no MySQL Workbench
        )

class CURSOR:
    def __init__(self):
        self.conexao = Conectar.conexao()  # Usando a conexão da classe Conectar
        self.cursor = self.conexao.cursor()

    def executar_comando(self,comando):
        self.cursor.execute(comando)
