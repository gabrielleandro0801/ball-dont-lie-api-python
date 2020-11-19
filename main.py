import requests

print('#######################')
print('#### Ball Dont Lie ####')
print('#######################')

def main():
    print('\nEscolha a Opcao:')
    print('<1> Ver franquia')
    print('<2> Ver jogador')
    print('Sua opcao: ')
    opcao = int(input())

    try:
        if opcao == 1:
            franchise = input('Digite um numero de 1 a 30: ')
            request = requests.get('https://www.balldontlie.io/api/v1/teams/' + franchise)
            franchise_data = request.json()
            print('Sigla: ' + str(franchise_data["abbreviation"]))
            print('Nome: ' + str(franchise_data["name"]))
            print('Nome completo: ' + franchise_data["full_name"])
            print('Conferencia: ' + franchise_data["conference"])
            print('Divisao: ' + franchise_data["division"])

        elif opcao == 2:
            player = input('Digite um numero de 1 a 3092: ')
            request = requests.get('https://www.balldontlie.io/api/v1/players/' + player)
            player_data = request.json()
            print('Nome: ' + player_data["first_name"] + " " + player_data["last_name"])
            print('Posicao: ' + player_data["position"] if player_data["position"] is not "" else "Posicao nao informada!")
            print('Peso: ' + str(player_data["weight_pounds"]) + " lbs" if player_data["weight_pounds"] is not None else "Peso nao informado!")
            print('Altura (em pes): ' + str(player_data["height_feet"]) + "'" + str(player_data["height_inches"]) if player_data["height_feet"] is not None and player_data["height_feet"] is not None else "Altura nao informada!")
            team_data = player_data.get("team")
            print('Time: ' + team_data["full_name"])
        else:
            print('Opcao invalida!')
            exit()
    except Exception as e:
        print('Erro ao fazer a busca da franquia | do jogador: ' + e)

    opcao = input('\nDeseja buscar novamente? (sim ou nao) ')
    if opcao.lower() == 'sim':
        main()
    else:
        print('Fim de Programa')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
