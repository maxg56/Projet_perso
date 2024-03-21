import os
import shutil

# Chemin du répertoire contenant les fichiers
repertoire_source = '/chemin/vers/le/repertoire/source'

# Parcourez tous les fichiers du répertoire source
for filename in os.listdir(repertoire_source):
    # Obtenez le chemin complet du fichier
    filepath = os.path.join(repertoire_source, filename)

    # Vérifiez si c'est un fichier
    if os.path.isfile(filepath):
        # Obtenez l'extension du fichier
        extension = os.path.splitext(filename)[1]

        # Créez un dossier pour cette extension s'il n'existe pas
        dossier_destination = os.path.join(repertoire_source, extension.lstrip('.'))
        if not os.path.exists(dossier_destination):
            os.makedirs(dossier_destination)

        # Déplacez le fichier vers le dossier correspondant
        shutil.move(filepath, os.path.join(dossier_destination, filename))

print("Les fichiers ont été séparés avec succès.")
