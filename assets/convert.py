from PIL import Image

def creer_masque_noir_et_transparent(chemin_entree, chemin_sortie):
    # Charger l'image et conversion en RGBA
    img = Image.open(chemin_entree).convert("RGBA")
    
    donnees = img.getdata()
    nouvelles_donnees = []

    for item in donnees:
        # item = (R, G, B, A)
        
        # 1. Si le pixel est noir pur
        if item[0] == 0 and item[1] == 0 and item[2] == 0:
            # On le rend transparent
            nouvelles_donnees.append((0, 0, 0, 0))
        else:
            # 2. Pour TOUS les autres pixels (peu importe leur couleur)
            # On les force en noir opaque
            nouvelles_donnees.append((0, 0, 0, 255))

    # Sauvegarde
    img.putdata(nouvelles_donnees)
    img.save(chemin_sortie, "PNG")
    print(f"Image binaire générée : {chemin_sortie}")

# Test du script
creer_masque_noir_et_transparent("T.png", "T.png")