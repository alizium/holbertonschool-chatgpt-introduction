#!/usr/bin/python3
import sys  # Pour accéder aux arguments passés en ligne de commande

for i in range(1, len(sys.argv)):
    # On commence à 1 pour ignorer sys.argv[0] (le nom du script)
    print(sys.argv[i])  # On affiche chaque argument utilisateur
