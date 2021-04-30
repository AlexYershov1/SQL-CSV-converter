# Name: Alexander Yershov

from os import remove
from os import mkdir

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