#!/usr/bin/python

import os

''' This file builds the dataset to give as an input
to the MLP '''

def createSupervisedDataSet(path):
    f = open(path,'r')
    lines = f.readlines()
    n = len(lines[0].split())
    input_variables_n = n-1
    output_variable_n = 1

    items =lines[0].split()
    indexes = []
    j = 0
    for i in items:
        try:
            i = int(i)
        except ValueError:
            indexes.append(j)
        j+=1
    values = {}
    for i in indexes:
        values[i] = []
    for line in lines:
        items = line.split()
        for i in indexes:
            values[i].append(items[i])
    maps = {}
    for k in values.keys():
        j=1
        values[k] = set(values[k])
        for i in values[k]:
            maps[i] = j
            j+=1

    for line in lines:
        items = line.split()
        print items
        for i in indexes:
            items[i] = maps[items[i]]
        for i in [i for i in range(0,n) if i not in indexes]:
            items[i] = int(items[i])
        print items
        line = ''
        for i in items:
            line += str(i)+' '
        f = open('./proba.txt','a')
        f.write(line)
        f.write('\n')


if __name__ == "__main__":
    path = './german.data.txt'
    createSupervisedDataSet(os.path.abspath(path))
