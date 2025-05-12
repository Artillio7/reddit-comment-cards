from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os
import random
import re
from view.style_manager import StyleManager
from view.faux_usernames import FAUX_USERNAMES
from view.like_icon import generate_like_icon
from model.structures import Post, Comment

class CardGenerator:

    def __init__(self, style_manager: StyleManager, 
                 palette=None, 
                 show_likes=True, 
                 faux_usernames=None):
        # TikTok vertical card, mais taille carte réduite (ex: 1080x1350)
        self.card_width = 1060  # Largeur fixe demandée
        self.size = (self.card_width, None)  # Hauteur dynamique
        # Style manager pour les thèmes
        self.style_manager = style_manager
        
        # Palette personnalisable (fallback si style_manager n'a pas de thème)
        default_palette = {
            'background': (18, 28, 58, 210),  # Bleu nuit profond, glassmorphism
            'border': (0, 120, 255, 120),    # Bleu vif pour la bordure
            'shadow': (0, 40, 120, 100),     # Ombre bleutée
            'text': (230, 245, 255, 255),    # Blanc bleuté très lisible
            'accent': (0, 195, 255, 255),    # Bleu cyan électrique
            'like': (0, 180, 255, 255),      # Bleu plus clair pour le like
        }
        self.palette = palette or default_palette
        # Récupérer les couleurs du thème actif ou utiliser la palette par défaut
        style = self.style_manager.get_style() or {}
        self.text_color = style.get('text', self.palette['text'])
        self.accent_color = style.get('accent', self.palette['accent'])
        self.card_bg_color = style.get('background', self.palette['background'])
        self.border_color = style.get('border', self.palette['border'])
        self.shadow_color = style.get('shadow', self.palette['shadow'])
        self.like_color = style.get('like', self.palette['like'])
        
        self.show_likes = show_likes
        self.faux_usernames = faux_usernames or FAUX_USERNAMES
        self.font_path = self._find_font()
        self.title_font_size = 56
        self.body_font_size = 44
        self.meta_font_size = 36
        os.makedirs("output", exist_ok=True)

    def _find_font(self):
        from pathlib import Path
        # Recherche Montserrat, Poppins, Roboto, Arial
        possible_paths = [
            Path(__file__).parent.parent.parent / "resources" / "fonts" / "Montserrat-Regular.ttf",
            Path(__file__).parent.parent.parent / "resources" / "fonts" / "Poppins-Regular.ttf",
            Path(__file__).parent.parent.parent / "resources" / "fonts" / "Roboto.ttf",
            Path(__file__).parent.parent.parent / "resources" / "fonts" / "Arial.ttf",
        ]
        for font_path in possible_paths:
            if os.path.exists(font_path):
                return str(font_path)
        return "arial.ttf"
        
    def _create_gradient_bar(self, width, height, start_color, end_color):
        """Crée une barre avec un dégradé horizontal"""
        from PIL import Image, ImageDraw
        
        gradient = Image.new('RGBA', (width, height), (0,0,0,0))
        draw = ImageDraw.Draw(gradient)
        
        # Créer le dégradé horizontal
        for x in range(width):
            r = int(start_color[0] + (x / width) * (end_color[0] - start_color[0]))
            g = int(start_color[1] + (x / width) * (end_color[1] - start_color[1]))
            b = int(start_color[2] + (x / width) * (end_color[2] - start_color[2]))
            a = start_color[3]
            draw.line([(x, 0), (x, height)], fill=(r, g, b, a))
        
        # Arrondir les coins
        mask = Image.new('L', (width, height), 0)
        mask_draw = ImageDraw.Draw(mask)
        mask_draw.rounded_rectangle([(0,0), (width, height)], radius=height//2, fill=255)
        
        # Appliquer le masque
        gradient.putalpha(mask)
        return gradient

    def _create_futuristic_pattern(self, width, height, border_radius, color):
        """Crée un motif futuriste de lignes/circuits/hexagones"""
        from PIL import Image, ImageDraw
        import random
        import math
        
        pattern = Image.new('RGBA', (width, height), (0,0,0,0))
        draw = ImageDraw.Draw(pattern)
        
        # Créer un masque pour limiter le dessin aux coins arrondis
        mask = Image.new('L', (width, height), 0)
        mask_draw = ImageDraw.Draw(mask)
        mask_draw.rounded_rectangle([(0,0), (width-1, height-1)], radius=border_radius, fill=255)
        
        # Réduire l'opacité de la couleur
        pattern_color = color[:3] + (40,)  # 40 d'alpha
        pattern_color_light = color[:3] + (20,)  # 20 d'alpha
        
        # Option 1: Motif de circuit
        # Lignes horizontales aléatoires
        for i in range(10):
            y = random.randint(0, height)
            line_width = random.randint(50, int(width*0.8))
            start_x = random.randint(0, width - line_width)
            draw.line([(start_x, y), (start_x + line_width, y)], fill=pattern_color, width=1)
            
            # Avec quelques connexions verticales
            if random.random() > 0.5:
                conn_height = random.randint(20, 80)
                draw.line([(start_x + random.randint(0, line_width), y), 
                          (start_x + random.randint(0, line_width), y + conn_height)], 
                         fill=pattern_color, width=1)
        
        # Option 2: Motif hexagonal (en plus)
        hex_size = 30
        hex_spacing = hex_size * 2
        alpha = 15  # Très transparent
        
        for x in range(0, width + hex_spacing, hex_spacing):
            for y in range(0, height + hex_spacing, hex_spacing):
                # Décalage pour les rangées impaires
                offset = hex_spacing // 2 if (y // hex_spacing) % 2 == 1 else 0
                x_pos = x + offset
                
                # Dessiner un hexagone
                if random.random() > 0.5:  # 50% de chance d'avoir un hexagone
                    points = []
                    for i in range(6):
                        angle = i * 60
                        px = x_pos + math.cos(math.radians(angle)) * (hex_size//2)
                        py = y + math.sin(math.radians(angle)) * (hex_size//2)
                        points.append((px, py))
                    
                    # Hexagone avec contour seulement
                    if random.random() > 0.7:
                        draw.polygon(points, outline=pattern_color_light)
                    else:
                        draw.polygon(points, fill=pattern_color_light)
        
        # Appliquer le masque
        pattern.putalpha(mask)
        return pattern

    def _create_light_effect(self, width, height, border_radius):
        """Crée un effet de lumière dynamique (réflexion, éblouissement)"""
        from PIL import Image, ImageDraw, ImageFilter, ImageChops
        
        light = Image.new('RGBA', (width, height), (0,0,0,0))
        draw = ImageDraw.Draw(light)
        
        # Effet de reflet en haut
        highlight_color = (255, 255, 255, 20)  # Très transparent
        
        # Trait lumineux horizontal en haut
        draw.rounded_rectangle(
            [(width*0.1, height*0.05), (width*0.9, height*0.07)], 
            radius=height*0.01, 
            fill=highlight_color
        )
        
        # Reflet subtil en coin supérieur gauche
        for i in range(10):
            opacity = 20 - i*2  # Diminue l'opacité
            if opacity > 0:
                size = 100 - i*10
                draw.ellipse(
                    [(20, 20), (20 + size, 20 + size)], 
                    fill=(255, 255, 255, opacity)
                )
        
        # Flouter l'effet pour le rendre plus naturel
        light = light.filter(ImageFilter.GaussianBlur(radius=10))
        
        # Créer un masque pour limiter aux coins arrondis
        mask = Image.new('L', (width, height), 0)
        mask_draw = ImageDraw.Draw(mask)
        mask_draw.rounded_rectangle([(0,0), (width-1, height-1)], radius=border_radius, fill=255)
        
        # Appliquer le masque
        light.putalpha(ImageChops.multiply(light.split()[3], mask))
        
        return light

    def create_title_card(self, title, subreddit, author, output_path=None, likes=None, pseudo=None, show_likes=True, show_pseudo=True):
        # Récupérer le nom du thème actuel pour l'utiliser dans le nom du fichier
        current_theme = self.style_manager.get_current_theme_name()
        """Génère une carte titre au style futuriste"""
        from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance, ImageChops
        import textwrap
        import os
        import random
        
        # Récupération du style
        style = self.style_manager.get_style()
        bg_color = style.get('background', self.card_bg_color)
        accent_color = style.get('accent', self.accent_color)
        text_color = style.get('text', self.text_color)
        border_color = style.get('border', self.border_color)
        shadow_color = style.get('shadow', self.shadow_color)
        like_color = style.get('like', self.like_color)
        secondary_accent = style.get('secondary_accent', accent_color)
        gradient_start = style.get('gradient_start', accent_color)
        gradient_end = style.get('gradient_end', secondary_accent)
        blur_radius = style.get('blur_radius', 16)
        border_width = style.get('border_width', 6)
        glow_effect = style.get('glow_effect', True)
        glow_intensity = style.get('glow_intensity', 2.5)  # Intensité de lueur augmentée
        pattern_overlay = style.get('pattern_overlay', False)
        light_effects = style.get('light_effects', True)  # Activer les effets de lumière par défaut
        
        # Pseudo et likes
        # Si pseudo n'est pas fourni ou est None, utiliser l'auteur ou un nom aléatoire
        if pseudo is None:
            if author and str(author) != 'None':
                pseudo = str(author)
            else:
                pseudo = random.choice(self.faux_usernames)
        likes_val = likes if likes is not None else random.randint(1200, 42000)
        likes_str = f"{likes_val/1000:.1f}k" if likes_val >= 1000 else str(likes_val)
        
        # Paramètres de mise en page améliorés
        card_padding = 64
        accent_bar_height = 14  # Plus épais
        border_radius = 56
        shadow_offset = 30  # Plus d'espace pour l'ombre
        vertical_padding = 50
        pseudo_padding_left = 40
        pseudo_padding_bottom = 30
        like_icon_padding_right = 40
        like_icon_padding_bottom = 30
        like_icon_spacing = 12
        
        # Police améliorée
        title_font = ImageFont.truetype(self.font_path, self.title_font_size)
        meta_font = ImageFont.truetype(self.font_path, self.meta_font_size)
        
        # Préparation du texte
        max_chars = 32  # Réduire le nombre de caractères par ligne pour éviter les débordements
        wrapped_title = textwrap.fill(title, width=max_chars)
        
        # Calcul de tailles
        temp_img = Image.new('RGBA', (10, 10), (0,0,0,0))
        temp_draw = ImageDraw.Draw(temp_img)
        title_bbox = temp_draw.textbbox((0, 0), wrapped_title, font=title_font)
        title_width = title_bbox[2] - title_bbox[0]
        title_height = title_bbox[3] - title_bbox[1]
        meta_text = pseudo
        meta_bbox = temp_draw.textbbox((0, 0), meta_text, font=meta_font)
        meta_width = meta_bbox[2] - meta_bbox[0]
        meta_height = meta_bbox[3] - meta_bbox[1]
        
        # Calcul dynamique de la hauteur de la carte
        content_height = title_height + accent_bar_height + 48
        card_height = content_height + 2 * vertical_padding + meta_height + 32
        card_width = self.card_width
        
        # Création de l'image
        image = Image.new('RGBA', (card_width + shadow_offset, card_height + shadow_offset), (0, 0, 0, 0))
        
        # Ombre améliorée avec teinte
        shadow = Image.new('RGBA', (card_width, card_height), (0, 0, 0, 0))
        shadow_draw = ImageDraw.Draw(shadow)
        shadow_draw.rounded_rectangle([(0,0),(card_width,card_height)], radius=border_radius, fill=shadow_color)
        shadow = shadow.filter(ImageFilter.GaussianBlur(blur_radius))
        image.paste(shadow, (shadow_offset, shadow_offset), shadow)
        
        # Création du fond
        card = Image.new('RGBA', (card_width, card_height), (0,0,0,0))
        card_draw = ImageDraw.Draw(card)
        card_draw.rounded_rectangle([(0,0),(card_width-1,card_height-1)], radius=border_radius, fill=bg_color, outline=border_color, width=border_width)
        
        # Effet de motif (circuit/hexagones) si activé
        if pattern_overlay:
            pattern = self._create_futuristic_pattern(card_width, card_height, border_radius, accent_color)
            card = Image.alpha_composite(card, pattern)
        
        # Bordure néon brillante
        if glow_effect:
            glow = Image.new('RGBA', (card_width, card_height), (0,0,0,0))
            glow_draw = ImageDraw.Draw(glow)
            # Dessiner plusieurs rectangles avec des rayons légèrement différents pour l'effet de brillance
            for i in range(3):
                glow_draw.rounded_rectangle([(i*2,i*2),(card_width-1-i*2,card_height-1-i*2)], 
                                         radius=border_radius-i, 
                                         outline=border_color, 
                                         width=1)
            # Flouter pour l'effet de lueur
            glow = glow.filter(ImageFilter.GaussianBlur(radius=8 * glow_intensity))
            card = Image.alpha_composite(card, glow)
        
        # Bordure standard (redessée après les effets)
        card_draw = ImageDraw.Draw(card)
        card_draw.rounded_rectangle([(0,0),(card_width-1,card_height-1)], 
                                  radius=border_radius, 
                                  outline=border_color, 
                                  width=border_width)
        
        # Barre d'accent avec gradient
        gradient_bar = self._create_gradient_bar(
            card_width - 2*card_padding, 
            accent_bar_height, 
            gradient_start, 
            gradient_end
        )
        card.paste(gradient_bar, (card_padding, card_padding), gradient_bar)
        
        # Texte principal (position améliorée)
        title_bbox = card_draw.textbbox((0, 0), wrapped_title, font=title_font)
        title_width = title_bbox[2] - title_bbox[0]
        title_height = title_bbox[3] - title_bbox[1]
        
        # Positionnement plus sûr avec marge fixe depuis le bord
        text_x = card_padding  # Aligné à gauche avec la même marge que la barre d'accent
        text_y = vertical_padding + accent_bar_height + 24
        
        # Effet de lueur pour le texte
        if glow_effect:
            # Créer la lueur du texte
            glow_text = Image.new('RGBA', (card_width, card_height), (0,0,0,0))
            glow_draw = ImageDraw.Draw(glow_text)
            glow_draw.text((text_x, text_y), wrapped_title, 
                         font=title_font, fill=accent_color)
            # Appliquer flou
            glow_text = glow_text.filter(ImageFilter.GaussianBlur(radius=3 * glow_intensity))
            # Ajouter à la carte
            card = Image.alpha_composite(card, glow_text)
        
        # Texte principal (doit être redessé après la lueur avec une opacité complète)
        # Assurer que le texte est parfaitement visible (opacité 255)
        text_color_opaque = text_color[:3] + (255,)  # Forcer l'opacité à 255
        card_draw = ImageDraw.Draw(card)  # Récupérer un nouveau contexte de dessin après les composites
        card_draw.text((text_x, text_y), wrapped_title, 
                     font=title_font, fill=text_color_opaque)
        
        # Pseudo avec effet de badge futuriste
        if show_pseudo:
            pseudo_x = pseudo_padding_left
            pseudo_y = card_height - pseudo_padding_bottom - meta_height
            
            # Badge arrière-plan pour le pseudo
            pseudo_badge_width = meta_width + 40
            pseudo_badge_height = meta_height + 16
            pseudo_badge_x = pseudo_x - 20
            pseudo_badge_y = pseudo_y - 8
            
            # Dessiner le badge
            card_draw.rounded_rectangle(
                [(pseudo_badge_x, pseudo_badge_y), 
                 (pseudo_badge_x + pseudo_badge_width, pseudo_badge_y + pseudo_badge_height)], 
                radius=10, 
                fill=(0, 0, 0, 80),
                outline=secondary_accent, 
                width=2
            )
            
            # Petit accent décoratif sur le badge
            card_draw.line(
                [(pseudo_badge_x + 4, pseudo_badge_y + 4), 
                 (pseudo_badge_x + 14, pseudo_badge_y + 4)], 
                fill=accent_color, 
                width=2
            )
            
            # Texte du pseudo
            card_draw.text((pseudo_x, pseudo_y), meta_text, font=meta_font, fill=(240, 240, 255, 240))
        
        # Likes avec icône futuriste - design épuré
        if show_likes:
            # Créer icône avec effet de lueur
            icon = generate_like_icon(
                size=64, 
                color=like_color, 
                glow=True, 
                glow_intensity=glow_intensity
            )
            icon_w, icon_h = icon.size
            
            # Calculer position
            likes_text_bbox = card_draw.textbbox((0,0), f"{likes_str}", font=meta_font)
            likes_text_w = likes_text_bbox[2] - likes_text_bbox[0]
            like_x = card_width - like_icon_padding_right - icon_w - like_icon_spacing - likes_text_w
            like_y = card_height - like_icon_padding_bottom - icon_h
            
            # Ajouter icône avec effet de lueur
            card.paste(icon, (like_x, like_y), icon)
            
            # Ajouter texte avec effet de lueur
            # Créer une lueur pour le texte des likes
            glow_likes = Image.new('RGBA', (card_width, card_height), (0,0,0,0))
            glow_likes_draw = ImageDraw.Draw(glow_likes)
            glow_likes_draw.text(
                (like_x + icon_w + like_icon_spacing, 
                 like_y + (icon_h - likes_text_bbox[3] + likes_text_bbox[1]) // 2), 
                f"{likes_str}", 
                font=meta_font, 
                fill=like_color
            )
            # Appliquer un léger flou pour l'effet de lueur
            glow_likes = glow_likes.filter(ImageFilter.GaussianBlur(radius=2))
            card = Image.alpha_composite(card, glow_likes)
            
            # Redessiner le texte pour qu'il soit net
            card_draw = ImageDraw.Draw(card)
            card_draw.text(
                (like_x + icon_w + like_icon_spacing, 
                 like_y + (icon_h - likes_text_bbox[3] + likes_text_bbox[1]) // 2), 
                f"{likes_str}", 
                font=meta_font, 
                fill=like_color
            )
        
        # Ajouter effets de lumière si activés
        if light_effects:
            light = self._create_light_effect(card_width, card_height, border_radius)
            card = Image.alpha_composite(card, light)
        
        # Assembler image finale
        image.paste(card, (0, 0), card)
        
        # Sauvegarder si chemin spécifié
        if output_path:
            # Modifier le nom du fichier pour inclure le thème si possible
            if '.' in output_path:
                base, ext = os.path.splitext(output_path)
                themed_output_path = f"{base}_{current_theme}{ext}"
            else:
                themed_output_path = f"{output_path}_{current_theme}.png"
                
            # S'assurer que le dossier parent existe
            parent_dir = os.path.dirname(themed_output_path)
            if parent_dir:
                os.makedirs(parent_dir, exist_ok=True)
            # Sauvegarder l'image avec gestion d'erreur
            try:
                image.save(themed_output_path)
                print(f"Image titre sauvegardée: {themed_output_path} (thème: {current_theme})")
            except Exception as e:
                print(f"Erreur lors de la sauvegarde de l'image: {e}")
                # Essayer de sauvegarder dans le dossier output par défaut
                fallback_path = os.path.join('output', f'title_fallback_{current_theme}.png')
                os.makedirs('output', exist_ok=True)
                image.save(fallback_path)
                return fallback_path
            return themed_output_path
        
        return image

    def create_comment_card(self, comment_text, author, upvotes=0, output_path=None, likes=None, pseudo=None, show_likes=True, show_pseudo=True):
        # Récupérer le nom du thème actuel pour l'utiliser dans le nom du fichier
        current_theme = self.style_manager.get_current_theme_name()
        from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops
        import textwrap
        # Nettoyage du texte commentaire Reddit
        comment_text = re.sub(r'u/[A-Za-z0-9_-]+', '', comment_text)
        comment_text = re.sub(r'r/[A-Za-z0-9_-]+', '', comment_text)
        comment_text = re.sub(r'\b(Edit|EDIT|edit|op|OP|crosspost)\b.*', '', comment_text)
        comment_text = re.sub(r'\n{3,}', '\n\n', comment_text)
        comment_text = comment_text.strip()
        # Pseudo - utiliser l'auteur si disponible, sinon un pseudo fictif
        if pseudo is None:
            if author and str(author) != 'None':
                pseudo = str(author)
            else:
                pseudo = random.choice(self.faux_usernames)
        # Likes stylisés
        effective_show_likes = show_likes and (likes is not None or upvotes)
        likes_val = likes if likes is not None else upvotes if upvotes else random.randint(50, 2000)
        likes_str = f"{likes_val/1000:.1f}k" if likes_val >= 1000 else str(likes_val)
        # Mise en page
        card_padding = 64
        border_radius = 56
        shadow_offset = 24
        vertical_padding = 50
        pseudo_padding_left = 40
        pseudo_padding_bottom = 30
        like_icon_padding_right = 40
        like_icon_padding_bottom = 30
        like_icon_spacing = 12
        # Police
        body_font = ImageFont.truetype(self.font_path, self.body_font_size)
        meta_font = ImageFont.truetype(self.font_path, self.meta_font_size)
        # Texte principal
        max_chars = 44
        wrapped_comment = textwrap.fill(comment_text, width=max_chars)
        temp_img = Image.new('RGBA', (10, 10), (0,0,0,0))
        temp_draw = ImageDraw.Draw(temp_img)
        comment_bbox = temp_draw.textbbox((0, 0), wrapped_comment, font=body_font)
        comment_width = comment_bbox[2] - comment_bbox[0]
        comment_height = comment_bbox[3] - comment_bbox[1]
        meta_text = pseudo
        meta_bbox = temp_draw.textbbox((0, 0), meta_text, font=meta_font)
        meta_width = meta_bbox[2] - meta_bbox[0]
        meta_height = meta_bbox[3] - meta_bbox[1]
        # Calcul dynamique de la hauteur de la carte
        content_height = comment_height + 48
        card_height = content_height + 2 * vertical_padding + meta_height + 32  # 32px d'espace avant pseudo
        card_width = self.card_width
        # Fond transparent
        image = Image.new('RGBA', (card_width + shadow_offset, card_height + shadow_offset), (0, 0, 0, 0))
        # Ombre améliorée avec teinte
        shadow = Image.new('RGBA', (card_width, card_height), (0, 0, 0, 0))
        shadow_draw = ImageDraw.Draw(shadow)
        shadow_draw.rounded_rectangle([(0,0),(card_width,card_height)], radius=border_radius, fill=self.shadow_color)
        shadow = shadow.filter(ImageFilter.GaussianBlur(16))
        image.paste(shadow, (shadow_offset, shadow_offset), shadow)
        
        # Création du fond
        card = Image.new('RGBA', (card_width, card_height), (0,0,0,0))
        card_draw = ImageDraw.Draw(card)
        card_draw.rounded_rectangle([(0,0),(card_width-1,card_height-1)], radius=border_radius, fill=self.card_bg_color, outline=self.border_color, width=6)
        
        # Bordure néon brillante
        glow = Image.new('RGBA', (card_width, card_height), (0,0,0,0))
        glow_draw = ImageDraw.Draw(glow)
        # Dessiner plusieurs rectangles avec des rayons légèrement différents pour l'effet de brillance
        for i in range(3):
            glow_draw.rounded_rectangle([(i*2,i*2),(card_width-1-i*2,card_height-1-i*2)], 
                                     radius=border_radius-i, 
                                     outline=self.border_color, 
                                     width=1)
        # Flouter pour l'effet de lueur
        glow = glow.filter(ImageFilter.GaussianBlur(radius=8 * 2.5))
        card = Image.alpha_composite(card, glow)
        
        # Bordure standard (redessée après les effets)
        card_draw = ImageDraw.Draw(card)
        card_draw.rounded_rectangle([(0,0),(card_width-1,card_height-1)], 
                                  radius=border_radius, 
                                  outline=self.border_color, 
                                  width=6)
        # Texte principal centré horizontalement
        text_x = card_width // 2 - comment_width // 2
        text_y = vertical_padding + 48
        card_draw.text((text_x, text_y), wrapped_comment, font=body_font, fill=self.text_color)
        # Pseudo fictif en bas à gauche
        if show_pseudo:
            pseudo_x = pseudo_padding_left
            pseudo_y = card_height - pseudo_padding_bottom - meta_height
            card_draw.text((pseudo_x, pseudo_y), meta_text, font=meta_font, fill=(220, 220, 255, 220))
        # Likes avec design épuré (en bas à droite)
        if show_likes:
            # Créer icône avec effet de lueur
            icon = generate_like_icon(size=64, color=self.like_color, glow=True, glow_intensity=2.5)
            icon_w, icon_h = icon.size
            likes_text_bbox = card_draw.textbbox((0,0), f"{likes_str}", font=meta_font)
            likes_text_w = likes_text_bbox[2] - likes_text_bbox[0]
            like_x = card_width - like_icon_padding_right - icon_w - like_icon_spacing - likes_text_w
            like_y = card_height - like_icon_padding_bottom - icon_h
            
            # Ajouter icône avec effet de lueur
            card.paste(icon, (like_x, like_y), icon)
            
            # Ajouter texte avec effet de lueur
            # Créer une lueur pour le texte des likes
            glow_likes = Image.new('RGBA', (card_width, card_height), (0,0,0,0))
            glow_likes_draw = ImageDraw.Draw(glow_likes)
            glow_likes_draw.text(
                (like_x + icon_w + like_icon_spacing, 
                 like_y + (icon_h - likes_text_bbox[3] + likes_text_bbox[1]) // 2), 
                f"{likes_str}", 
                font=meta_font, 
                fill=self.like_color
            )
            # Appliquer un léger flou pour l'effet de lueur
            glow_likes = glow_likes.filter(ImageFilter.GaussianBlur(radius=2))
            card = Image.alpha_composite(card, glow_likes)
            
            # Redessiner le texte pour qu'il soit net
            card_draw = ImageDraw.Draw(card)
            card_draw.text(
                (like_x + icon_w + like_icon_spacing, 
                 like_y + (icon_h - likes_text_bbox[3] + likes_text_bbox[1]) // 2), 
                f"{likes_str}", 
                font=meta_font, 
                fill=self.like_color
            )
            
        # Ajouter effets de lumière pour renforcer l'effet de lueur
        light = self._create_light_effect(card_width, card_height, border_radius)
        card = Image.alpha_composite(card, light)
            
        image.paste(card, (0, 0), card)
        if output_path:
            # Modifier le nom du fichier pour inclure le thème si possible
            if '.' in output_path:
                base, ext = os.path.splitext(output_path)
                themed_output_path = f"{base}_{current_theme}{ext}"
            else:
                themed_output_path = f"{output_path}_{current_theme}.png"
                
            # S'assurer que le dossier parent existe
            parent_dir = os.path.dirname(themed_output_path)
            if parent_dir:
                os.makedirs(parent_dir, exist_ok=True)
            # Sauvegarder l'image avec gestion d'erreur
            try:
                image.save(themed_output_path)
                print(f"Image commentaire sauvegardée: {themed_output_path} (thème: {current_theme})")
            except Exception as e:
                print(f"Erreur lors de la sauvegarde de l'image: {e}")
                # Essayer de sauvegarder dans le dossier output par défaut
                fallback_path = os.path.join('output', f'comment_fallback_{current_theme}.png')
                os.makedirs('output', exist_ok=True)
                image.save(fallback_path)
                return fallback_path
            return themed_output_path
        return image

    def _draw_multiline_text(self, draw, text, position, font, fill, max_width, max_height):
        # Wrap le texte automatiquement pour tenir dans la largeur max
        import textwrap
        lines = []
        for paragraph in text.split('\n'):
            wrapped = textwrap.wrap(paragraph, width=60)  # Largeur de base, ajustée ensuite
            for line in wrapped:
                # Ajuster dynamiquement pour la largeur max
                bbox = font.getbbox(line)
                w = bbox[2] - bbox[0]
                while w > max_width and len(line) > 5:
                    line = line[:-1]
                    bbox = font.getbbox(line)
                    w = bbox[2] - bbox[0]
                lines.append(line)
        y = position[1]
        for line in lines:
            bbox = font.getbbox(line)
            line_height = bbox[3] - bbox[1]
            if y + line_height > position[1] + max_height:
                break
            draw.text((position[0], y), line, font=font, fill=fill)
            y += line_height + 6
