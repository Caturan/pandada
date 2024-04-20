"""
    Write a solution to calculate and display the number of rows and columns of players.

    Return the result as an array:
"""

import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    x = players.player_id.count()
    k = int(x)
    
    a = players.columns
    s = len(a)
    y = [k,s]
    return y


