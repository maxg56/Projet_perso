import os
import shutil


repertoire_source = "\.."
pile = os.listdir(repertoire_source)

while len(pile ) >= 0 :
    filepath = os.path.join(repertoire_source, pile.pop())
    if os.path.isfile(filepath): 
        pass
    else:
        pile.append(os.listdir(repertoire_source+filepath))