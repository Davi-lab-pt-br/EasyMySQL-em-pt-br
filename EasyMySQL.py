import mysql.connector

class Conectar:
    @staticmethod
    def conexao():
        return mysql.connector.connect(
            host='localhost',
            user='root',
            password='admin',
            database='bdyoutube'
        )

class CURSOR:
    def __init__(self):
        self.conexao = Conectar.conexao()  # Usando a conexão da classe Conectar
        self.cursor = self.conexao.cursor()

    def executar_comando(self,comando):
        self.cursor.execute(comando)
