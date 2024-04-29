import noise 
from PIL import Image
import random
taille = (128, 128)


def sec_color(x,y,image,value,):
    
    blue = (66,110,225)
    green = (36,135,32)
    beach =(240,210,172)
    mountains = (140,140,140)
    snow =(250,250,250)

    if value < -0.07:
        image.putpixel((x, y) , blue)
    elif value < 0:
        image.putpixel((x, y) , beach)
    elif value < 0.25:
        image.putpixel((x, y) , green)
    elif value < 0.50 :
        image.putpixel((x, y), mountains)
    elif value < 1.0:
        image.putpixel((x, y), snow)

def bruit_de_perlin(longueur,Auteur):
    """Cette fonction utilise l'algorithme De bruit de perling puis ressort une matrice"""
    matrice_de_pixel = [[None for _ in range(Auteur)]for _  in range(longueur)]
    scale = round(random.uniform(10.0, 80.0),2)
    octaves = 6
    lacunarity = round(random.uniform(1.5, 2.0),2)
    persistence = round(random.uniform(0.5, 0.7),2)
    print(f"scale : {scale} , lacunarity: {lacunarity} ,persistence :{persistence}")
    for x in range(longueur):
        for y in range(Auteur):
            value = noise.pnoise2(x/scale,
                                y/scale,
                                octaves=octaves,
                                persistence=persistence,
                                lacunarity=lacunarity,
                                repeatx=longueur,
                                repeaty=Auteur,
                                base=0
                                )
            matrice_de_pixel[x][y] = value
    return matrice_de_pixel

if __name__ == "__main__":
    taille = (1980, 1080)
    for i in range(10):
        image_Nom = f"noise{i}.png"
        matrice = bruit_de_perlin(taille[0],taille[1])

        image = Image.new(mode="RGB", size=taille)
        for x in range(taille[0]):
            for y in range(taille[1]):
                sec_color(x,y,image,matrice[x][y]) 
        image.save(image_Nom)

