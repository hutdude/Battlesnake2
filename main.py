# Welcome to
# __________         __    __  .__                               __
# \______   \_____ _/  |__/  |_|  |   ____   ______ ____ _____  |  | __ ____
#  |    |  _/\__  \\   __\   __\  | _/ __ \ /  ___//    \\__  \ |  |/ // __ \
#  |    |   \ / __ \|  |  |  | |  |_\  ___/ \___ \|   |  \/ __ \|    <\  ___/
#  |________/(______/__|  |__| |____/\_____>______>___|__(______/__|__\\_____>
#
# This file can be a nice home for your Battlesnake logic and helper functions.
#
# To get you started we've included code to prevent your Battlesnake from moving backwards.
# For more info see docs.battlesnake.com


import random
import typing
import sys


# info is called when you create your Battlesnake on play.battlesnake.com
# and controls your Battlesnake's appearance
# TIP: If you open your Battlesnake URL in a browser you should see this data
def info() -> typing.Dict:
    print("INFO")

    return {
        "apiversion": "1",
        "author": "",  # TODO: Your Battlesnake Username
        "color": "#888888",  # TODO: Choose color
        "head": "default",  # TODO: Choose head
        "tail": "default",  # TODO: Choose tail
    }


# start is called when your Battlesnake begins a game
def start(game_state: typing.Dict):
    print("GAME START")


# end is called when your Battlesnake finishes a game
def end(game_state: typing.Dict):
    print("GAME OVER\n")
    
def getHeuristic(gameState):
    # Make sure you prevent your Battlesnake from...
    #   - moving backwards
    #   - moving out of bounds
    #   - colliding with itself
    #   - colliding with other Battlesnakes
    
    opponents = game_state['board']['snakes']
    my_body = game_state['you']['body']
    board_width = game_state['board']['width']
    board_height = game_state['board']['height']
    food = gameState['board']['food']
    
       
    return(value)    

def isTerminal(gameState):
    # returns true if gameState represents a state that would be the end of the game
    # this can include:
    #   1. One of the players has won the game
    #   2. The game has ended in a draw
    #   3. 
    
    return True

def minimax(gameState, depth, maximizingPlayer):
    if depth == 0 or isTerminal(gameState):
        return getHeuristic(gameState)
    if maximizingPlayer: 
        value  = float('-inf')
        bestMove = None
        for each in ["up", "down", "left", "right"]:
            newState = gameState.apply(move_option)
            minimaxResults = minimax(newState, depth-1, False)
            if minimaxResults[0] > value:  # compare value of returned minimax function with currently stored value
                value, bestMove = minimaxResults
        return (value, best_move)
    else: # minimizing player
        value = float('inf')
        bestMove = None
        for each in ["up", "down", "left", "right"]:
            newState = gameState.apply(move_option)
            minimaxResults = minimax(newState, depth-1, False)
            if minimaxResults[0] < value:  # compare value of returned minimax function with currently stored value
                value, bestMove = minimaxResults
        return (value, best_move)


# move is called on every turn and returns your next move
# Valid moves are "up", "down", "left", or "right"
# See https://docs.battlesnake.com/api/example-move for available data
def move(game_state: typing.Dict) -> typing.Dict:

    is_move_safe = {"up": True, "down": True, "left": True, "right": True}


    # Are there any safe moves left?
    safe_moves = []
    for move, isSafe in is_move_safe.items():
        if isSafe:
            safe_moves.append(move)

    if len(safe_moves) == 0:
        print(f"MOVE {game_state['turn']}: No safe moves detected! Moving down")
        return {"move": "down"}


    confidence = 0  # stores the value of the heuristic function of the chosen move that is returned from minimax
    confindence, next_move = minimax(game_state, 1, True)

    print(f"MOVE {game_state['turn']}: {next_move}")
    return {"move": next_move}


# Start server when `python main.py` is run
if __name__ == "__main__":
    from server import run_server
    port = "8000"
    for i in range(len(sys.argv) - 1):
        if sys.argv[i] == '--port':
            port = sys.argv[i+1]

    run_server({"info": info, "start": start, "move": move, "end": end, "port": port})
