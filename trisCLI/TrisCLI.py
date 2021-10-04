# _____   ____   _   ____
#/__ __\ /  __\ / \ / ___\ 
#  / \   |  \/| | | |    \ 
#  | |   |    / | | \___ | 
#  \_/   \_/\_\ \_/ \____/ 

# autore: Filippo Bollito
# versione: 2.9
# novità: miglioramento modalità difficile
# data: 29/9/2021

import sys, os, time, random

def cls():
    if sys.platform == 'linux':
        os.system('clear')
    else:
        os.system('cls')

class TrisGame:
    
    def __init__(self) -> None: # <- inizziallizza la classe 
        try:
            o = open('winners_and_loosers.txt', 'r')
            o.close()
        except FileNotFoundError:
            o = open('winners_and_loosers.txt', 'w')
            o.write('Vincitori:          Perdenti:          ' + '\n')
            o.close()
    
    def run(self) -> None: # <- metodo di avvio del gioco 
        
        tr = TrisRequirements

        tr.grid_zone = []
        for l in tr.x:
            for n in tr.y:
                tr.grid[l+n] = ' '
                tr.grid_zone.append(l+n)
        
        tr.turn = 'X'
        tr.t = tr.player1
        tr.nt = tr.player2
        tr.trn = 0

        if tr.begin == False:
            read = input("Vuoi leggere l'elenco delle vittorie e sconfitte? s/n: ")
            if read == 's':
                o = open('winners_and_loosers.txt', 'r')
                lines = o.readlines()
                for line in lines:
                    print(line + '\n')
                o.close
            again = input('Vuoi uscire? s/n: ')
            if again == 's':
                raise StopAsyncIteration()
            elif again == 'n':
                self.menu()
            else:
                self.run()
        else:
            tr.begin = False
            self.menu()
            self.run()

    def menu(self): # <- game menù, selezione della modalità
      while True:  
        players = input('Seleziona il numero di giocatori: (1/2) ')
        if players == '1':
            self.SinglePlayer()
            break
        elif players == '2':
            self.Multiplayer()
            break
        else:
            print('Non possono esserci più di due giocatori, per giocare contro il computer scrivi "1", per giocare con un altra persona scrivi "2"')

    def test(self): # <- controlla se un player ha vinto 
        TrisRequirements.victory = 'F'
        for p in TrisRequirements.plyrs:
            for l in TrisRequirements.x:
                if TrisRequirements.grid[l+'1'] == TrisRequirements.grid[l+'2'] == TrisRequirements.grid[l+'3'] == p:
                    print('Ha vinto', TrisRequirements.t, 'complimenti!')
                    TrisRequirements.victory = 'T'
            for n in TrisRequirements.y:
                if TrisRequirements.grid['a'+n] == TrisRequirements.grid['b'+n] == TrisRequirements.grid['c'+n] == p:
                    print('Ha vinto', TrisRequirements.t, 'complimenti!')
                    TrisRequirements.victory = 'T'
            if TrisRequirements.grid['a1'] == TrisRequirements.grid['b2'] == TrisRequirements.grid['c3'] == p:
                print('Ha vinto', TrisRequirements.t, 'complimenti!')
                TrisRequirements.victory = 'T'
            elif TrisRequirements.grid['c1'] == TrisRequirements.grid['b2'] == TrisRequirements.grid['a3'] == p:
                print('Ha vinto', TrisRequirements.t, 'complimenti!')
                TrisRequirements.victory = 'T'

    def Print(self): # <- stampa la griglia aggiornata 

        print('Turno', str(TrisRequirements.trn))
        print('   a   b   c\n'
          '1 ', TrisRequirements.grid['a1'], '|', TrisRequirements.grid['b1'], '|', TrisRequirements.grid['c1'] + '\n'
          '  ---+---+---' + '\n'
          '2 ', TrisRequirements.grid['a2'], '|', TrisRequirements.grid['b2'], '|', TrisRequirements.grid['c2'] + '\n'
          '  ---+---+---' + '\n'
          '3 ', TrisRequirements.grid['a3'], '|', TrisRequirements.grid['b3'], '|', TrisRequirements.grid['c3'] + '\n')

    class SinglePlayer: # <- modalità single player 

        def __init__(self) -> None:
            self.run()
        
        def run(self): # <- avvia il gioco in single player 

            player1 = input('Inserisci il tuo nome: ')
            TrisRequirements.t = player1
            print('Ci sono vari livelli di difficoltà, selezionane uno:')
            time.sleep(0.1)
            print('Facile (F)')
            time.sleep(0.1)
            print('Medio (M)')
            time.sleep(0.1)
            print('Difficile (D)')
            time.sleep(0.1)
            print('Impossibile (I)')
            
            while True:

                choice = input('Scegli un livello: ')
                options = ['F', 'M', 'D', 'I']

                if choice in options:
                    TrisGame.SinglePlayer.LogicAdapters(choice,) #<- seleziona l'adattatore logico del caso
                    self.play(choice)
                    break
                else:
                    print('Inserisci "F", "M", "D" o "I".')

        def play(self, choice):

            '''
            options = {'F': self.LogicAdapters().Facile, 
                       'M':self.LogicAdapters().Medio, 
                       'D':self.LogicAdapters().Difficile, 
                       'I':self.LogicAdapters().Impossibile}'''

            if choice == 'D' or choice == 'I':

                print('Emulerò Filippo Bollito')
                starter = input("Chi inizia?\n1) Tu\n2) Io\n3) Casuale\n")
                if starter == '1':
                    TrisRequirements.starter = 'X'
                elif starter == '2':
                    TrisRequirements.starter = 'O'
                elif starter == '3':
                    TrisRequirements.starter = random.choice(TrisRequirements.plyrs)
                
                if TrisRequirements.starter == 'O':
                    print('Comincerò io')
                    pc = True
                else:
                    pc = False
                    print('Comincerai tu')
            else:

                print('Sceglierò casualmente chi comincerà')
                starter = random.choice(TrisRequirements.plyrs)
                if starter == 'X':
                    print('Comincerò io')
                    time.sleep(2)
                    pc = True
                else:
                    print('Comincerai tu')
                    time.sleep(2)
                    pc = False

            la = TrisGame.SinglePlayer.LogicAdapters.selected
            cls()

            TrisGame().Print()
            TrisRequirements.trn = 1

            while True: # <- inizio effrettivo gioco

                if pc == True:
                    la.response()
                    time.sleep(1)
                    pc = False
                else:
                    while True:
                        coordinates = input('Inserisci le coordinate della tua mossa (letteranumero): ')
                        if coordinates in TrisRequirements.grid:
                            if TrisRequirements.grid[coordinates] in TrisRequirements.plyrs:
                                print('Coordinate già inserite...')
                                pass
                            else:
                                TrisRequirements.grid[coordinates] = 'X'
                                TrisRequirements.grid_zone.remove(coordinates)
                                pc = True
                                break
                
                cls()
                TrisGame().Print()
                TrisGame().test()  

                if TrisRequirements.victory == 'T':
                    break
                else:
                    TrisRequirements.trn = TrisRequirements.trn + 1
                    if TrisRequirements.trn == 9:
                        print('Pareggio! Complimenti')               

        class LogicAdapters: #<- logica in base alla quale scegliere la mossa 
            
            def __init__(self, *args) -> None:

                if len(args) != 0:
                    if args[0] == 'F':
                        TrisGame.SinglePlayer.LogicAdapters.selected = TrisGame.SinglePlayer.LogicAdapters.Facile()
                    elif args[0] == 'M':
                        TrisGame.SinglePlayer.LogicAdapters.selected = TrisGame.SinglePlayer.LogicAdapters.Medio()
                    elif args[0] == 'D':
                        TrisGame.SinglePlayer.LogicAdapters.selected = TrisGame.SinglePlayer.LogicAdapters.Difficile()
                    elif args[0] == 'I':
                        TrisGame.SinglePlayer.LogicAdapters.selected = TrisGame.SinglePlayer.LogicAdapters.Impossibile()
                    else:
                        raise StopAsyncIteration()
                else:
                    print('no args')
                    raise StopAsyncIteration()

            class Facile: # <- selezione casuale della mossa

                def response(self):
                    computerF_move = random.choice(TrisRequirements.grid_zone)
                    TrisRequirements.grid[computerF_move] = 'O'
                    TrisRequirements.grid_zone.remove(computerF_move)
                    return True

            class Medio: # <- Quando può fa tris, impedisce all'altro di farlo, altrimenti gioca casualmente

                def response(self):
                    global computer_move
                    error = random.randrange(1,10)
                    computer_move = random.choice(TrisRequirements.grid_zone)
                    if error != 0:
                        TrisGame.SinglePlayer.LogicAdapters.Intelligent()
                    TrisRequirements.grid[computer_move] = 'O'
                    TrisRequirements.grid_zone.remove(computer_move)

            class Difficile: # <- gioca come Filippo Bollito

                def response(self):
                    global computer_move
                    
                    error = random.randrange(1,10)
                    computer_move = random.choice(TrisRequirements.grid_zone)
                    if TrisRequirements.starter == 'O':
                        if TrisRequirements.trn == 1:
                            computer_move = random.choice(TrisRequirements.grid_angles)
                        elif TrisRequirements.trn == 3:
                            for angle in TrisRequirements.grid_angles:
                                if TrisRequirements.grid[angle] == 'X' and TrisRequirements.grid[TrisRequirements.opposite_angles[angle]] == ' ':
                                    intelligent_grid_zones = tuple(TrisRequirements.grid_angles)
                                    intelligent_grid_zones = list(intelligent_grid_zones)
                                    intelligent_grid_zones.remove(TrisRequirements.opposite_angles[angle])
                                    for intelligent_move in intelligent_grid_zones:
                                        if TrisRequirements.grid[intelligent_move] == ' ':
                                            computer_move = intelligent_move
                                elif TrisRequirements.grid[angle] == 'X' and TrisRequirements.grid[TrisRequirements.opposite_angles[angle]] == 'O':
                                    for angle in TrisRequirements.grid_angles:
                                        if TrisRequirements.grid[angle] == ' ':
                                            computer_move = angle
                                    TrisRequirements.case = 1
                        elif TrisRequirements.trn == 5 and TrisRequirements.case == 1:
                            for angle in TrisRequirements.grid_angles:
                                if TrisRequirements.grid[angle] == ' ':
                                    computer_move = angle
                    elif TrisRequirements.starter == 'X':
                        if TrisRequirements.trn == 2 and TrisRequirements.grid['b2'] == ' ':
                            computer_move = 'b2'
                        elif TrisRequirements.trn == 4:
                            angle_letters = ('a', 'c')
                            angle_numbers = ('1', '3')
                            for l in angle_letters:
                                for n in angle_numbers:
                                    if TrisRequirements.grid[l+angle_numbers[angle_numbers.index(n)]] == TrisRequirements.grid[angle_letters[angle_letters.index(l)-1]+angle_numbers[angle_numbers.index(n)-1]] != ' ':
                                        intelligent_grid_zones = tuple(TrisRequirements.grid_zone)
                                        intelligent_grid_zones = list(intelligent_grid_zones)
                                        for angle in TrisRequirements.grid_angles:
                                            try:
                                                intelligent_grid_zones.remove(angle)
                                            except ValueError:
                                                pass
                                        computer_move = random.choice(intelligent_grid_zones)
                    if error != 0:
                        TrisGame.SinglePlayer.LogicAdapters.Intelligent()
                    TrisRequirements.grid[computer_move] = 'O'
                    TrisRequirements.grid_zone.remove(computer_move)
                    print(computer_move)

            class Impossibile: # <- gioca come FilippoBollito, ma senza errori di distrazione
                
                def __init__(self) -> None:
                    print('questo livello è ancora in fase sperimentale')
                    raise EOFError()

                def response(self):
                    global computer_move

                    grid_corners = ['a1', 'c1', 'a3', 'c3']
                    first_move = random.choice(grid_corners)
                    TrisRequirements.grid[first_move] = 'X'

            class Intelligent: # <- Trova la migliore mossa

                def __init__(self) -> None:
                    global computer_move

                    for symbol in TrisRequirements.plyrs:
                        for l in TrisRequirements.x:
                            column_zones = []
                            for n in TrisRequirements.y:
                                column_zones.append(l+n)
                            column_zones = tuple(column_zones)
                            for n in TrisRequirements.y:
                                test_column = list(column_zones)
                                test_column.remove(l+n)
                                if TrisRequirements.grid[test_column[0]] == TrisRequirements.grid[test_column[1]] == symbol and TrisRequirements.grid[l+n] == ' ':
                                    computer_move = l+n
                        for n in TrisRequirements.y:
                            line_zones = []
                            for l in TrisRequirements.x:
                                line_zones.append(l+n)
                            line_zones = tuple(line_zones)
                            for l in TrisRequirements.x:
                                test_line = list(line_zones)
                                test_line.remove(l+n)
                                if TrisRequirements.grid[test_line[0]] == TrisRequirements.grid[test_line[1]] == symbol and TrisRequirements.grid[l+n] == ' ':
                                    computer_move = l+n
                        diagonals = (('a1', 'b2', 'c3'), ('a3', 'b2', 'c1'))
                        for diagonal in diagonals:
                            for d in diagonal:
                                test_diagonal = list(diagonal)
                                test_diagonal.remove(d)
                                if TrisRequirements.grid[test_diagonal[0]] == TrisRequirements.grid[test_diagonal[1]] == symbol and TrisRequirements.grid[d] == ' ':
                                    computer_move = d            

    class Multiplayer: # <- modalità multiplayer 
    
      def __init__(self) -> None:

        tr  = TrisRequirements

        if tr.trn == 0:
            TrisGame().Print()
            tr.trn = 1

        print('La mossa è di', tr.t)
        print(tr.turn)
        coordinates = input('Inserisci le coordinate della tua mossa (letteranumero): ')
        if coordinates in tr.grid:
            print('si')
            if tr.grid[coordinates] in tr.plyrs:
                print('Coordinate già inserite...')
                TrisGame.Multiplayer()
            else:
                print(tr.turn, 'si')
                tr.grid[coordinates] = tr.turn
                cls()
                TrisGame().Print()
                TrisGame().test()
                if tr.victory == 'T':
                    o = open('winners_and_loosers.txt', 'a')
                    self.playersplayers = [tr.player1, tr.player2]
                    self.w_a_l = ('Vincitore: ' + tr.t, 'perdente: ' + tr.nt)
                    o.write(str(self.w_a_l) + '\n')
                    o.close()
                    TrisGame().run()
                else: 
                    if tr.turn == 'X':
                        tr.turn = 'O'
                        tr.t = tr.player2
                        tr.nt = tr.player1
                    else:
                        tr.turn = 'X'
                        tr.t = tr.player1
                        tr.nt = tr.player2
                    tr.trn = tr.trn + 1

                    if tr.trn == 10:
                        print('Pareggio! Complimenti a entrambi')
                        TrisGame().run()
                    else:
                        TrisGame.Multiplayer()
        else:
            print('Coordinate errate...')
            TrisGame.Multiplayer()

