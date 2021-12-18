#!/usr/bin/env python3

import sys
sys.path.append('../')
from common.readinput import read_filename

# Parse fixed width boards - evenly spaced in groups of 3
def chunkstring(string):
    if len(string) < 2:
        return []

    parsed = []
    chunksize = 3
    for i in range(0, len(string), chunksize):
        parsed.append(int(string[i:i+chunksize].strip()))
    return parsed

def parse_boards(lines):
    boards = []
    board = []

    for line in lines:
        numbers = chunkstring(line)

        if len(numbers) > 1:
            board.append(numbers)
        else:
            if len(board) > 0:
                boards.append(board)
                board = []

    # No ending new line, so grab last board
    if len(board) > 0:
        boards.append(board)

    return boards

def build_scoreboard(boards):
    scoreboard = []
    for _ in range(len(boards)):
        board = [[0 for _ in range(5)] for _ in range(5)]
        scoreboard.append(board)

    return scoreboard

def check_number(draw, boards, scoreboard):
    for board_index, board in enumerate(boards):
        for row_number, row in enumerate(board):
            for index, number in enumerate(row):
                if number == draw:
                    mark_scoreboard(board_index, row_number, index, scoreboard)


def mark_scoreboard(board_index, row_index, index, scoreboard):
    board = scoreboard[board_index]
    row = board[row_index]
    row[index] = 1


def check_for_winning_board(scoreboard):
    for board_index, board in enumerate(scoreboard):
        if check_for_winning_row(board):
            return board_index

        transposed = [list(row) for row in zip(*board)]
        if check_for_winning_row(transposed):
            return board_index

    return None

def check_for_winning_row(board):
    for row in board:
        if sum(row) == 5:
            return True

    return False


def sum_unselected_numbers(board, board_score):
    un_marked = [[x if y==0 else 0 for x,y in zip(r1,r2)] for r1, r2 in zip(board, board_score)]
    print(un_marked)
    return sum([sum(x) for x in un_marked])

def main():
    filename = read_filename()

    with open(filename) as f:
        drawn_numbers = [int(n.strip()) for n in f.readline().split(',')]
        boards = parse_boards(f.readlines())
        scoreboard = build_scoreboard(boards)

        print(f"Drawn Numbers: {drawn_numbers}")
        print(f"Boards: {boards}")
        print(f"Scoreboard: {scoreboard}")

        winning_number = None
        winning_board_index = None
        for number in drawn_numbers:
            print(f"checking {number}")
            check_number(number, boards, scoreboard)
            winning_board_index = check_for_winning_board(scoreboard)
            if winning_board_index != None:
                winning_number = number
                break


        winning_board = boards[winning_board_index]
        winning_score = scoreboard[winning_board_index]
        print(f"Winning number: {winning_number}")
        print(f"Final Score: {scoreboard}")
        print(f"Winning Board {winning_board_index}:\n{winning_board}\n{winning_score}")

        unmarked_sums = sum_unselected_numbers(winning_board, winning_score)
        print(f"Sum of unmarked: {unmarked_sums}")

        final_value = unmarked_sums * winning_number
        print(f"Final value: {final_value}")




main()

