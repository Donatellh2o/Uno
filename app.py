from flask_api import FlaskAPI
from flask import send_file, request
import fitz

app = FlaskAPI(__name__)


liste = [2100, 2970]
ecart_angles = 15
largeur_angles = 20
largeur_centre = 50

rect = fitz.Rect(0, 0, liste[0], liste[1])
larg = liste[0]/10
haut = liste[1]/10


# @app.route('/generate')
# def index():
#     # todo open image
#     red = [200, 75, 51]
#     doc = fitz.Document()
#     page = doc._newPage(width=450, height=500)
#     page = doc[0]
#     rect = fitz.Rect(0, 0, 450, 500)
#     page.draw_rect(rect, color=(red[0]/255, red[1]/255, red[2]/255), fill=(red[0]/255, red[1]/255, red[2]/255), overlay=False)
#     pix = page.get_pixmap()
#     pix.save('page.png')

#     return send_file('page.png', mimetype="image/png")
    # return doc


@app.route('/with_parameters')
def generate():

    rgb = list(request.args.get('rgb').split(','))
    key = request.args.get('key')

    print(rgb)
    print(key)

    color = (int(rgb[0])/255, int(rgb[1])/255, int(rgb[2])/255)
    fichier = 'png/chiffres/' + key + '.png'

    doc = fitz.open()
    page = doc._newPage(width=liste[0], height=liste[1])

    page = doc[0]
    page.draw_rect(page.rect, color=color, fill=color, overlay=False)
    pix = page.get_pixmap()
    pix.save('page.png')

    for t in range(1, 4):

        if (t == 1):
            x1 = float(ecart_angles)
            y1 = float(ecart_angles)
            x2 = float(ecart_angles + largeur_angles)
            y2 = float(ecart_angles + largeur_angles*1.69)

            if (fichier == ('6.png' or '9.png')):
                y2 = float(ecart_angles + largeur_angles*1.95)

            rect_ = fitz.Rect(
                float((x1)/larg)*float(liste[0]),
                float((y1)/haut)*float(liste[1]),
                float((x2)/larg)*float(liste[0]),
                float((y2)/haut)*float(liste[1])
                )

        if (t == 2):
            x1 = float((larg-largeur_centre) / 2)
            y1 = float((haut-largeur_centre*1.69) / 2)
            x2 = float((larg-largeur_centre) / 2 + largeur_centre)
            y2 = float((haut-largeur_centre*1.69) / 2 + largeur_centre*1.69)

            if (fichier == ('6.png' or '9.png')):
                y1 = float((haut-largeur_centre*1.95) / 2)
                y2 = float(float((haut-largeur_centre*1.95) / 2 + largeur_centre*1.95))

            rect_ = fitz.Rect(
                float((x1)/larg)*float(liste[0]),
                float((y1)/haut)*float(liste[1]),
                float((x2)/larg)*float(liste[0]),
                float((y2)/haut)*float(liste[1])
                )

        if (t == 3):
            x1 = float(larg - (ecart_angles + largeur_angles))
            y1 = float(haut - (ecart_angles + largeur_angles*1.69))
            x2 = float(larg - ecart_angles)
            y2 = float(haut - ecart_angles)
            if (fichier == ('6.png' or '9.png')):
                y1 = float(haut - (ecart_angles + largeur_angles*1.95))

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

    return send_file('page.png', mimetype="image/png")

if __name__ == "__main__":
    app.run(debug=True)