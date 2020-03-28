#Classe de Pokemom
class Pokemon:
    def __init__(self, nome, tipo, nivel):
        self.nome = nome
        self.tipo = tipo
        self.nivel = nivel
        self.maxvida = nivel * 10
        self.vida = self.maxvida
        self.vivo = True

    def __repr__(self):
        return self.nome
    
    def perder_vida(self, valor):
        if self.morreu():
            return 'O seu pokemom saiu da batalha'
        else:
            self.vida -= valor
            return 'O seu {} tem agora {} de vida'.format(self.nome, self.vida)
    
    def ganhar_vida(self, valor):
        self.vida += valor
        if self.vida > self.maxvida:
            self.vida = self.maxvida
        
    def morreu(self):
        if self.vida <= 0:
            self.vivo = False
            return True
        else:
            return False

#Classe do Charmander
class Charmander(Pokemon):

    list_atack = {'bola de fogo': 3, 'Investida' : 1, 'tornado de fogo' : 5}

    def __init__(self, nome, nivel):
        super().__init__(nome, 'Fogo', nivel)
        self.raca = "Charmander"
    
    def atack(self, atack, pokemon):

        if atack in self.list_atack:
            aux = 0
            if pokemon.tipo == 'Fogo':
                aux = 0
            elif pokemon.tipo == 'Grama':
                aux = 2
            else:
                aux = -1
            pokemon.perder_vida(self.list_atack[atack] + aux)
            return '{} atacou o {} com a Habilidade {}'.format(self.nome, pokemon.nome, atack)
        else:
             pokemon.perder_vida(self.list_atack['Investida'] + aux)
             return '{} atacou o {} com a Habilidade Investida'.format(self.nome, pokemon.nome)

#Class Bubasoauro
class Bulbassauro(Pokemon):

    list_atack = {'chigode de vinha': 3, 'Investida' : 1, 'tufao de folha' : 5}

    def __init__(self, nome, nivel):
        super().__init__(nome, 'Grama', nivel)
        self.raca = "Bulbassauro"
    
    def atack(self, atack, pokemon):
        if atack in self.list_atack:
            aux = 0
            if pokemon.tipo == 'Grama':
                aux = 0
            elif pokemon.tipo == 'Agua':
                aux = 2
            else:
                aux = -1
            pokemon.perder_vida(self.list_atack[atack] + aux)
            return '{} atacou o {} com a Habilidade {}'.format(self.nome, pokemon.nome, atack)
        else:
             pokemon.perder_vida(self.list_atack['Investida'] + aux)
             return '{} atacou o {} com a Habilidade Investida'.format(self.nome, pokemon.nome)

#Class Squirdle
class Squirtle(Pokemon):

    list_atack = {'tiro de bolha': 3, 'Investida' : 1, "jato d'agua" : 5}

    def __init__(self, nome, nivel):
        super().__init__(nome, 'Grama', nivel)
        self.raca = "Squirtle"
    
    def atack(self, atack, pokemon):
        if atack in self.list_atack:
            aux = 0
            if pokemon.tipo == 'Grama':
                aux = -1
            elif pokemon.tipo == 'Agua':
                aux = 0
            else:
                aux = 2
            pokemon.perder_vida(self.list_atack[atack] + aux)
            return '{} atacou o {} com a Habilidade {}'.format(self.nome, pokemon.nome, atack)
        else:
             pokemon.perder_vida(self.list_atack['Investida'] + aux)
             return '{} atacou o {} com a Habilidade Investida'.format(self.nome, pokemon.nome)
    

