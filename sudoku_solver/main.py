import tkinter as tk
import numpy as np
from sudoku import Sudoku

root = tk.Tk()
root.title("Sudoku Solver")
root.geometry("500x500")  

label = tk.Label(root, text="Sudoku Solver!", font=("Arial", 16))
label.pack(pady=20)


allfeild = {}
#  for margin for 3x3 box
g = 0
gap = 20
for i in range(0,9):
    gapy = 0
    if i == 3 or i == 6:
        g += gap
    for j in range(0,9):
        if j == 3 or j == 6:
            gapy += gap
        allfeild[(i,j)] = tk.Entry(root,font=('Arial',16),width=2)
        allfeild[(i,j)].place(x=((i*30))+100+g,y=(j*(30))+100+gapy)


def clear(fnc):
    for i in range(0,9):
        for j in range(0,9):
            entry = allfeild[(i,j)]
            entry.delete(0,tk.END)
            fnc(entry,i,j)

def on_click():
    data = np.array([0 for _ in range(81)]).reshape((9,9))
    for key,value in allfeild.items():
        i,j = key
        v = value.get()
        v = int(v) if v else 0
        data[i][j] = v
    puzzle = Sudoku(data)
    solution = puzzle.get_solution()
    clear(lambda entry,i,j:entry.insert(0,str(solution[i][j])))
    # for i in range(0,9):
    #     for j in range(0,9):
    #         entry = allfeild[(i,j)]
    #         entry.delete(0,tk.END)
    #         entry.insert(0,str(solution[i][j]))


button = tk.Button(root, text="Solve", command=on_click)
button.pack()
button = tk.Button(root, text="Clear", command=lambda :clear(lambda x,y,z:None))
button.place(y=50)

# Run the application
root.mainloop()
