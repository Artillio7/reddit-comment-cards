from PIL import Image, ImageDraw

def generate_like_icon(size=48, color=(255, 70, 100, 255), bg_alpha=0):
    """
    Génère une icône coeur stylisée (PNG RGBA, fond transparent).
    - size: taille du carré (px)
    - color: couleur du coeur (RGBA)
    - bg_alpha: opacité du fond (0 = transparent)
    """
    img = Image.new('RGBA', (size, size), (0, 0, 0, bg_alpha))
    draw = ImageDraw.Draw(img)
    # Dessin d'un coeur stylisé (bezier simplifié)
    w, h = size, size
    # Forme du coeur
    draw.polygon([
        (w*0.5, h*0.78),
        (w*0.09, h*0.38),
        (w*0.23, h*0.13),
        (w*0.5, h*0.32),
        (w*0.77, h*0.13),
        (w*0.91, h*0.38),
    ], fill=color)
    draw.ellipse([(w*0.09, h*0.15), (w*0.41, h*0.50)], fill=color)
    draw.ellipse([(w*0.59, h*0.15), (w*0.91, h*0.50)], fill=color)
    return img
