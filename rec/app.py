import numpy as np
import pandas as pd

movies=pd.read_csv('rec/movies.csv')
# print(movies.head(5))
print("we have listed a few genres \n 1.Adventure\n2.Horror\n3.Comedy\n4.Sci-fi\n5.Action\n6.Romatic\n7.Crime\n8.Mystery\n9.Fantasy\n10.Inspirational\n11.Musical")
rec=input("enetr the genre you wish to watch-->")
if(rec=="Adventure" or rec=="adventure"):
    data=movies.iloc[0:15].values
    print(data)
if(rec=="Horror" or rec=="horror"):
    data=movies.iloc[15:30].values
    print(data)
if(rec=="Comedy" or rec=="comedy"):
    data=movies.iloc[30:46].values
    print(data)
if(rec=="Sci-fi" or rec=="scifi"):
    data=movies.iloc[46:61].values
    print(data)
if(rec=="Action" or rec=="action"):
    data=movies.iloc[61:76].values
    print(data)
if(rec=="Romantic" or rec=="romantic"):
    data=movies.iloc[76:91].values
    print(data)
if(rec=="Crime" or rec=="crime"):
    data=movies.iloc[91:106].values
    print(data)
if(rec=="Mystery" or rec=="mystery"):
    data=movies.iloc[106:121].values
    print(data)
if(rec=="Fantasy" or rec=="fantasy"):
    data=movies.iloc[121:136].values
    print(data)
if(rec=="Inspirational" or rec=="inspirational"):
    data=movies.iloc[136:151].values
    print(data)
if(rec=="Musical" or rec=="musical"):
    data=movies.iloc[151:166].values
    print(data)