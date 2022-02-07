# глобальные константы
CROSS = "X"
NOUGHT = "O"
EMPTY = " "
LOCK = "LOCK"
CELLS_TOTAL = 26


def display_instructions():
    """Выводится инструкция к игре на экран"""
    print(
        """
        Добро пожаловать на игру «Обратные крестики-нолики» на поле 5 x 5.
        В игре действует правило «Пять в ряд» – проигрывает тот, 
        у кого получился вертикальный, горизонтальный или диагональный ряд из пяти своих фигур (крестиков/ноликов).
        Игра работает в режиме «человек против компьютера».
        Чтобы сделать ход, введи число от 1 до 25. 
        Числа однозначно соотвествуют полям доски - так, как показано ниже:

                           1 | 2 | 3 | 4 | 5
                           ------------------
                           6 | 7 | 8 | 9 | 10
                           ------------------
                           11| 12| 13| 14| 15
                           ------------------
                           16| 17| 18| 19| 20
                           ------------------
                           21| 22| 23| 24| 25
                           
                            Интересной игры!\n
       """
    )


def yes_no_question(question):
    """
    Задаётся вопрос с ответом 'Да' или 'Нет'
    :param question: текст вопроса
    :return: текст ответа
    """
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response


def ask_number(question, bottom, top):
    """
    Вводится число из указанного диапазона
    :param question: текст вопроса
    :param bottom: нижняя граница диапазона
    :param top: верхняя граница диапазона
    :return: целое число ответа
    """
    response = None
    while response not in range(bottom, top):
        try:
            response = int(input(question))
        except ValueError:
            print('Ошибка ввода. Попробуй ещё.')
    return response


def turn_to_go():
    """
    Определяется принадлежность перового хода
    :return: символы для каждого игрока
    """
    go_first = yes_no_question("Хочешь ходить первым? (y, n): ")
    if go_first == "y":
        print("\nПервым ходишь ты. Ты играешь крестиками.")
        human = CROSS
        computer = NOUGHT
    else:
        print("\nПервым ходит компьютер. Ты играешь ноликами.")
        computer = CROSS
        human = NOUGHT
    return computer, human


def new_board():
    """
    Создаётся новая игровая доска
    """
    board = []
    for cell in range(CELLS_TOTAL):
        board.append(EMPTY)
    return board


def display_board(board):
    """
    Отрисовывается игровая доска на экране
    """
    print("---------------------")
    for i in range(5):
        print("|", board[1 + i * 5], "|", board[2 + i * 5], "|", board[3 + i * 5], "|", board[4 + i * 5], "|",
              board[5 + i * 5], "|")
        print("---------------------")


def open_moves(board):
    """
    Создаётся список доступных ходов
    """
    moves = []
    for cell in range(CELLS_TOTAL):
        if board[cell] == EMPTY:
            moves.append(cell)
    return moves


def strike(board):
    """
    Определяется поражение в игре
    """
    WAYS_TO_STRIKE = ((1, 2, 3, 4, 5),
                      (6, 7, 8, 9, 10),
                      (11, 12, 13, 14, 15),
                      (16, 17, 18, 19, 20),
                      (21, 22, 23, 24, 25),
                      (1, 7, 13, 19, 25),
                      (5, 9, 13, 17, 21),
                      (1, 6, 11, 16, 21),
                      (2, 7, 12, 17, 22),
                      (3, 8, 13, 18, 23),
                      (4, 9, 14, 19, 24),
                      (5, 10, 15, 20, 25))

    for row in WAYS_TO_STRIKE:
        if board[row[0]] == board[row[1]] == board[row[2]] == board[row[3]] == board[row[4]] != EMPTY:
            strike_ = board[row[0]]
            return strike_
        if EMPTY not in board:
            return LOCK
    # return None


def human_move(board, human):
    """
    Определяется ход человека
    """
    open_move = open_moves(board)
    move = None
    while move not in open_move:
        move = ask_number("Твой ход. Выбери одно из полей (1 - 25): ", 1, CELLS_TOTAL)
        if move not in open_move:
            print("\nЭто поле уже занято. Выбери другое.\n")
    print("Ход принят.")
    return move


def computer_move(board, computer, human):
    """
    Определяется ход компьютера
    """
    # список ходов
    MOVES_AVAILABLE = [11, 20, 22, 2, 17, 8, 10, 25, 7, 19, 13, 14, 18, 4, 23, 5, 6, 15, 12, 1, 16, 21, 24, 3, 9]

    print("Ход компьютера. Поле номер ", end=" ")

    for move in MOVES_AVAILABLE:
        if move in open_moves(board):
            print(move)
            return move


def next_turn(turn):
    """
    Осуществляется переход хода
    """
    if turn == CROSS:
        return NOUGHT
    else:
        return CROSS


def find_striker(striker, computer, human):
    """
    Определяется исход игры
    :return: выводится сообщение об исходе
    """
    if striker != LOCK:
        print("Пять", striker, "в ряд\n")
    else:
        print("Ничья\n")
    if striker == computer:
        print("Поздравляю! Ты победил!")
    elif striker == human:
        print("Победа компьютера.")
    elif striker == LOCK:
        print("Ничья.")


def main():
    # вывод инструкций
    display_instructions()
    # определение символов для каждого игрока
    computer, human = turn_to_go()
    turn = CROSS
    # отрисовка доски на экране
    board = new_board()
    display_board(board)
    while not strike(board):
        if len(open_moves(board)) == 1:
            print('Ходы закончились.\nНичья.')
            break
        elif turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        # переход хода
        turn = next_turn(turn)
    striker = strike(board)
    find_striker(striker, computer, human)


# запуск программы
main()
input("Нажмите Enter, чтобы выйти.")
