# -*- coding: utf-8 -*-

import pandas as pd
import pdb

OPTIONS = ['ja', 'nein', 'Enthaltung', 'ungültig', 'nichtabgegeben']
COLS = ['Name', 'Vorname', 'Fraktion/Gruppe']


def setVotingCategory(data, title):
    voting = data[OPTIONS]
    data[title] = voting.idxmax(axis=1)


def dropColumns(columns):
    return data.drop(columns, axis=1)


def getMdbAbstimmungen():
    
    data = [] 
    abstimmungen = pd.read_csv('../../data/Abstimmungen.csv')
    for ind,row in abstimmungen.iterrows():
        link = row.csv
        title = row.title
        print title
        abstimmung = pd.read_csv('../' + row.csv)
        setVotingCategory(abstimmung, title)
        abstimmung = abstimmung[COLS + [title]]
        data.append(abstimmung)


    mdbAbstimmungen = reduce(lambda df1, df2: df1.merge(df2, on=COLS, how='outer'), data)
    mdbAbstimmungen.rename(columns = {COLS[2]: 'party', 'Name':'name', 'Vorname':'first_name'}, inplace=True)
    
    mdbAbstimmungen.to_csv('../../data/mdbAbstimmungen.csv')



if __name__=='__main__':
    getMdbAbstimmungen()
