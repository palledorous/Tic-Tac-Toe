from tic_tac_toe.board import Board
from tic_tac_toe.player import Player
from tic_tac_toe.views import CommandLineBoardPresenter
from tic_tac_toe.user_messages import UserMessages
from tic_tac_toe.printer import Printer
from tic_tac_toe.errors import (
    Errors,
    InvalidBoardIndexError,
    InputNotNumericError,
    PositionAlreadyTakenError,
)


def run():
    board = Board()
    player = Player(token=["X", "O"])
    view = CommandLineBoardPresenter()
    printer = Printer()
    user_messages = UserMessages(printer)
    errors = Errors(printer)

    user_messages.countdown()

    user_messages.logo()

    user_messages.instructions_option()

    if player.get_input() == 0:
        user_messages.display_instructions()
        view.display_board(board, printer)
    else:
        view.display_board(board, printer)
        user_messages.whos_turn(player, board)

    while not board.game_over():
        try:
            selection = player.get_input()
            board.turn(selection, player)
        except InputNotNumericError:
            errors.input_not_numeric_error_message()
        except InvalidBoardIndexError:
            errors.invalid_board_index_error_message()
        except PositionAlreadyTakenError:
            errors.position_already_taken_error_message()
        finally:
            view.display_board(board, printer)
            if not board.win() and not board.tie():
                user_messages.whos_turn(player, board)

    if board.win():
        user_messages.who_won(board)

    if board.tie():
        user_messages.its_a_tie()
