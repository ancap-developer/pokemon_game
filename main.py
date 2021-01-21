import pickle

from pokemon import *
from pessoa import *


def escolher_pokemon_incial(player):
    print('Olá {}, você poderá escolher agora o Pokémon que irá lhe acompanhar nessa jornada!'.format(player))

    pikachu = PokemonEletrico('Pikachu', level=1)
    charmander = PokemonFogo('Charmander', level=1)
    squirtle = PokemonAgua('Squirtle', level=1)

    print('Você possui 3 escolhas: ')
    print('1 -', pikachu)
    print('2 -', charmander)
    print('3 -', squirtle)

    while True:
        escolha = input('Escolha o seu Pokémon: ')

        if escolha == '1':
            player.capturar(pikachu)
            break
        elif escolha == '2':
            player.capturar(charmander)
            break
        elif escolha == '3':
            player.capturar(squirtle)
            break
        else:
            print('Escolha inválida')


def salvar_jogo(player):
    try:
        with open('database.db', 'wb') as arquivo:
            pickle.dump(player, arquivo)
            print('*Jogo salvo*')
    except Exception as error:
        print('Erro ao salvar jogo')
        print(error)


def carregar_jogo():
    try:
        with open('database.db', 'rb') as arquivo:
            player = pickle.load(arquivo)
            print('Loading feito com sucesso')
            return player
    except:
        print('Save não encontrado')


if __name__ == '__main__':
    print('==========================================')
    print('Bem-vindo ao game Pokémon RPG feito em Python')
    print('==========================================')

    player = carregar_jogo()

    if not player:

        nome = input('Olá, qual o seu nome: ')
        player = Player(nome)
        print('Olá {}, esse é um mundo habitado por Pokémons, '
              'a partir de agora sua missão é se tornar o mestre dos Pokémons'.format(nome))
        print('Capture o máximo de Pokémons que conseguir e lute contra seus inimigos')
        player.mostrar_dinheiro()

        if player.pokemons:
            print('Já vi que você tem alguns Pokémons')
            player.mostrar_pokemons()
        else:
            print('Você não tem nenhum Pokémon, portanto precisa escolher um!')
            escolher_pokemon_incial(player)
            print('Pronto, agora que você já possui um Pokémon, enfrente seu arqui-rival Gary')
            gary = Inimigo(nome='Gary', pokemons=[PokemonAgua('Squirtle', level=1)])
            player.batalhar(gary)
            salvar_jogo(player)

    while True:
        print('==========================================')
        print('O que deseja fazer?')
        print('1 - Explorar o mundo')
        print('2 - Lutar com um inimigo')
        print('3 - Ver Pokédex')
        print('0 - Sair do jogo')
        escolha = input('Sua escolha: ')

        if escolha == '0':
            print('*Fechando o jogo*')
            break
        elif escolha == '1':
            player.explorar()
            salvar_jogo(player)
        elif escolha == '2':
            player.batalhar(Inimigo())
            salvar_jogo(player)
        elif escolha == '3':
            player.mostrar_pokemons()
        else:
            print('Escolha inválida!')
