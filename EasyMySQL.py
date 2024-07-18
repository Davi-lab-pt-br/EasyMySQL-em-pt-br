import mysql.connector

class Conectar:
    @staticmethod
    def conexao():
        return mysql.connector.connect(
            host='Seu host',
            user='Seu usuário',
            password='Sua senha',
            database='Seu banco de dados'
        )
    
    def conexao_fechar():
        mysql.connector.connect(
            host='localhost',
            user='root',
            password='admin',
            database='bdyoutube'
        ).close()

class CURSOR:
    def __init__(self):
        self.conexao = Conectar.conexao()  # Usando a conexão da classe Conectar
        self.cursor = self.conexao.cursor()

    def executar_comando(self,comando):
        self.cursor.execute(comando)

    def fechall(self):
        self.cursor.fetchall()

    def close(self):
        self.cursor.close()
