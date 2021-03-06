from board import my_board, print_board, board_keys


def game():

    turn = 'X'
    count = 0

    for i in range(10):
        print_board(my_board)
        print("It's your turn," + turn + ".Move to which place?")

        move = input()

        if my_board[move] == " ":
            my_board[move] = turn
            count += 1
        else:
            print("That place is already taken.\nMove to which place? ")
            continue

        # check if player X or O has won,for every move after 5 moves.
        if count >= 5:
            if my_board['7'] == my_board['8'] == my_board['9'] != ' ':  # across the top
                print_board(my_board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif my_board['4'] == my_board['5'] == my_board['6'] != ' ':  # across the middle
                print_board(my_board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif my_board['1'] == my_board['2'] == my_board['3'] != ' ':  # across the bottom
                print_board(my_board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif my_board['1'] == my_board['4'] == my_board['7'] != ' ':  # down the left side
                print_board(my_board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif my_board['2'] == my_board['5'] == my_board['8'] != ' ':  # down the middle
                print_board(my_board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif my_board['3'] == my_board['6'] == my_board['9'] != ' ':  # down the right side
                print_board(my_board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif my_board['7'] == my_board['5'] == my_board['3'] != ' ':  # diagonal
                print_board(my_board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif my_board['1'] == my_board['5'] == my_board['9'] != ' ':  # diagonal
                print_board(my_board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break

        # IF neither X nor 0 wins and the board if full, we'll declare the result as tie.
        if count == 9:
            print("\nGame Over.\n")
            print("It's a Tie!!")

        # Change player after every move.
        if turn == "X":
            turn = "O"
        else:
            turn = 'X'

    restart = input("Do you want to play again?(y/n)")
    if restart in 'yY':
        for key in board_keys:
            my_board[key] = " "

        game()


if __name__ == "__main__":
    game()
