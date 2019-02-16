"""
The team.py file is where you should write all your code!

Write the __init__ and the step functions. Further explanations
about these functions are detailed in the wiki.

List your Andrew ID's up here!
jaabrams
ztlee
dsalgado
"""
from awap2019 import Tile, Direction, State
from random import randint, shuffle

MOVES = [Direction.UP, Direction.LEFT, Direction.RIGHT, Direction.DOWN]

def access(board, loc):
    try:
        return board[loc[0]][loc[1]]
    except Exception:
        return None

def select_move(board, state, visits):
    shuffle(MOVES)

    if state.line_pos != -1:
        return Direction.NONE

    x = state.x
    y = state.y
    tile = board[x][y]
    if tile.is_end_of_line():
        visits[tile.get_line()] += 1
        return Direction.ENTER

    if state.dir != Direction.NONE:
        return state.dir    


    for dir in MOVES:
        loc = (x, y)
        new_loc = dir.get_loc(loc)
        min_visits = min(visits.values())

        new_tile = access(board, new_loc)
        if new_tile and new_tile.is_end_of_line():
            # if visits[new_tile.get_line()] - min_visits <= 2:
            return dir


    for dir in MOVES:
        loc = (x, y)
        new_loc = dir.get_loc(loc)

        if access(board, new_loc) and access(board, new_loc).get_booth() == None and access(board, new_loc).get_line() == None:
            return dir


class Team(object):
    def __init__(self, initial_board, team_size, company_info):
        """
        The initializer is for you to precompute anything from the
        initial board and the company information! Feel free to create any
        new instance variables to help you out.

        Specific information about initial_board and company_info are
        on the wiki. team_size, although passed to you as a parameter, will
        always be 4.
        """
        self.board = initial_board
        self.team_size = team_size
        self.company_info = company_info

        self.team_name = "Dilhan and friends"
        self.visited = {}
        for i in company_info.keys():
            self.visited[i] = 0

    def step(self, visible_board, states, score):
        """
        The step function should return a list of four Directions.

        For more information on what visible_board, states, and score
        are, please look on the wiki.
        """
        out = []
        for i in range(4):
            out.append(select_move(visible_board, states[i], self.visited))

        return out  
