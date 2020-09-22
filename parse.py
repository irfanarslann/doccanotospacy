import json
import easygui
import logging
import findLabels
logging.basicConfig(level=logging.INFO, filename='logs/parserLog.txt')

labels = []
path = easygui.fileopenbox()


def parseDoccanoToSpacy():
    try:

        fopen = open(path, 'rt')
        lines = fopen.readlines()
        data = []
        labels = findLabels.getLabels(path)

        for line in lines:
            line = json.loads(line)

            if 'labels' in line:
                line['entities'] = line.pop('labels')
            else:
                line['entities'] = []

            entities = []

            for e in line['entities']:
                if e[2] in labels:
                    entities.append(
                        {"start": e[0], "end": e[1], "label": e[2]})
                    line['entities'] = entities

            entJson = {"entities": []}
            if (len(line["text"]) > 5):
                text = (line["text"])

                for e in line["entities"]:
                    entJson["entities"].append(
                        (e["start"], e["end"], e["label"]))

                data.append((text, entJson))

        return data

    except Exception as ex:
        logging.info(ex)
        


def getLabels():
    return labels
