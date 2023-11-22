# Documentation du Script de Tri de Fichiers
### Introduction
Ce script Python a été conçu pour trier les fichiers d'un répertoire source en fonction de leurs extensions. Il crée des dossiers correspondant aux extensions des fichiers et déplace chaque fichier dans le dossier approprié.



## Configuration
### Répertoire Source
Définissez la variable repertoire_source avec le chemin absolu du répertoire contenant les fichiers que vous souhaitez trier.
```python
    repertoire_source = '/chemin/vers/le/repertoire/source'
```
### Exécution du Script
Le script parcourt tous les fichiers du répertoire source, vérifie s'ils sont des fichiers (plutôt que des répertoires) et les déplace dans des dossiers spécifiques en fonction de leurs extensions.

### Fonctionnement
1. **Parcours des Fichiers** : Le script utilise la bibliothèque '**os**' pour parcourir tous les fichiers du répertoire source.

2. **Création des Dossiers** : Pour chaque fichier, il extrait l'extension du nom de fichier et crée un dossier correspondant à cette extension (s'il n'existe pas déjà).

3. **Déplacement des Fichiers** : Les fichiers sont ensuite déplacés vers leur dossier respectif.

4. **Message de Confirmation** : Une fois le processus terminé, le script affiche un message indiquant que les fichiers ont été séparés avec succès.

### Conclusion
Ce script est utile pour maintenir l'ordre dans un répertoire contenant divers types de fichiers en les organisant de manière claire et compréhensible. N'hésitez pas à ajuster le chemin du répertoire source selon vos besoins.