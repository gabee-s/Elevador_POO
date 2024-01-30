'''[PY-A11] Você foi contratado para desenvolver o software de controle de um elevador inteligente. A classe Elevador foi criada para modelar esse sistema e possui os seguintes atributos: totalCapacidade, atualCapacidade, totalAndar e atualAndar, que representam, respectivamente, a capacidade máxima do elevador, a capacidade atual, o total de andares do prédio e o andar atual do elevador.

A classe Elevador também possui os seguintes métodos:

Subir(): caso o elevador não esteja no andar mais alto, o método incrementa o número do andar atual e exibe "Subindo". Caso contrário, exibe "VOCÊ ESTÁ NO ANDAR MAIS ALTO!".

Descer(): caso o elevador não esteja no térreo, o método decrementa o número do andar atual e exibe "Descendo". Caso contrário, exibe "VOCÊ JÁ ESTÁ NO TÉRREO!".

Entrar(): caso a capacidade atual do elevador não tenha sido atingida, o método incrementa o número de pessoas presentes no elevador e exibe "Entrando uma pessoa". Caso contrário, exibe "O ELEVADOR ESTÁ CHEIO!".

Sair(): caso haja pelo menos uma pessoa no elevador, o método decrementa o número de pessoas presentes e exibe "Saindo uma pessoa". Caso contrário, exibe "NÃO TEM NINGUÉM".
'''

class Elevador:
    def __init__(self,totalCapacidade, atualCapacidade, totalAndar, atualAndar):
        self.totalCapacidade = totalCapacidade
        self.atualCapacidade = atualCapacidade
        self.totalAndar = totalAndar
        self.atualAndar = atualAndar
    
    def subir(self):
        if self.atualAndar < self.totalAndar:
            print('Subindo')
            self.atualAndar+=1
        else:
            print('VOCÊ ESTÁ NO ANDAR MAIS ALTO!')


    def descer(self):
        if 0 < self.atualAndar <= self.totalAndar:
            print('Descendo')
            self.atualAndar-=1
        else:
            print('VOCÊ JÁ ESTÁ NO TÉRREO!')


    def entrar(self):
        if self.atualCapacidade < self.totalCapacidade:
            print('Entrando uma pessoa')
            self.atualCapacidade +=1
        else:
            print('O ELEVADOR ESTÁ CHEIO')

    def sair(self):
        if 0 < self.atualCapacidade <= self.totalCapacidade:
            print('Saindo uma pessoa')
            self.atualCapacidade -=1
        else:
            print('NÃO TEM NINGUÉM')
