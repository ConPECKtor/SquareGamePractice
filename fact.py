from tkinter import Tk, Canvas, HIDDEN, NORMAL
from time import sleep
from random import randint


colors = ['red', 'yellow', 'green', 'black', 'grey', 'pink', 'blue']
currentTime = 1000
currentAttempt = 0

p1Points = 0
p2Points = 0

root = Tk()
canvas = Canvas(root, width=400, height=400)
canvas.pack()

square = None

def cutTime(currTime):
    return currTime - 150

def createFigure():
    return canvas.create_rectangle(35, 20, 365, 350, width=15, outline=colors[randint(0, len(colors) - 1)], fill=colors[randint(0, len(colors) - 1)]) # Создание квадрата

def gameTick():
    global currentAttempt, square, currentTime


    if (currentAttempt >= 30):
        print(f'Конец! Счёт P1 = {p1Points}, P2 = {p2Points}')
        return
    if square:
        canvas.delete(square)
    square = createFigure()

    root.after(currentTime, gameTick)
    currentAttempt += 1
    if (currentAttempt % 5 == 0):
        currentTime = cutTime(currentTime)



def delete(event):
    global p1Points, p2Points

    fillСolor = canvas.itemcget(square, 'fill')
    outlineСolor = canvas.itemcget(square, 'outline')

    if not canvas.find_withtag(square):
        return

    canvas.delete(square)

    if fillСolor != outlineСolor:
        return
        
    if event.char == 'q':
        p1Points += 1
    else:
        p2Points += 1

canvas.bind('q', delete) 
canvas.bind('p', delete) 


canvas.focus_set()

gameTick()

root.mainloop() 
