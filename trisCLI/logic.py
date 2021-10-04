# classe per la logica
import json, os

class Logic:
    
    def __init__(self, *args) -> None:
        self.data = Data().get()
        self.grid = []
        self.move = 'b2'

        for i in range(1, 10):
            self.grid.append(i)
        
        self.grid_corners = [1, 3, 7, 9]
        self.opposites = [[1,9][7,3]]
        self.center = 5

        try:
            self.turn = args[0]
        except (IndexError, AttributeError):
            self.turn = None

        self.preprocess()

    def preprocess(self):
        
        self.first_move = self.data['first_move']
        self.percentrate = 0.0
        self.stimate = []

        if self.first_move != {}:
            for i in self.first_move:
                self.stimate.append([i, self.first_move[i]])
        else:
            pass

        self.AI()

    def calculate(self):

        for i in self.stimate:
            if i[0] == self.move:
                self.percentrate += 1.0
                
    def AI(self):
        self.covert = {'a1':1, 'b1':2, 'c1':3,
                       'a2':4, 'b2':5, 'c2':6,
                       'a3':7, 'b3':8, 'c3':9}
        
        self.move = self.covert[self.move]
        self.grid.pop(self.grid.index(self.move))

        if self.move == self.center:
            self.next = self.grid_corners
        else:
            self.next = self.grid
        
        for i in self.next:
            if i in self.grid and i in self.grid_corners:
                for o in self.opposites:
                    if i in o:
                        o.pop(i)
                        self.cp_move = o[0]

class Data:
    PATH = os.path.dirname(__file__)

    def get(self):
        self.data = json.load(open(os.path.join(self.PATH, 'db.json')))
        return self.data

Logic()
