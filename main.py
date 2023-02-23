import fitz
from PyPDF2 import PdfMerger
import os
import random
import shutil

localisation_generale = ''

#------Positions sur la page------
ecart_angles = 15
largeur_angles = 20
largeur_centre = 50

#------Format------
liste = [2100, 2970]
format = 'A4'

#------RGB------
red = [200, 75, 51]
blue = [51, 116, 181]
green = [146, 190, 83]
yellow = [246, 214, 89]
black = [0, 0, 0]


#----------------

rouge = (red[0]/255, red[1]/255, red[2]/255)
bleu = (blue[0]/255, blue[1]/255, blue[2]/255)
vert = (green[0]/255, green[1]/255, green[2]/255)
jaune = (yellow[0]/255, yellow[1]/255, yellow[2]/255)
noir = (black[0]/255, black[1]/255, black[2]/255)

rect = fitz.Rect(0, 0, liste[0], liste[1])

larg = liste[0]/10
haut = liste[1]/10

#----------------

print("")
print("Création des folders")
print("")

nom_origine = 'resultats'
s = '/'

try:
    os.mkdir(nom_origine)
except:
    print(nom_origine+" n'a pas fonctionné")

for i in ['speciales_couleurs', 'chiffres']:

    try:
        os.mkdir(nom_origine+s+i)
    except:
        print(nom_origine+s+i+" n'a pas fonctionné")

    for u in ['rouge', 'jaune', 'vert', 'bleu']:

        try:
            os.mkdir(nom_origine+s+i+s+u)
        except:
            print(nom_origine+s+i+s+u+" n'a pas fonctionné")

i = 'speciales'

try:
    os.mkdir(nom_origine+s+i)
except:
    print(nom_origine+s+i+" n'a pas fonctionné")

print("")
print("---Done---")
print("")


    #++++++++++++++++++++++++++++++++++

def transformation_chiffres(nom_fichier, fichier_location_sortie, fichier_couleur, fichier_document_autour, fichier_document_centre):

    doc = fitz.open()
    page = doc._newPage(width = liste[0], height = liste[1])

    page = doc[0]
    page.draw_rect(page.rect, color=globals()[fichier_couleur], fill=globals()[fichier_couleur], overlay=False)
    pix = page.get_pixmap()
    pix.save(fichier_location_sortie)


    for t in range(1,5):

        if (t==1):
            x1=float(ecart_angles)
            y1=float(ecart_angles)
            x2=float(ecart_angles + largeur_angles)
            y2=float(ecart_angles + largeur_angles*1.69)

            if (nom_fichier == ('6.png' or '9.png')):
                y2=float(ecart_angles + largeur_angles*1.95)

            rect_ = fitz.Rect(
                float((x1)/larg)*float(liste[0]),
                float((y1)/haut)*float(liste[1]),
                float((x2)/larg)*float(liste[0]), 
                float((y2)/haut)*float(liste[1])
                )

            fichier = fichier_document_autour

        if (t==2):
            x1=float((larg-largeur_centre) / 2)
            y1=float((haut-largeur_centre*1.69) / 2)
            x2=float((larg-largeur_centre) / 2 + largeur_centre)
            y2=float((haut-largeur_centre*1.69) / 2 + largeur_centre*1.69)
           
            if (nom_fichier == ('6.png' or '9.png')):
                y1=float((haut-largeur_centre*1.95) / 2)
                y2=float(float((haut-largeur_centre*1.95) / 2 + largeur_centre*1.95))

            rect_ = fitz.Rect(
                float((x1)/larg)*float(liste[0]),
                float((y1)/haut)*float(liste[1]),
                float((x2)/larg)*float(liste[0]), 
                float((y2)/haut)*float(liste[1])
                )

            fichier = fichier_document_centre

        if (t==3):
            x1=float(larg - (ecart_angles + largeur_angles))
            y1=float(haut - (ecart_angles + largeur_angles*1.69))
            x2=float(larg - ecart_angles)
            y2=float(haut - ecart_angles)
            if (nom_fichier == ('6.png' or '9.png')):
                y1=float(haut - (ecart_angles + largeur_angles*1.95))

            rect_ = fitz.Rect(
                float((x1)/larg)*float(liste[0]),
                float((y1)/haut)*float(liste[1]),
                float((x2)/larg)*float(liste[0]), 
                float((y2)/haut)*float(liste[1])
                )

            fichier = fichier_document_autour

        if (t==4):
            rect_ = rect
            fichier = 'png/contours'+format+'.png'

        page = doc[0]
        img = open(fichier, "rb").read()
        page.insert_image(rect_, stream=img)
        pix = page.get_pixmap()
        pix.save(fichier_location_sortie)

