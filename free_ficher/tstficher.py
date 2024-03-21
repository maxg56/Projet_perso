import os
import shutil


repertoire_source = "\.."
pile = os.listdir(repertoire_source)
b  = 0
while len(pile ) != 0 :
    filepath = os.path.join(repertoire_source, pile.pop())

    if os.path.isfile(filepath):
        print(len(pile)) 
        pass
    elif os.path.isdir(filepath):
        repertoire_source = str(filepath)
        pile +=os.listdir(repertoire_source)
        print(len(pile))
        
