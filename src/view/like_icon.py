from PIL import Image, ImageDraw, ImageFilter, ImageChops

def generate_like_icon(size=48, color=(255, 70, 100, 255), bg_alpha=0, glow=True, glow_color=None, glow_intensity=1.5):
    """
    Génère une icône coeur stylisée futuriste (PNG RGBA, fond transparent).
    - size: taille du carré (px)
    - color: couleur du coeur (RGBA)
    - bg_alpha: opacité du fond (0 = transparent)
    - glow: ajouter un effet de lueur néon
    - glow_color: couleur de la lueur (utilise color si None)
    - glow_intensity: intensité de la lueur (1.0 = normal)
    """
    # Base image
    img = Image.new('RGBA', (size, size), (0, 0, 0, bg_alpha))
    draw = ImageDraw.Draw(img)
    
    # Dessin du cœur
    w, h = size, size
    heart_points = [
        (w*0.5, h*0.78),  # Pointe du bas
        (w*0.09, h*0.38),  # Gauche
        (w*0.23, h*0.13),  # Haut gauche
        (w*0.5, h*0.32),   # Creux haut
        (w*0.77, h*0.13),  # Haut droit
        (w*0.91, h*0.38),  # Droit
    ]
    
    # Effet de lueur néon
    if glow:
        glow_color = glow_color or color
        
        # Créer la lueur
        glow_img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
        glow_draw = ImageDraw.Draw(glow_img)
        
        # Dessiner le cœur pour la lueur (plus épais)
        glow_draw.polygon(heart_points, fill=glow_color)
        glow_draw.ellipse([(w*0.07, h*0.13), (w*0.43, h*0.52)], fill=glow_color)
        glow_draw.ellipse([(w*0.57, h*0.13), (w*0.93, h*0.52)], fill=glow_color)
        
        # Appliquer flou gaussien pour l'effet de lueur
        glow_img = glow_img.filter(ImageFilter.GaussianBlur(radius=size/10 * glow_intensity))
        
        # Combiner avec l'image originale
        img = ImageChops.screen(img, glow_img)
    
    # Dessiner le cœur principal
    draw = ImageDraw.Draw(img)
    draw.polygon(heart_points, fill=color)
    draw.ellipse([(w*0.09, h*0.15), (w*0.41, h*0.50)], fill=color)
    draw.ellipse([(w*0.59, h*0.15), (w*0.91, h*0.50)], fill=color)
    
    # Ajouter des reflets/highlights pour effet métallique
    highlight_color = tuple(min(c + 60, 255) for c in color[:3]) + (100,)  # Plus clair et semi-transparent
    highlight_points = [(w*0.24, h*0.20), (w*0.30, h*0.22), (w*0.22, h*0.25)]
    draw.polygon(highlight_points, fill=highlight_color)
    
    return img
