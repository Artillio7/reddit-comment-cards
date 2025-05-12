def sanitize_filename(filename: str) -> str:
    """
    Nettoie un nom de fichier/dossier en supprimant les caractères problématiques
    """
    import re
    # Utiliser une regex pour remplacer tous les caractères non alphanumériques par des underscores
    # Cela inclut les espaces, les caractères spéciaux, les accents, etc.
    safe_filename = re.sub(r'[^\w\s-]', '_', filename)
    # Remplacer les espaces par des underscores
    safe_filename = re.sub(r'\s+', '_', safe_filename)
    # Supprimer les underscores multiples
    safe_filename = re.sub(r'_+', '_', safe_filename)
    # Supprimer les underscores en début et fin de chaîne
    safe_filename = safe_filename.strip('_')
    # Si le nom est vide après nettoyage, utiliser un nom par défaut
    if not safe_filename:
        safe_filename = 'unnamed_file'
    # Limite la longueur
    return safe_filename[:255]

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
