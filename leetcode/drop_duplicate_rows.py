"""
There are some duplicate rows in the DataFrame based on the email column.

Write a solution to remove these duplicate rows and keep only the first occurrence.

The result format is in the following example.
"""

import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    customers = customers.drop_duplicates(subset='email')
    return customers   


"""
    To drop duplicate rows in a DataFrame in Python, we can use the 'drop_duplicates()' method provided by the pandas library. 

    Drop duplicated and keep the first occurence:
    df.drop_duplicates(inplace=True)

    Keep the last occurance instead: 
    df.drop_duplicates(inplace=True, keep='last')

    Drop duplicates based on specific columns: 
    df.drop_duplicates(subset=['column_name'])

    Drop duplicates based on all columns: 
    df.drop_duplicates()

    Drop duplicates and reset index: 
    df.drop_duplicates(inplace=True).reset_index(drop=True)
"""