#+++++

def transformation_pdf(nom_fichier, fichier_location_sortie, fichier_couleur, fichier_document_autour, fichier_document_centre):

    doc = fitz.open()
    page = doc._newPage(width = liste[0], height = liste[1])

    page = doc[0]
    page.draw_rect(page.rect, color=globals()[fichier_couleur], fill=globals()[fichier_couleur], overlay=False)
    pix = page.get_pixmap()
    pix.save(fichier_location_sortie)

    for t in range(1,5):

        if (t==1):
            x1=float(ecart_angles)
            y1=float(ecart_angles)
            x2=float(ecart_angles + largeur_angles * 2)
            y2=float(ecart_angles + largeur_angles * 2)

            rect_ = fitz.Rect(
                float((x1)/larg)*float(liste[0]),
                float((y1)/haut)*float(liste[1]),
                float((x2)/larg)*float(liste[0]), 
                float((y2)/haut)*float(liste[1])
                )

            fichier = fichier_document_autour

        if (t==2):
            x1=float(larg/2 - largeur_centre)
            y1=float(haut/2 - largeur_centre)
            x2=float(larg/2 + largeur_centre)
            y2=float(haut/2 + largeur_centre)

            rect_ = fitz.Rect(
                float((x1)/larg)*float(liste[0]),
                float((y1)/haut)*float(liste[1]),
                float((x2)/larg)*float(liste[0]), 
                float((y2)/haut)*float(liste[1])
                )

            fichier = fichier_document_centre

        if (t==3):
            x1=float(larg - (ecart_angles + largeur_angles * 2))
            y1=float(haut - (ecart_angles + largeur_angles * 2))
            x2=float(larg - ecart_angles)
            y2=float(haut - ecart_angles)

            rect_ = fitz.Rect(
                float((x1)/larg)*float(liste[0]),
                float((y1)/haut)*float(liste[1]),
                float((x2)/larg)*float(liste[0]), 
                float((y2)/haut)*float(liste[1])
                )

            fichier = fichier_document_autour

        if (t==4):
            rect_ = rect
            fichier = 'png/contours'+format+'.png'

        page = doc[0]
        img = open(fichier, "rb").read()
        page.insert_image(rect_, stream=img)
        pix = page.get_pixmap()
        pix.save(fichier_location_sortie)



#+++++



nn = input("Create PNG chiffres (y/n) : ")
if nn == 'y' :

    print("")
    print("Création des PNG des chiffres")

    for u in ['rouge','jaune','vert','bleu']:
       
        print("")
        print(u+"s")

        for i in range(10):

            print("     "+str(i))

            nom_fichier = str(i)+'.png'
            localisation_fichier_source_chiffre = localisation_generale+'png/chiffres/'+str(i)+'.png'
            localisation_fichier_source_couleur = u
            sortie = localisation_generale+'resultats/chiffres/'+u+'/'+u+nom_fichier

            transformation_chiffres(nom_fichier, sortie, localisation_fichier_source_couleur, localisation_fichier_source_chiffre, localisation_fichier_source_chiffre)
            
        
    print("")
    print("---Done---")




nn = input("Create PNG spéciales colorées (y/n) : ")
if nn == 'y' :

    print("")
    print("Création des PNG des signes colorés")

    for u in ['rouge','jaune','vert','bleu']:
       
        print("")
        print(u+"s")

        for i in ['sauter','sens','plus_2']:

            print("     "+i)

            localisation_fichier_source_centre = localisation_generale+'png/cartes_speciales_couleurs/'+i+'_signe.png'
            nom_fichier = i+'.png'
            localisation_fichier_source_chiffre = localisation_generale+'png/cartes_speciales_couleurs/'+str(i)+'.png'
            localisation_fichier_source_couleur = u
            sortie = localisation_generale+'resultats/speciales_couleurs/'+u+'/'+u+nom_fichier

            transformation_pdf(nom_fichier, sortie, localisation_fichier_source_couleur, localisation_fichier_source_chiffre, localisation_fichier_source_centre)

    print("")
    print("---Done---")






nn = input("Create PNG spéciales (y/n) : ")
if nn == 'y' :

    print("")
    print("Création des PNG signes intercouleurs")
    print("")

    for i in ['changer', 'plus_4']:

        print(i)

        localisation_fichier_source_centre = localisation_generale+'png/cartes_speciales/'+i+'_signe.png'
        nom_fichier = i+'.png'
        localisation_fichier_source_chiffre = localisation_generale+'png/cartes_speciales/'+str(i)+'.png'
        localisation_fichier_source_couleur = 'noir'
        sortie = localisation_generale+'resultats/speciales/'+nom_fichier

        transformation_pdf(nom_fichier, sortie, localisation_fichier_source_couleur, localisation_fichier_source_chiffre, localisation_fichier_source_centre)

    print("")    
    print("---Done---")
    print("")



