
from random import choice
from random import randint
from random import randrange


gestures = {1 : "ROCK", 
            2 : "PAPER", 
            3 : "SCISSORS",
            4 : "LIZARD",
            5 : "SPOCK"
            }

# SCORE CONTENEDORES
cpu_score = []
player_score = []

#CHOICES CONTENEDORES
cpu = 0
player = 0

def Num_Rounds():

    maxRounds = 10

    while True:
        player_rounds = input('\n''\t' 'Choose number of rounds [ODD] -------------> ')

        try:
            if (int(player_rounds) + 1) % 2 == 0:
                n_rounds = int(player)
                break

            elif (int(player_rounds) > maxRounds) and ((int(player_rounds) + 1) % 2 == 0):
                print('\n''\t'"WARNING:"'\n''\t'"That number is too high"'\n''\n')

            else:
                print('\n''\t'"WARNING:"'\n''\t'"Please enter a valid option"'\n''\n')

        except (ValueError):
            print('\n''\t'"WARNING:"'\n''\t'"Please enter a valid option"'\n''\n')

    return int(player_rounds)          

def CPU_choice():
    cpu = randint(1,len(gestures))
    return cpu

def Player_choice():

    while True:

        player = input('\n''\t' 'ROCK [1] | PAPER [2] | SCISSORS [3] | LIZARD [4] | SPOCK [5]' '\n'
            '\t' 'Choose one option -------------> ')

        try:
            if  int(player) <= len(gestures):
                player = int(player)
                break

            elif int(player) > len(gestures):
                print('\n''\t'"WARNING:"'\n''\t'"Please enter a valid option"'\n''\n')
            
            else:
                print('\n''\t'"WARNING:"'\n''\t'"Please enter a valid option"'\n''\n')

        except (ValueError):
            print('\n''\t'"WARNING:"'\n''\t'"Please enter a valid option"'\n''\n')

    print('\n' + f'You have chosen: {gestures.get(player)}')
    return player

def Rounds():

    # TIE
    if cpu == player:
        result_rounds = 0

    #CPU WINS COMBINATIONS 
    elif cpu == list(gestures)[0]   and   (player == list(gestures)[2] or player == list(gestures)[3]):   
        # rock wins scissors.2 and lizard.3
        result_rounds = 1
    elif cpu == list(gestures)[1]   and   (player == list(gestures)[0] or player == list(gestures)[4]):
        # paper wins rock.0 and spock.4
        result_rounds = 1
    elif cpu == list(gestures)[2]   and   (player == list(gestures)[1] or player == list(gestures)[3]):
        # scissors wins paper.1 or lizard.3
        result_rounds = 1
    elif cpu == list(gestures)[3]  and    (player == list(gestures)[1] or player == list(gestures)[4]):
        # lizard wins paper.1 or spock
        result_rounds = 1
    elif cpu == list(gestures)[4]  and    (player == list(gestures)[0] or player == list(gestures)[2]):
        # spock wins rock.0 or scissors.2
        result_rounds = 1


    #PLAYER WINS COMBINATION 
    elif player == list(gestures)[0]   and   (cpu == list(gestures)[2] or cpu == list(gestures)[3]):   
        # rock wins scissors.2 and lizard.3
        result_rounds = 2
    elif player == list(gestures)[1]   and   (cpu == list(gestures)[0] or cpu == list(gestures)[4]):
        # paper wins rock.0 and spock.4
        result_rounds = 2
    elif player == list(gestures)[2]   and   (cpu == list(gestures)[1] or cpu == list(gestures)[3]):
        # scissors wins paper.1 or lizard.3
        result_rounds = 2
    elif player == list(gestures)[3]  and    (cpu == list(gestures)[1] or cpu == list(gestures)[4]):
        # lizard wins paper.1 or spock
        result_rounds = 2
    elif player == list(gestures)[4]  and    (cpu == list(gestures)[0] or cpu == list(gestures)[2]):
        # spock wins rock.0 or scissors.2
        result_rounds = 2


    else:
        result_rounds = print('Something went wrong in rounds')

    return result_rounds

def PrintResult():

    cpu_round = 0
    player_round = 0

    if result_rounds == 0: #TIES
        cpu_round += 0
        player_round += 0
        print("\n""\t""\t" f"#######  TIED  #######" "\n")

    elif result_rounds == 1: #CPU WINS COMBINATION
        cpu_round += 1
        player_round += 0
        print("\n""\t""\t" f"####### U  LOSE #######" "\n" )

    elif result_rounds == 2: #HUMAN WINS COMBINATION
        cpu_round += 0
        player_round += 1
        print("\n""\t""\t" f"#######  U WON  #######" "\n")

    return (cpu_round, player_round)

## GAME ##
rounds_to_win = Num_Rounds()

while rounds_to_win != 0:

    print('\n''\t''\t' '-----------------------' '\n'
            '\t''\t'' ##### LETS PLAY #####' '\n'
            '\t''\t' '-----------------------' '\n'
            '\n''\t''\t' f'# YOU`VE GOT {rounds_to_win} ROUNDS #' '\n')

    # PLAYERS CHOICE
    cpu = CPU_choice()
    player = Player_choice()

    # SCORES
    result_rounds = Rounds()
    result = PrintResult()

    cpu_score.append(result[0])
    player_score.append(result[1])


    # UPDATING THE COUNTER
    if result_rounds !=0:
        rounds_to_win -= 1
 
        print("\t" "\t" "-----------------------" "\n"
              "\t" "\t" "######   SCORE   ######" "\n" 
            "\t""\t" f"     CPU {sum(cpu_score)} | YOU {sum(player_score)}" "\n"
              "\t" "\t" "-----------------------" "\n")
    else:
        rounds_to_win += 0

    print("\t""\t" f"#### {rounds_to_win} rounds left ####""\n"
          "\t""\t" "-----------------------" "\n")

## FINAL RESULT
if rounds_to_win == 0:
    print("\n""\n""\t" "\t" "####  FINAL SCORE  ####" "\n" 
          "\t""\t" f"     CPU {sum(cpu_score)} | YOU {sum(player_score)} ")

    if sum(cpu_score) > sum(player_score):
        print("\n""\t""\t" "#######################"  "\n"
              "\t""\t"     "## YOU LOSE THE GAME ##"  "\n"
              "\t""\t"     "#######################"  "\n")
    
    elif sum(cpu_score) < sum(player_score):
        print("\n""\t""\t" "#######################"  "\n"
              "\t""\t"     "### YOU WON THE GAME ##"  "\n"
              "\t""\t"     "#######################"  "\n")

    elif sum(cpu_score) == sum(player_score):
        print("\n""\t""\t" "#######################"  "\n"
              "\t""\t"     "## TIED WITH MACHINE ##"  "\n"
              "\t""\t"     "#######################"  "\n")      
    else:
        pass