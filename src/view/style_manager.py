# Gestion des styles/thèmes pour les cards
# (sera rempli pour permettre des thèmes évolutifs)
class StyleManager:
    def __init__(self, config):
        self.config = config
        # Charger les paramètres de style depuis config
    def get_style(self):
        # Retourne le style courant (couleurs, polices, etc.)
        return self.config.get('card_style', {})
