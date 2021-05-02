# Name: Alexander Yershov

from os import remove
from os import mkdir
# Name: Alexander Yershov
# ID: 319140943

from os import remove
from os import mkdir

# constants
firstRowValues = 0
firstPart = 1
lastValue = -2
tableName = 2

file = open('demo.sql', 'r')    # open the sql file
mkdir('csvFiles')       # folder for the newly created csv files
fillingTable = False    # TRUE if in process of filling table

def createTable(table):
    # function creates the title row in the new csv file
    global file
    for line in file:
        if 'KEY' in line:       # stop adding values
            table.write('\n')
            break
        table.write(line.split()[firstRowValues].strip('`') + ', ')  # write to csv

def fillTable(table, line):
    # function takes an insert line, translates it and writes it on the csv file
    insertLine = line.split('(')[firstPart:]     # line without "insert into 'name' values"
    values = []

    for i in range(len(insertLine)):
        values += insertLine[i].replace(')','').replace(';','').strip(',').split(',')   # convert values into list
        values.append('\n')
    values = [value + ', ' if value is not '\n' else value for value in values] # add ,
    values[lastValue] = values[lastValue].strip(', ')
    [table.write(value) for value in values]    # write to csv

# main program code, goes through the lines in the sql file and searches for key sentences
for line in file:
    wordsLst = line.split()
    if 'CREATE TABLE' in line:
    # check if the last table is empty and delete it if it's true. Then open a new table.
        if fillingTable:
            table.close()
            remove(name)    # delete empty table
        name = 'csvFiles\\' + wordsLst[tableName].strip('`') + '.csv'   # get table name
        table = open(name, 'w')   # open new csv file
        createTable(table)
        fillingTable = True

    if 'INSERT INTO' in line:
        fillTable(table, line)  # insert values into table
        fillingTable = False
file = open('demo.sql', 'r')
mkdir('csvFiles')
fillingTable = False

def createTable(table):
    # function creates the title row in the new csv file
    global file
    for line in file:
        if 'KEY' in line:
            table.write('\n')
            break
        table.write(line.split()[0].strip('`') + ', ')

def fillTable(table, line):
    # function takes an insert line, translates it and writes it on the csv file
    insertLine = line.split('(')[1:]     
    values = []

    for i in range(len(insertLine)):
        values += insertLine[i].replace(')','').replace(';','').strip(',').split(',')
        values.append('\n')
    values = [value + ', ' if value is not '\n' else value for value in values]
    values[-2] = values[-2].strip(', ') # take out , in the end
    [table.write(value) for value in values]


for line in file:
    wordsLst = line.split()
    if 'CREATE TABLE' in line:
        if fillingTable:    # check if the last table is empty
            table.close()
            remove(name)
        name = 'csvFiles\\' + wordsLst[2][1:-1] + '.csv'   # get table name
        table = open(name, 'w')
        createTable(table)
        fillingTable = True

    if 'INSERT INTO' in line:
        fillTable(table, line)
        fillingTable = False