class TrisRequirements:
    def __init__(self) -> None:
        TrisRequirements.title = ' _____   ____   _   ____  \n/__ __\ /  __\ / \ / ___\ \n  / \   |  \/| | | |    \ \n  | |   |    / | | \___ | \n  \_/   \_/\_\ \_/ \____/ \nProgrammato da Filippo Bollito'
        TrisRequirements.grid = {'a1' : '-', 'b1' : '-', 'c1' : '-',
        'a2' : '-', 'b2' : '-', 'c2' : '-',
        'a3' : '-', 'b3' : '-', 'c3' : '-'}
        '''Game grid'''

        TrisRequirements.grid_angles = ('a1', 'a3', 'c1', 'c3')
        TrisRequirements.opposite_angles = {'a1' : 'c3', 'c1' : 'a3', 'a3' : 'c1', 'c3' : 'a1'}
        TrisRequirements.player1 = 'player1'
        TrisRequirements.player2 = 'player2'
        TrisRequirements.plyrs = ('X', 'O')
        '''Players symbols'''
        TrisRequirements.x = ['a', 'b', 'c']
        '''Columns'''
        TrisRequirements.y = ['1', '2', '3']
        '''Lines'''
        TrisRequirements.victory = 'F'
        TrisRequirements.turn = 'X'
        '''Symbol of the current turn player'''
        TrisRequirements.trn = 0
        '''Turn number'''
        TrisRequirements.grid_zone = []
        '''Zones in the game grid'''
        TrisRequirements.begin = True
        TrisRequirements.case = 0


# entry point
try:
    TrisRequirements() # <- inizziallizza la classe con le variabili

    print(TrisRequirements.title)# <- stampa il titolo
    time.sleep(3)
    cls()
    
    TrisGame().run()# <- avvia il gioco
except (StopAsyncIteration, KeyboardInterrupt):
    cls()
    print(TrisRequirements.title)
    exit()
except EOFError:
    TrisGame().run()
