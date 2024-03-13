# Importez les modules nécessaires
import os
import subprocess

# Définissez une liste des fichiers Python à tester
fichiers_python = ["scraping.py", "manager.py", "single.py", "QR_code.py"]

# Fonction pour exécuter Pylint sur chaque fichier
def executer_pylint(fichier):
    """
    Exécute Pylint sur le fichier spécifié.

    Parameters
    ----------
    fichier : str
        Le nom du fichier Python à tester.

    Returns
    -------
    None
    """
    command = f"pylint {fichier}"
    subprocess.run(command, shell=True)

# Fonction pour exécuter Black pour formater chaque fichier
def executer_black(fichier):
    """
    Exécute Black pour formater le fichier spécifié.

    Parameters
    ----------
    fichier : str
        Le nom du fichier Python à formater.

    Returns
    -------
    None
    """
    command = f"black {fichier}"
    subprocess.run(command, shell=True)

# Exécutez Pylint sur chaque fichier
for fichier in fichiers_python:
    executer_pylint(fichier)

# Exécutez Black pour formater chaque fichier
for fichier in fichiers_python:
    executer_black(fichier)