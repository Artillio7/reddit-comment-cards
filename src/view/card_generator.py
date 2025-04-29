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
        # Palette personnalisable
        default_palette = {
            'background': (30, 32, 40, 180),  # glassmorphism
            'border': (180, 180, 255, 90),
            'shadow': (0, 0, 0, 80),
            'text': (255, 255, 255, 240),
            'accent': (0, 255, 255, 220),
            'like': (255, 70, 100, 255),
        }
        self.palette = palette or default_palette
        self.text_color = self.palette['text']
        self.accent_color = self.palette['accent']
        self.card_bg_color = self.palette['background']
        self.border_color = self.palette['border']
        self.shadow_color = self.palette['shadow']
        self.like_color = self.palette['like']
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

    def create_title_card(self, title, subreddit, author, output_path=None, likes=None, pseudo=None):
        from PIL import Image, ImageDraw, ImageFont
        import textwrap
        # Pseudo fictif
        pseudo = pseudo or random.choice(self.faux_usernames)
        # Likes stylisés
        show_likes = self.show_likes if likes is None else bool(likes)
        likes_val = likes if likes is not None else random.randint(120, 4200)
        likes_str = f"{likes_val/1000:.1f}k" if likes_val >= 1000 else str(likes_val)
        # Mise en page
        card_padding = 64
        accent_bar_height = 10
        border_radius = 56
        shadow_offset = 24
        vertical_padding = 50
        pseudo_padding_left = 40
        pseudo_padding_bottom = 30
        like_icon_padding_right = 40
        like_icon_padding_bottom = 30
        like_icon_spacing = 12
        # Police
        title_font = ImageFont.truetype(self.font_path, self.title_font_size)
        meta_font = ImageFont.truetype(self.font_path, self.meta_font_size)
        # Texte principal
        max_chars = 38
        wrapped_title = textwrap.fill(title, width=max_chars)
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
        card_height = content_height + 2 * vertical_padding + meta_height + 32  # 32px d'espace avant pseudo
        card_width = self.card_width
        # Fond transparent
        image = Image.new('RGBA', (card_width + shadow_offset, card_height + shadow_offset), (0, 0, 0, 0))
        # Ombre douce
        shadow = Image.new('RGBA', (card_width, card_height), (0, 0, 0, 0))
        shadow_draw = ImageDraw.Draw(shadow)
        shadow_draw.rounded_rectangle([(0,0),(card_width,card_height)], radius=border_radius, fill=self.shadow_color)
        shadow = shadow.filter(ImageFilter.GaussianBlur(16))
        image.paste(shadow, (shadow_offset, shadow_offset), shadow)
        # Carte glassmorphism
        card = Image.new('RGBA', (card_width, card_height), (0,0,0,0))
        card_draw = ImageDraw.Draw(card)
        card_draw.rounded_rectangle([(0,0),(card_width-1,card_height-1)], radius=border_radius, fill=self.card_bg_color, outline=self.border_color, width=6)
        # Effet lumineux (néon)
        neon_radius = border_radius + 12
        card_draw.rounded_rectangle([(8,8),(card_width-9,card_height-9)], radius=neon_radius, outline=self.accent_color, width=3)
        # Barre d'accent
        card_draw.rounded_rectangle([(card_padding, card_padding), (card_width-card_padding, card_padding+accent_bar_height)], radius=accent_bar_height//2, fill=self.accent_color)
        # Texte principal centré horizontalement
        text_x = card_width // 2 - title_width // 2
        text_y = vertical_padding + accent_bar_height + 48
        card_draw.text((text_x, text_y), wrapped_title, font=title_font, fill=self.text_color)
        # Pseudo fictif en bas à gauche
        pseudo_x = pseudo_padding_left
        pseudo_y = card_height - pseudo_padding_bottom - meta_height
        card_draw.text((pseudo_x, pseudo_y), meta_text, font=meta_font, fill=(220, 220, 255, 220))
        # Likes (en bas à droite)
        if show_likes:
            icon = generate_like_icon(size=64, color=self.like_color)
            icon_w, icon_h = icon.size
            likes_text_bbox = card_draw.textbbox((0,0), f"{likes_str}", font=meta_font)
            likes_text_w = likes_text_bbox[2] - likes_text_bbox[0]
            like_x = card_width - like_icon_padding_right - icon_w - like_icon_spacing - likes_text_w
            like_y = card_height - like_icon_padding_bottom - icon_h
            card.paste(icon, (like_x, like_y), icon)
            # Texte likes aligné verticalement au centre de l'icône
            card_draw.text((like_x + icon_w + like_icon_spacing, like_y + (icon_h - likes_text_bbox[3] + likes_text_bbox[1]) // 2), f"{likes_str}", font=meta_font, fill=self.like_color)
        image.paste(card, (0, 0), card)
        if output_path:
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            image.save(output_path)
            return output_path
        return image

    def create_comment_card(self, comment_text, author, upvotes=0, output_path=None, likes=None, pseudo=None):
        from PIL import Image, ImageDraw, ImageFont
        import textwrap
        # Nettoyage du texte commentaire Reddit
        comment_text = re.sub(r'u/[A-Za-z0-9_-]+', '', comment_text)
        comment_text = re.sub(r'r/[A-Za-z0-9_-]+', '', comment_text)
        comment_text = re.sub(r'\b(Edit|EDIT|edit|op|OP|crosspost)\b.*', '', comment_text)
        comment_text = re.sub(r'\n{3,}', '\n\n', comment_text)
        comment_text = comment_text.strip()
        # Pseudo fictif
        pseudo = pseudo or random.choice(self.faux_usernames)
        # Likes stylisés
        show_likes = self.show_likes if likes is None else bool(likes)
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
        # Ombre douce
        shadow = Image.new('RGBA', (card_width, card_height), (0, 0, 0, 0))
        shadow_draw = ImageDraw.Draw(shadow)
        shadow_draw.rounded_rectangle([(0,0),(card_width,card_height)], radius=border_radius, fill=self.shadow_color)
        shadow = shadow.filter(ImageFilter.GaussianBlur(16))
        image.paste(shadow, (shadow_offset, shadow_offset), shadow)
        # Carte glassmorphism
        card = Image.new('RGBA', (card_width, card_height), (0,0,0,0))
        card_draw = ImageDraw.Draw(card)
        card_draw.rounded_rectangle([(0,0),(card_width-1,card_height-1)], radius=border_radius, fill=self.card_bg_color, outline=self.border_color, width=6)
        # Effet lumineux (néon)
        neon_radius = border_radius + 12
        card_draw.rounded_rectangle([(8,8),(card_width-9,card_height-9)], radius=neon_radius, outline=self.accent_color, width=3)
        # Texte principal centré horizontalement
        text_x = card_width // 2 - comment_width // 2
        text_y = vertical_padding + 48
        card_draw.text((text_x, text_y), wrapped_comment, font=body_font, fill=self.text_color)
        # Pseudo fictif en bas à gauche
        pseudo_x = pseudo_padding_left
        pseudo_y = card_height - pseudo_padding_bottom - meta_height
        card_draw.text((pseudo_x, pseudo_y), meta_text, font=meta_font, fill=(220, 220, 255, 220))
        # Likes (en bas à droite)
        if show_likes:
            icon = generate_like_icon(size=64, color=self.like_color)
            icon_w, icon_h = icon.size
            likes_text_bbox = card_draw.textbbox((0,0), f"{likes_str}", font=meta_font)
            likes_text_w = likes_text_bbox[2] - likes_text_bbox[0]
            like_x = card_width - like_icon_padding_right - icon_w - like_icon_spacing - likes_text_w
            like_y = card_height - like_icon_padding_bottom - icon_h
            card.paste(icon, (like_x, like_y), icon)
            # Texte likes aligné verticalement au centre de l'icône
            card_draw.text((like_x + icon_w + like_icon_spacing, like_y + (icon_h - likes_text_bbox[3] + likes_text_bbox[1]) // 2), f"{likes_str}", font=meta_font, fill=self.like_color)
        image.paste(card, (0, 0), card)
        if output_path:
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            image.save(output_path)
            return output_path
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
