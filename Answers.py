import pandas as pd

#For question 1

read_people = pd.read_excel('people.xlsx')
read_animlas = pd.read_excel('animals.xlsx')

df1 = read_people.rename(columns={'ID' : 'PersonID' , 'name' : 'PersonName' , 'age' : 'PersonAge'})



#For question 2

df2 = read_animlas.rename(columns={'ID' : 'AnimalID' , 'Name' : 'AnimalName' , 'Age' : 'AnimalAge'})


#For question 3


df3 = read_people.merge(read_animlas, left_on='ID' , right_on='Owner_ID')



#For question 4

df4 = read_people.merge(read_animlas, left_on='ID' , right_on='Owner_ID' , how='left')


#For question 5

df5 = df3['Name_x'].unique()



#For question 6

df6 = df3.loc[(df3['Name_x'] == 'Ido')]



#For question 7

df7 = df3.loc[(df3['Age_x'] > 20)]


#For question 8

df8 = df3.loc[(df3['Age_x'] >= 30)]


#For question 9

df9 = df3.loc[(df3['Gender'] == 'F') & (df3['Type'] == 'dog') | (df3['Type'] == 'cat')]



#For question 10

df10 = df4.loc[(df4['Gender'] == 'M') & (df4['Type'].isnull())]



#For question 11

df11 = df3.loc[(df3['Gender'] == 'F') & (df3['Color'] == 'white')]


#For question 12

df12 = df3.loc[(df3['Gender'] == 'M') & (df3['Type'] == 'dog') & (df3['Age_x'] >= 21)]
df12 = df12['Color'].unique()


#For question 13

df13 = df10['Name_x']


#For question 14

df14 = df3.loc[(df3['Gender'] == 'F') & (df3['Color'] != 'black') & (df3['Age_y'] >= 3)]


#For question 15

df15 = df3.loc[(df3['Name_y'] == df3['Name_y'])]
df15 = df15.Name_y.value_counts()
df15 = df15[df15 > 1]
#print(len(df15.index))