import tkinter as tk
import string
import random
from tkinter import messagebox


def createMatrix():
    global letters
    letters = list(string.ascii_lowercase[:16])# ограничение алфавита от 'a' до 'p'

    random.shuffle(letters);print(letters)
    print(sorted(letters))# перемешиваем буквы случайным образом
    for i in range(4):
        for j in range(4):
            letter = letters[i * 4 + j]
            matrixLabels[i][j].config(text=letter)


def checkAlphabeticalOrder():
    global letters
    if sorted(letters) == letters:
        messagebox.showinfo("Алфавитный порядок", "Буквы расположены в алфавитном порядке: 123")
    else:
        messagebox.showinfo("Алфавитный порядок", "Буквы не расположены в алфавитном порядке")


def rotateSubmatrix(indices):
    global letters
    temp_values = []
    temp_indices = []
    for index in indices:
        row, col = index2RowCol(index)
        label = matrixLabels[row][col]
        temp_values.append(label["text"])
        temp_indices.append(index)

    # поворот субматрицы по часовой стрелке на одну клетку
    if len(temp_values) == 4:
        temp_values = [temp_values[2], temp_values[0], temp_values[3], temp_values[1]]

    # обновление лейблов
    for i, index in enumerate(temp_indices):
        row, col = index2RowCol(index)
        label = matrixLabels[row][col]
        label.config(text=temp_values[i])

    # обновление списка letters
    for i, index in enumerate(temp_indices):
        letters[index - 1] = temp_values[i]

    print(letters)

def index2RowCol(index):
    row = (index - 1) // 4
    col = (index - 1) % 4
    return row, col


def updateMatrix():
    createMatrix()


def replace():
    #global replace_called
    #if not replace_called:
        index1 = int(textbox1.get())
        index2 = int(textbox2.get())

        row1, col1 = index2RowCol(index1)
        row2, col2 = index2RowCol(index2)

        # свап лейблов
        temp = matrixLabels[row1][col1]["text"]
        matrixLabels[row1][col1].config(text=matrixLabels[row2][col2]["text"])
        matrixLabels[row2][col2].config(text=temp)

        # свап элементов в letters
        index1_value = letters[index1 - 1]
        index2_value = letters[index2 - 1]
        letters[index1 - 1] = index2_value
        letters[index2 - 1] = index1_value

        print(letters)

    # выключение кнопки замена


        replaceButton.config(state=tk.DISABLED)


root = tk.Tk()
root.title("Matrix 4x4")

matrixLabels = []
for i in range(4):
    rowLabels = []
    for j in range(4):
        label = tk.Label(root, text='', padx=10, pady=5)
        label.grid(row=i, column=j)
        rowLabels.append(label)
    matrixLabels.append(rowLabels)

createMatrix()

buttonFrame = tk.Frame(root)
buttonFrame.grid(row=4, columnspan=4)

# индекмы матрицы для кнопок 
buttonIndices = [
    [5, 1, 6, 2],
    [6, 2, 7, 3],
    [7, 3, 8, 4],
    [9, 5, 10, 6],
    [10, 6, 11, 7],
    [11, 7, 12, 8],
    [13, 9, 14, 10],
    [14, 10, 15, 11],
    [15, 11, 16, 12]
]

# кнопки1-9
for i, indices in enumerate(buttonIndices):
    button = tk.Button(buttonFrame, text=str(i + 1), command=lambda indices=indices: rotateSubmatrix(indices))
    button.grid(row=i // 3, column=i % 3, padx=10, pady=5)

# геометрия текстбоксов
textboxFrame = tk.Frame(root)
textboxFrame.grid(row=5, columnspan=4, pady=10)

textbox1Label = tk.Label(textboxFrame, text="Index 1:")
textbox1Label.grid(row=0, column=0)

textbox1 = tk.Entry(textboxFrame)
textbox1.grid(row=0, column=1, padx=5)

textbox2Label = tk.Label(textboxFrame, text="Index 2:")
textbox2Label.grid(row=0, column=2)

textbox2 = tk.Entry(textboxFrame)
textbox2.grid(row=0, column=3, padx=5)

replaceButton = tk.Button(textboxFrame, text="Замена", command=replace)
replaceButton.grid(row=0, column=4, padx=5)
# вызовв замены
replaceCalled = False

checkButton = tk.Button(root, text="Проверка", command=checkAlphabeticalOrder)
checkButton.grid(row=0, column=5)

root.mainloop()
