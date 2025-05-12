# Gestion des styles/thèmes pour les cards
# Implémentation de thèmes évolutifs pour TikTok
class StyleManager:
    def __init__(self, config):
        self.config = config
        # Forcer l'activation du thème aléatoire pour s'assurer que les thèmes changent à chaque exécution
        self.random_theme_enabled = True
        # Thèmes prédéfinis
        self.themes = {
            'default': {
                'background': (30, 32, 40, 180),  # glassmorphism
                'border': (180, 180, 255, 90),
                'shadow': (0, 0, 0, 80),
                'text': (255, 255, 255, 240),
                'accent': (0, 255, 255, 220),
                'like': (255, 70, 100, 255),
                'font': 'Montserrat-Regular.ttf',
                'blur_radius': 16,
                'border_width': 6,
                'glow_effect': True
            },
            'neon_future': {
                'background': (15, 22, 40, 190),  # Plus sombre, plus opaque
                'border': (95, 55, 255, 120),  # Violet futuriste
                'shadow': (0, 0, 40, 100),  # Ombre bleue
                'text': (225, 245, 255, 255),  # Blanc bleuté
                'accent': (0, 195, 255, 255),  # Cyan électrique
                'like': (255, 45, 125, 255),  # Rose vif
                'secondary_accent': (170, 0, 255, 255),  # Violet secondaire
                'gradient_start': (80, 25, 180, 255),  # Pour gradients
                'gradient_end': (0, 200, 255, 255),  # Pour gradients
                'font': 'Montserrat-Regular.ttf',  # Fallback à la police existante
                'blur_radius': 24,  # Flou plus fort
                'border_width': 3,  # Bordure plus fine
                'glow_effect': True,
                'glow_intensity': 2.0,  # Intensité du glow
                'pattern_overlay': True,  # Motif hexagonal/circuits
                'light_effects': True  # Effets de lumière dynamiques
            },
            'cyberpunk': {
                'background': (20, 15, 35, 210),  # Violet sombre
                'border': (255, 215, 0, 140),  # Or électrique
                'shadow': (20, 0, 20, 120),
                'text': (245, 240, 255, 255),  # Blanc légèrement violet
                'accent': (255, 230, 0, 255),  # Jaune électrique
                'like': (255, 50, 90, 255),  # Rose vif
                'secondary_accent': (0, 255, 180, 255),  # Turquoise
                'gradient_start': (255, 213, 0, 180),  # Or
                'gradient_end': (255, 90, 40, 180),  # Orange brûlé
                'font': 'Montserrat-Regular.ttf',  # Fallback à la police existante
                'blur_radius': 20,
                'border_width': 4,
                'glow_effect': True,
                'glow_intensity': 2.5,
                'pattern_overlay': True,
                'light_effects': True,
                'noise_overlay': True  # Effet de texture/grain
            },
            "blue_tiktok": {
                "background": (18, 28, 58, 210),          # Bleu nuit profond, glassmorphism
                "border": (0, 120, 255, 120),             # Bleu vif pour la bordure
                "shadow": (0, 40, 120, 100),              # Ombre bleutée
                "text": (230, 245, 255, 255),             # Blanc bleuté très lisible
                "accent": (0, 195, 255, 255),             # Bleu cyan électrique
                "like": (0, 180, 255, 255),               # Bleu plus clair pour le like
                "gradient_start": (0, 195, 255, 255),     # Dégradé bleu cyan
                "gradient_end": (0, 120, 255, 255),       # Dégradé bleu vif
                "secondary_accent": (0, 120, 255, 255),
                "blur_radius": 16,
                "border_width": 6,
                "glow_effect": True,
                "glow_intensity": 2.5,
                "pattern_overlay": False,
                "light_effects": True
            }
        }
        # Sélectionner le thème par défaut, aléatoire ou depuis la config
        if self.random_theme_enabled:
            self.get_random_theme()
        else:
            self.current_theme = self.config.get('theme', 'blue_tiktok')
        
    def get_style(self):
        # Retourne le style/thème courant
        return self.themes.get(self.current_theme, self.themes['default'])
    
    def set_theme(self, theme_name):
        if theme_name in self.themes:
            self.current_theme = theme_name
            return True
        return False
    
    def get_fonts_directory(self):
        from pathlib import Path
        return Path(__file__).parent.parent.parent / "resources" / "fonts"
    
    def get_random_theme(self):
        """Sélectionne un thème aléatoire parmi les thèmes disponibles et le définit comme thème courant."""
        import random
        theme_names = list(self.themes.keys())
        random_theme = random.choice(theme_names)
        self.current_theme = random_theme
        return random_theme
        
    def get_current_theme_name(self):
        """Retourne le nom du thème actuellement utilisé."""
        return self.current_theme
