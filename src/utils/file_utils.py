def sanitize_filename(filename: str) -> str:
    """
    Nettoie un nom de fichier/dossier en supprimant les caractères problématiques
    """
    # Remplace les espaces par des underscores
    filename = filename.replace(' ', '_')
    # Supprime les caractères spéciaux
    filename = filename.replace('?', '').replace('!', '').replace(':', '').replace(';', '')
    filename = filename.replace(',', '').replace('.', '').replace('/', '').replace('\\', '')
    filename = filename.replace('*', '').replace('|', '').replace('"', '').replace('<', '')
    filename = filename.replace('>', '').replace('(', '').replace(')', '').replace('[', '')
    filename = filename.replace(']', '')
    # Limite la longueur
    return filename[:255]

def generate_slug(title: str) -> str:
    """
    Génère un nom de dossier clean en kebab-case à partir d'un titre
    """
    try:
        # Utiliser sanitize_filename pour nettoyer le titre
        slug = sanitize_filename(title)
        # Remplacer les underscores par des tirets
        slug = slug.replace('_', '-')
        # Limiter à 50 caractères
        return slug[:50]
    except Exception as e:
        print(f"Erreur lors de la génération du slug: {str(e)}")
        return title.strip().lower().replace(' ', '-')[:50]
