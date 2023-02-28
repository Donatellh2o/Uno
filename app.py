from flask_api import FlaskAPI
from flask import send_file, request
import fitz
import os

app = FlaskAPI(__name__)


liste = [2100, 2970]
ecart_angles = 15
hauteur_angles = 34
hauteur_centre = 85

rect = fitz.Rect(0, 0, liste[0], liste[1])
larg = liste[0]/10
haut = liste[1]/10


#-- Generator of numbers function --
def generate_number(rgb, key, validation):

    color = (int(rgb[0])/255, int(rgb[1])/255, int(rgb[2])/255)

    doc = fitz.open()
    page = doc._newPage(width=liste[0], height=liste[1])

    page = doc[0]
    page.draw_rect(page.rect, color=color, fill=color, overlay=False)
    pix = page.get_pixmap()
    pix.save('page.png')

    for t in range(1, 4):

        fichier = 'png/' + key + '.png'

        if (t == 1):
            x1 = float(ecart_angles)
            y1 = float(ecart_angles)
            x2 = float(ecart_angles + hauteur_angles)
            y2 = float(ecart_angles + hauteur_angles)

            rect_ = fitz.Rect(
                float((x1)/larg)*float(liste[0]),
                float((y1)/haut)*float(liste[1]),
                float((x2)/larg)*float(liste[0]),
                float((y2)/haut)*float(liste[1])
                )

        if (t == 2):
            x1 = float((larg-hauteur_centre) / 2)
            y1 = float((haut-hauteur_centre) / 2)
            x2 = float((larg-hauteur_centre) / 2 + hauteur_centre)
            y2 = float((haut-hauteur_centre) / 2 + hauteur_centre)

            rect_ = fitz.Rect(
                float((x1)/larg)*float(liste[0]),
                float((y1)/haut)*float(liste[1]),
                float((x2)/larg)*float(liste[0]),
                float((y2)/haut)*float(liste[1])
                )

            if validation == 1:
                fichier = 'png/' + key + '_signe.png'

        if (t == 3):
            x1 = float(larg - (ecart_angles + hauteur_angles))
            y1 = float(haut - (ecart_angles + hauteur_angles))
            x2 = float(larg - ecart_angles)
            y2 = float(haut - ecart_angles)

            rect_ = fitz.Rect(
                float((x1)/larg)*float(liste[0]),
                float((y1)/haut)*float(liste[1]),
                float((x2)/larg)*float(liste[0]),
                float((y2)/haut)*float(liste[1])
                )

        page = doc[0]
        img = open(fichier, "rb").read()
        page.insert_image(rect_, stream=img)
        pix = page.get_pixmap()
        pix.save('page.png')
#-----


#-- Route for numbers --
@app.route('/with_parameters')
def generate():

    rgb = list(request.args.get('rgb').split(','))
    key = request.args.get('key')
    try:
        if int(key) in range(0, 10):
            generate_number(rgb, key, 0)
            return send_file('page.png', mimetype="image/png")
            os.remove("page.png")
    except:
        print()

    if key in ['sauter', 'sens', 'plus_2', 'changer', 'plus_4']:
        generate_number(rgb, key, 1)
        return send_file('page.png', mimetype="image/png")
        os.remove("page.png")
    

    if key == 'complete':
        return send_file('result.pdf', mimetype="image/pdf")

if __name__ == "__main__":
    app.run(debug=True)
#-----
