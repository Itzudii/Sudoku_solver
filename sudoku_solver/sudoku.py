import numpy as np

class Sudoku:
    def __init__(self,array):
        self.orignal = array
        self.board = np.array(self.orignal)

    def norepeat(self,array): 
        array = array.flatten()   
        array = np.sort(array)
        prev = 0
        for i in array:
            if i == prev and prev != 0:
                return False
            prev = i
        return True
    
    def check(self,index):
        getcorn = lambda X:(X//3)*3
        x,y = index
        row = self.board[x,:]
        col = self.board[:,y]
        x, y = getcorn(x),getcorn(y)
        return self.norepeat(row) and self.norepeat(col) and self.norepeat(self.board[x:x+3,y:y+3])
    
    def nextempty(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return (i,j)
        return None
    
    def backT(self):
        empty = self.nextempty()
        if not empty:
            return True
        x,y = empty

        for i in range(1,10):
            self.board[x][y] = i
            if self.check((x,y)):
                if self.backT():
                    return True

            self.board[x][y] = 0
        return False
    
    def get_solution(self):
        self.backT()
        return self.board

    
if __name__ == '__main__':
    data = np.array([0 for j in range(1,82)]).reshape((9,9))

    puzzle = Sudoku(data)
    print(puzzle.get_solution())