"""
Write a solution to create a DataFrame from a 2D list called student_data. This 2D list contains the IDs and ages of some students.

The DataFrame should have two columns, student_id and age, and be in the same order as the original 2D list.
"""


import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    list1 = []
    list2 = []
    for row in student_data:
        list1.append(row[0])
        list2.append(row[1])
    df = pd.DataFrame(
        {
        "student_id": list1,
        "age": list2,  
        }
    )
    return df 