"""
        +-------------+---------+
    | Column Name | Type    |
    +-------------+---------+
    | id          | int     |
    | name        | varchar |
    +-------------+---------+
    id is the primary key (column with unique values) for this table.
    Each row of this table indicates the ID and name of a customer.

    Table: Orders

    +-------------+------+
    | Column Name | Type |
    +-------------+------+
    | id          | int  |
    | customerId  | int  |
    +-------------+------+
    id is the primary key (column with unique values) for this table.
    customerId is a foreign key (reference columns) of the ID from the Customers table.
    Each row of this table indicates the ID of an order and the ID of the customer who ordered it.

    Write a solution to find all customers who never order anything.

    Return the result table in any order.

    Example 1:

    Input: 
    Customers table:
    +----+-------+
    | id | name  |
    +----+-------+
    | 1  | Joe   |
    | 2  | Henry |
    | 3  | Sam   |
    | 4  | Max   |
    +----+-------+
    Orders table:
    +----+------------+
    | id | customerId |
    +----+------------+
    | 1  | 3          |
    | 2  | 1          |
    +----+------------+
    Output: 
    +-----------+
    | Customers |
    +-----------+
    | Henry     |
    | Max       |
    +-----------+
"""
import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    ortak = pd.merge(customers, orders, left_on='id', right_on='customerId', how='left')
    ortak_olmayan = ortak[ortak['customerId'].isnull()]
    ortak_olmayan = ortak_olmayan.rename(columns={'name': 'Customers'})
    output = ortak_olmayan[['Customers']]
    return output 