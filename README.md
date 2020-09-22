#Doccano output file parser for spaCy NLP.

Hello everyone! I developed a parser that can parse Doccano output file format to spaCy format for NLP. 

If u wondering how to use this script, then let me explain:

1: First thing u have to do import parse.py file into ur NLP Train Python File.

2: Change TRAIN_DATA = [] variable to TRAIN_DATA = parse.parseDoccanoToSpacy()

3: Run ur train file 

4: Choose ur doccano export file.

5: And your model will be trained with ur data that annotated with doccano
