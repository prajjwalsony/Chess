#ALL Tested
import pandas as pd
import numpy as np
df=pd.read_csv("database.csv")

#sample data = 1234,"[{'k': 'e1', 'q': 'd1', 'b1': 'c1', 'b2': 'f1', 'h1': 'b1', 'h2': 'g1', 'r1': 'a1', 'r2': 'h1', 'p1': 'a2', 'p2': 'b2', 'p3': 'c2', 'p4': 'd2', 'p5': 'e2', 'p6': 'f2', 'p7': 'g2', 'p8': 'h2'}, {'k': 'e8', 'q': 'd8', 'b1': 'c8', 'b2': 'f8', 'h1': 'b8', 'h2': 'g8', 'r1': 'a8', 'r2': 'h8', 'p1': 'a7', 'p2': 'b7', 'p3': 'c7', 'p4': 'd7', 'p5': 'e7', 'p6': 'f7', 'p7': 'g7', 'p8': 'h7'}, 'w']"


def getData(id):
    return (df.loc[df['id'] == id, 'data']).iloc[0]


test_data=[{'k':'e1', 'q':'d1','b1':'c1', 'b2':'f1', 'h1':'a2', 'h2':'g1', 'r1':'a1', 'r2':'h1', 'p1':'a2', 'p2':'b2', 'p3':'c2', 'p4':'d2', 'p5':'e2', 'p6':'f2', 'p7':'g2', 'p8':'h2'},
    {'k':'e8', 'q':'d8','b1':'c8', 'b2':'f8', 'h1':'b8', 'h2':'g8', 'r1':'a8', 'r2':'h8', 'p1':'a7', 'p2':'b7', 'p3':'c7', 'p4':'d7', 'p5':'e7', 'p6':'f7', 'p7':'g7', 'p8':'h7'},
    'w']


def createData(id):
    lst=[{'k':'e1', 'q':'d1','b1':'c1', 'b2':'f1', 'h1':'a2', 'h2':'g1', 'r1':'a1', 'r2':'h1', 'p1':'a2', 'p2':'b2', 'p3':'c2', 'p4':'d2', 'p5':'e2', 'p6':'f2', 'p7':'g2', 'p8':'h2'},
    {'k':'e8', 'q':'d8','b1':'c8', 'b2':'f8', 'h1':'b8', 'h2':'g8', 'r1':'a8', 'r2':'h8', 'p1':'a7', 'p2':'b7', 'p3':'c7', 'p4':'d7', 'p5':'e7', 'p6':'f7', 'p7':'g7', 'p8':'h7'},
    'w']
    new_row={'id':id, 'data':str(lst)}
    df_new = df._append(new_row, ignore_index=True)
    df_new.to_csv('database.csv', index=False)


def modifyData(id, data):
    df.loc[df['id'] == id, 'data'] = str(data)
    df.to_csv('database.csv', index=False)

# print(createData(1236))

