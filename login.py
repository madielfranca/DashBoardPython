from PyQt5 import uic,QtWidgets
import sqlite3
from tkinter import *
import os

# Create Object
root = Tk()

def chama_segunda_tela():
    primeira_tela.label_4.setText("")
    nome_usuario = primeira_tela.lineEdit.text()
    senha = primeira_tela.lineEdit_2.text()
    if nome_usuario == "joao123" and senha == "123456" :
        primeira_tela.close()
        segunda_tela.show()
    else :
        primeira_tela.label_4.setText("Dados de login incorretos!")

def open_file():

    #os.system('F:\jogos\MK11\MK11\Binaries\Retail\MK11.exe')
    #os.system('F:\jogos\guitar\GH3.exe')
    os.system('C:/Windows/System32/notepad.exe')

def logout():
    segunda_tela.close()
    primeira_tela.show()

def abre_tela_cadastro():
    tela_cadastro.show()


def cadastrar():
    nome = tela_cadastro.lineEdit.text()
    login = tela_cadastro.lineEdit_2.text()
    senha = tela_cadastro.lineEdit_3.text()
    c_senha = tela_cadastro.lineEdit_4.text()

    if (senha == c_senha):
        try:
            banco = sqlite3.connect('banco_cadastro.db') 
            cursor = banco.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS cadastro (nome text,login text,senha text)")
            cursor.execute("INSERT INTO cadastro VALUES ('"+nome+"','"+login+"','"+senha+"')")

            banco.commit() 
            banco.close()
            tela_cadastro.label.setText("Usuario cadastrado com sucesso")

        except sqlite3.Error as erro:
            print("Erro ao inserir os dados: ",erro)
    else:
        tela_cadastro.label.setText("As senhas digitadas estão diferentes")
    

    


app=QtWidgets.QApplication([])
primeira_tela=uic.loadUi("primeira_tela.ui")
segunda_tela = uic.loadUi("segunda_tela.ui")
tela_cadastro = uic.loadUi("tela_cadastro.ui")
#Button(root, text='Open',
 #      command=open_file).pack(side=TOP,
  #                             pady=10)
primeira_tela.pushButton.clicked.connect(open_file)
primeira_tela.pushButton_2.clicked.connect(open_file)


primeira_tela.show()
app.exec()