nn = input("Create PNG versos (y/n) : ")
if nn == 'y' :

    print("")
    print("Création des PNG des versos")
    print("")

    for i in range (4):

        print(str(i))

        doc = fitz.open()
        page = doc._newPage(width = liste[0], height = liste[1])

        for u in range (2):

            if u == 0 :
                fichier = 'png/cartes_speciales/verso'+str(i)+'.png'

            if u == 1 :
                fichier = 'png/contours'+format+'.png'

            page = doc[0]
            img = open(fichier, "rb").read()
            page.insert_image(rect, stream=img)
            pix = page.get_pixmap()
            pix.save('resultats/speciales/verso'+str(i)+'.png')


    print("")    
    print("---Done---")
    print("")










print("")
print("Réunion des PNG")
print("")


compte = []

for i in range(8):
    compte += [i]

c = 0

try:
    os.mkdir('resultats/reunis')
except:
    print("resultats/reunis n'a pas fonctionné")

doc = fitz.open()
page = doc._newPage(width = liste[0], height = liste[1])
largeur = liste[0]/4            
hauteur = liste[1]/4

comptei = []
compte2 = []

for u in ['rouge', 'jaune', 'vert', 'bleu']:

    for z in range(10):
        for t in range(2):
            comptei.append(str(z))
            autre = 'chiffres/'+u+'/'+u
            compte2.append(autre)
    for z in ['sauter', 'sens', 'plus_2']:
        for t in range(2):
            comptei.append(z)
            autre = 'speciales_couleurs/'+u+'/'+u
            compte2.append(autre)
    
for z in ['changer', 'plus_4']:
    for t in range(4):
        comptei.append(z)
        autre = 'speciales/'
        compte2.append(autre)

i = 0

for b in range(7):

    print("Page "+str(b+1)+"/7")

    for cpt2 in range(4): 
        for cpt in range(4):

            rect_ = [cpt*largeur, cpt2*hauteur, (cpt+1)*largeur, (cpt2+1)*hauteur]

            fichier = "resultats/"+compte2[i]+comptei[i]+".png"

            img = open(fichier, "rb").read()
            page = doc[0]
            page.insert_image(rect_, stream=img)
            i += 1

    sortie = 'resultats/reunis/'+str(compte[c])
    c += 1

    doc.save(sortie+'.pdf', deflate=1)

print("")
print("---Done---")
print("")









print("Réunion des PNG du verso")
print("")


liste_ = []
liste0 = []
liste1 = []
liste2 = []
liste3 = []

for i in range(28):

    liste0 += [0]
    liste1 += [1]
    liste2 += [2]
    liste3 += [3]

liste_ += liste0
liste_ += liste1
liste_ += liste2
liste_ += liste3

random.shuffle(liste_)

print(liste_)
print("")



for i in range(7):
    compte += [i]

c = 0

try:
    os.mkdir('resultats/reunis')
except:
    print("resultats/reunis n'a pas fonctionné")

doc = fitz.open()
page = doc._newPage(width = liste[0], height = liste[1])
largeur = liste[0]/4            
hauteur = liste[1]/4

i = 0


for b in range(7):

    print("Verso "+str(b+1)+"/7")

    for cpt2 in range(4): 
        for cpt in range(4):

            rect_ = [cpt*largeur, cpt2*hauteur, (cpt+1)*largeur, (cpt2+1)*hauteur]

            fichier = "resultats/speciales/verso"+str(liste_[i])+".png"

            img = open(fichier, "rb").read()
            page = doc[0]
            page.insert_image(rect_, stream=img)
            i += 1

    doc.save('resultats/reunis/verso'+str(compte[c])+'.pdf', deflate = 1)
    c += 1

print("")
print("---Done---")
print("")








print("Fusionnement des PDF")

liste = []

general = "resultats/reunis/"
    
for i in range(7):

    liste += [general+str(i)+".pdf"]
    liste += [general+"verso"+str(i)+".pdf"]

merger = PdfMerger()

for pdf in liste:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()

print("")
print("---Done---")
print("")

print("")
print("--------------------- Finished ---------------------")

print("")
nn = input("Delete other files (y/n) : ")
if nn == 'y' :
    shutil.rmtree('resultats')
    print("Done.")
    print("")
else :
    print("Files kept")
    print("")