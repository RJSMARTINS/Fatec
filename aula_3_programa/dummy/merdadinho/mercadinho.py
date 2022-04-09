#author: Renan Martins  
#version: 1.0.1
#date: 04/09/2022
#description: Este programa cadastra usuarios
#project: Mercadinho

from asyncore import read
from hashlib import sha256
import csv
import sys
from time import sleep

# mensagem de boas vindas

mensagem = "Olá, seja bem vindo ao mercadinho Fatec"

# imprimindo mensagem de boas vindas como maquina de escrever

for letra in mensagem:
    sys.stdout.write(letra)
    sys.stdout.flush()
    sleep(0.1)
print()

# setando as opções do menu

opicoes_de_login = ["sig in", "sign up", "deletar usuario", "Esqueci a senha", "Fale conosco", "cadastrar-se"]

# imprimindo menu de opções

count = 1 
for opcao in opicoes_de_login:
    print(f"[{count}] - {opcao}")    
    count += 1 #count = count + 1
    print("")
opcao_digitada = input ("Qual opção deseja? ")

with open("dbs.csv") as arquivo:
    print(arquivo.read())
    
