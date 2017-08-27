# -*- coding: utf-8 -*-
import os
import pandas as pd
from abstimmungsparser import Abstimmung

PATH = os.path.dirname(os.path.realpath(__file__))
KEYS = ['title', 'tags', 'categories']
ABSTIMMUNG_KEYS = ['bundestagssitzung', 'legislaturperiode', 'datum']


def getCSVLink(abstimmung):
    datafiles = abstimmung.get_data_files()
    for filename in datafiles:
        url = filename['url']
        if url.split('.')[-1] == 'csv':
            return url
    print 'WARNING: %s No csv file found' % abstimmung.get_title()
    return '-'
        

def createAbstimmungsDatabase():

    data = []

    for directory, subs, files in os.walk(PATH):
        if '018' in directory:
            filename = os.path.join(directory, 'index.md')
            abstimmung = Abstimmung()
            abstimmung.parse_abstimmung(filename)

            values = []
            for key in KEYS:
                values.append(abstimmung.data[key])

            for key in ABSTIMMUNG_KEYS:
                values.append(abstimmung.data['abstimmung'][key])

            csv = getCSVLink(abstimmung)
            values.append(csv)
            values.append([directory])
            data.append(values)


    dataFrame = pd.DataFrame(data, columns=KEYS + ABSTIMMUNG_KEYS + ['csv', 'directory'])
    dataFrame.to_csv('../../data/Abstimmungsdaten.csv', encoding='utf8')


if __name__=='__main__':
    createAbstimmungsDatabase()
