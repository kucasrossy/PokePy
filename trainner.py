from pokemon import *

class Trainner:
    def __init__(self, nome, pocao, pokemons):
        self.nome = nome
        self.pocao = pocao
        self.pokemons = pokemons
        self.pokemon_atual = pokemons[0]

    def atacando(self,pokemom):
        var_atack = input('Escolha o seu ataque:\n')
        self.mostrar_atack()
        print('Vá {} atague o {} com a/o {}'.format(self.pokemon_atual.nome,pokemom.nome,var_atack))
        self.pokemon_atual.atack(var_atack, pokemom)

    def usar_pocao(self):
        if not self.pocao <= 0:
            if self.pokemon_atual.vida < self.pokemon_atual.maxvida:
                print('O seu {} tem {} de vida'.format(self.pokemon_atual.nome, self.pokemon_atual.vida)) 
                self.pokemon_atual.ganhar_vida(5)
                self.pocao -= 1
                print('Agora ele tem {} de vida'.format(self.pokemon_atual.vida))  
            else:
                print('Vida Maxima')
        else:
            print('Você não possui mais poções')
    
    def mostrar_pokemons(self):
        for pokemon in self.pokemons:
            print(pokemon)
    
    def mostrar_atack(self):
       print('Os golpes do {} são: '.format(self.pokemon_atual.nome))
       for atack in self.pokemon_atual.list_atack:
           print(atack)
    
    def atual_pokemon(self):
        if not (self.pokemon_atual == None):
            print('O seu atual pokemom é {}'.format(self.pokemon_atual.nome))
    
    def escolher_pokemon(self):
        self.mostrar_pokemons()
        var_pokemom = input('Escolha entre eles\n')
        for i in self.pokemons:
            if var_pokemom == i.nome:
                self.pokemon_atual = i
                break
            
class Trainner_enemy:
    pass

'''
pokemon1 = Charmander('Todynho', 5)
pokemon2 = Bulbassauro('Verde', 6)

pokemon3 = Squirtle('Fuck-Year', 10)

lucas = Trainner('Lucas', 10 ,[pokemon1,pokemon2])


lucas.mostrar_atack()

lucas.usar_pocao()
'''
