from PIL import Image
import random

largeur = 5050
hauteur = 5050
objet_image = Image.new('RGB', (largeur, hauteur), (0,0,0))

for j in range(hauteur):
    j = j+1
    print(j)
    for i in range(largeur):
        R = random.randint(0,255) 
        G = random.randint(0,255)
        B = random.randint(0,255)
        i = i+1
        objet_image.putpixel((largeur - i, hauteur - j) ,(R,G,B))

objet_image.show()
