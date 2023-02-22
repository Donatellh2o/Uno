import os
import fitz
import shutil

nom_origine = 'png'
s = '/'

try:
    os.mkdir(nom_origine)
except:
    print(nom_origine+" n'a pas fonctionné")

for i in ['cartes_speciales_couleurs', 'cartes_speciales', 'chiffres', 'couleur']:
    
    try:
        os.mkdir(nom_origine+s+i)
    except:
        print(nom_origine+s+i+" n'a pas fonctionné")

print("")

test = os.path.exists("contours.png")
if test == True:
    shutil.move("contours.png", "png/contours.png")
    print("contours.png déplacé")
else :
    print("contours.png n'existe pas (contours arrondis blancs)")

print("")
print("--------------------- Terminé ---------------------")

