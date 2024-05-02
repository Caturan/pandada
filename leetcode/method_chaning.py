"""
    Write a solution to list the names of animals that weigh strictly more than 100 kilograms.
    Return the animals sorted by weight in descending order.
"""

import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    result = animals[animals['weight'] > 100].sort_values(by='weight', ascending=False)['name']
    result_df = pd.DataFrame(result)
    return result_df 

"""
    In Pandas, method chaining enables us to perform operations on a DataFrame without breaking up each operation into a separate line or creating multiple temporary variables. 
"""