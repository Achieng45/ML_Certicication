# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[]):
    if prev_play in ["R","P","S"]:
        opponent_history.append(prev_play)
    counter_moves={"R":"P","P":"S","S":"R"}
    if len(opponent_history)==0:
        return "R"
    
    most_common_move=max(set(opponent_history),key=opponent_history.count)
    return counter_moves.get(most_common_move,"R")
    # guess = "R"
    # if len(opponent_history) > 2:
    #     guess = opponent_history[-2]

    # return guess
