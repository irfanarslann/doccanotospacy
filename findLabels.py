import easygui
import json
import logging as log


def findLabels(path):
    try:
        labelList = []
        fopen = open(path, 'r')
        for line in fopen.readlines():
            line = json.loads(line)

            if 'labels' in line:
                line['entities'] = line.pop('labels')

            else:
                line['entities'] = []

            for e in line['entities']:
                labelList.append(e[2])

        return labelList

    except Exception as ex:
        log.error(ex)
        


def getLabels(path):
    try:
        if findLabels(path) != None:
            labelSet = list(set(findLabels(path)))
            return labelSet
    except Exception as ex:
        log.error(ex)
