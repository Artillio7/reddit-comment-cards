from PIL import Image, ImageDraw, ImageFont
import os
from view.style_manager import StyleManager
from model.structures import Post, Comment

class CardGenerator:
    def __init__(self, style_manager: StyleManager):
        # Style vertical TikTok
        self.width = 1080
        self.height = 1920
        self.size = (self.width, self.height)
        self.background_color = (25, 25, 25)
        self.text_color = (255, 255, 255)
        self.accent_color = (255, 69, 0)
        self.card_bg_color = (45, 45, 45, 230)
        self.font_path = self._find_font()
        self.title_font_size = 48
        self.body_font_size = 38
        self.meta_font_size = 30
        os.makedirs("output", exist_ok=True)

    def _find_font(self):
        from pathlib import Path
        possible_paths = [
            Path(__file__).parent.parent.parent / "resources" / "fonts" / "helvetica.ttf",
            Path(__file__).parent.parent.parent / "resources" / "fonts" / "arial.ttf",
            Path(__file__).parent.parent.parent / "resources" / "fonts" / "roboto.ttf",
        ]
        for font_path in possible_paths:
            if os.path.exists(font_path):
                return str(font_path)
        return "arial.ttf"

    def create_title_card(self, title, subreddit, author, output_path=None):
        from PIL import Image, ImageDraw, ImageFont
        import textwrap
        image = Image.new('RGB', self.size, self.background_color)
        draw = ImageDraw.Draw(image)
        title_font = ImageFont.truetype(self.font_path, self.title_font_size)
        meta_font = ImageFont.truetype(self.font_path, self.meta_font_size)
        if not subreddit.startswith("r/"):
            subreddit = f"r/{subreddit}"
        max_chars = int(self.width / (self.title_font_size * 0.5))
        wrapped_title = textwrap.fill(title, width=max_chars)
        card_padding = 40
        title_bbox = draw.textbbox((0, 0), wrapped_title, font=title_font)
        title_width = title_bbox[2] - title_bbox[0]
        title_height = title_bbox[3] - title_bbox[1]
        meta_text = f"Posted by u/{author} on {subreddit}"
        meta_bbox = draw.textbbox((0, 0), meta_text, font=meta_font)
        meta_height = meta_bbox[3] - meta_bbox[1]
        card_width = min(self.width - 80, title_width + card_padding * 2)
        card_height = title_height + meta_height + card_padding * 3
        card_x = (self.width - card_width) // 2
        card_y = (self.height - card_height) // 2 - 100
        shadow_offset = 8
        shadow = Image.new('RGBA', (card_width, card_height), (0, 0, 0, 100))
        image.paste(shadow, (card_x + shadow_offset, card_y + shadow_offset), shadow)
        card = Image.new('RGBA', (card_width, card_height), self.card_bg_color)
        image.paste(card, (card_x, card_y), card)
        accent_bar_height = 6
        accent_bar = Image.new('RGBA', (card_width, accent_bar_height), self.accent_color)
        image.paste(accent_bar, (card_x, card_y), accent_bar)
        title_x = card_x + card_padding
        title_y = card_y + card_padding + accent_bar_height
        draw.text((title_x, title_y), wrapped_title, font=title_font, fill=self.text_color)
        meta_x = card_x + card_padding
        meta_y = title_y + title_height + card_padding
        draw.text((meta_x, meta_y), meta_text, font=meta_font, fill=(200, 200, 200))
        if output_path:
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            image.save(output_path)
            return output_path
        return image

    def create_comment_card(self, comment_text, author, upvotes=0, output_path=None):
        from PIL import Image, ImageDraw, ImageFont
        import textwrap
        image = Image.new('RGB', self.size, self.background_color)
        draw = ImageDraw.Draw(image)
        body_font = ImageFont.truetype(self.font_path, self.body_font_size)
        meta_font = ImageFont.truetype(self.font_path, self.meta_font_size)
        max_chars = int(self.width / (self.body_font_size * 0.6))
        wrapped_comment = textwrap.fill(comment_text, width=max_chars)
        comment_bbox = draw.textbbox((0, 0), wrapped_comment, font=body_font)
        comment_width = comment_bbox[2] - comment_bbox[0]
        comment_height = comment_bbox[3] - comment_bbox[1]
        meta_text = f"u/{author} • {upvotes:,} points"
        meta_bbox = draw.textbbox((0, 0), meta_text, font=meta_font)
        meta_height = meta_bbox[3] - meta_bbox[1]
        card_padding = 40
        card_width = min(self.width - 80, comment_width + card_padding * 2)
        card_height = comment_height + meta_height + card_padding * 3
        card_x = (self.width - card_width) // 2
        card_y = (self.height - card_height) // 2
        shadow_offset = 8
        shadow = Image.new('RGBA', (card_width, card_height), (0, 0, 0, 100))
        image.paste(shadow, (card_x + shadow_offset, card_y + shadow_offset), shadow)
        card = Image.new('RGBA', (card_width, card_height), self.card_bg_color)
        card_draw = ImageDraw.Draw(card)
        card_draw.rectangle((0, 0, card_width-1, card_height-1), outline=(100, 100, 100, 128), width=1)
        image.paste(card, (card_x, card_y), card)
        meta_x = card_padding
        meta_y = card_padding
        card_draw.text((meta_x, meta_y), meta_text, font=meta_font, fill=(180, 180, 180))
        line_y = meta_y + meta_height + card_padding // 2
        card_draw.line([(card_padding, line_y), (card_width - card_padding, line_y)], fill=(100, 100, 100), width=1)
        comment_x = card_padding
        comment_y = line_y + card_padding // 2
        card_draw.text((comment_x, comment_y), wrapped_comment, font=body_font, fill=(255, 255, 255))
        upvote_size = 20
        upvote_x = len(f"u/{author} •") * (self.meta_font_size // 2) + meta_x + 10
        upvote_y = meta_y + (meta_height - upvote_size) // 2
        card_draw.polygon([(upvote_x + upvote_size//2, upvote_y), (upvote_x, upvote_y + upvote_size), (upvote_x + upvote_size, upvote_y + upvote_size)], fill=self.accent_color)
        image.paste(card, (card_x, card_y), card)
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
