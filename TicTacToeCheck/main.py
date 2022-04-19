import numpy as np
import random
import time


def generate_playboard(size):
    tab = np.random.choice(["*"], size=(size, size))
    return tab


def display_playborad(playboard):
    size = int(playboard.shape[0])
    playboard_string = ""
    for row in range(size):
        for column in range(size):
            playboard_string += playboard[row][column] + " "
        playboard_string += "\n"
    print(playboard_string)


def check_next(sign, counter, checked):
    if sign == checked and sign != "*":
        counter += 1
    elif checked == "*":
        counter = 0
    elif sign != checked and checked != "*":
        counter = 1
    return counter


def check_u(playboard, required):
    size = int(playboard.shape[0])
    run = True

    for column in range(size):
        counter = 0
        current_sign = playboard[0][0]

        for skos in range(2):
            for row in range(size - skos * column):
                checked = playboard[row][column + skos * row]
                counter = check_next(current_sign, counter, checked)
                current_sign = checked

                if counter == required:
                    run = False
                    print(current_sign + " wygral!")
                    break

        if run == False:
            return False


def check_l(playboard, required):
    size = int(playboard.shape[0])
    run = True

    for row in range(size):
        counter = 0
        current_sign = playboard[0][0]

        for skos in range(2):
            for column in range(size - skos * row):
                checked = playboard[row + skos * column][column]
                counter = check_next(current_sign, counter, checked)
                current_sign = checked

                if counter == required:
                    run = False
                    print(current_sign + " wygral!")
                    break

        if run == False:
            return False

def put_sign(board, size, sign):
    x = random.randrange(size)
    y = random.randrange(size)
    if board[x][y] == "*":
        board[x][y] = sign;
    else: put_sign(board, size, sign)



size = int(input("Jaka plansza wariacie? "))
required = int(input("Do ilu gramy? "))

if size < required:
    print("ty dzieciole")

else:
    board = generate_playboard(size)
    while True:
        put_sign(board, size, "X")
        if check_l(board, required) == False or check_u(board, required) == False:
            display_playborad(board)
            break
        put_sign(board, size, "O")
        if check_l(board, required) == False or check_u(board, required) == False:
            display_playborad(board)
            break
        display_playborad(board)
        time.sleep(0.1)
