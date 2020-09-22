import json
import easygui
import logging
import findLabels
logging.basicConfig(level=logging.INFO, filename='logs/parserLog.txt')

viqLabels = []
path = easygui.fileopenbox()


def parseDoccanoToSpacy():
    try:

        fopen = open(path, 'rt')
        lines = fopen.readlines()
        data = []
        viqLabels = findLabels.getLabels(path)

        for line in lines:
            line = json.loads(line)

            if 'labels' in line:
                line['entities'] = line.pop('labels')
            else:
                line['entities'] = []

            viq_entities = []

            for e in line['entities']:
                if e[2] in viqLabels:
                    viq_entities.append(
                        {"start": e[0], "end": e[1], "label": e[2]})
                    line['entities'] = viq_entities

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
    return viqLabels
