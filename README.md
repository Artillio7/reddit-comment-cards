# Générateur de Contenu Reddit

Ce projet permet de collecter et visualiser du contenu Reddit de manière structurée, avec la génération automatique d'images et de fichiers contextuels.

## Fonctionnalités
- Interface en ligne de commande intuitive
- Sélection parmi 21 catégories de contenu
- Pour chaque catégorie :
  - Choix du subreddit
  - Options de tri (top, hot, new, etc.)
  - Période de temps
  - Nombre de posts à traiter
- Génération automatique :
  - Images stylisées pour les titres et commentaires
  - Fichiers Markdown contextuels
  - Organisations des fichiers par dossier
- Support des vidéos et liens dans les posts

## Installation
1. Créez un environnement virtuel Python :
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
```

2. Installez les dépendances :
```bash
pip install -r requirements.txt
```

3. Configurez vos identifiants Reddit :
- Copiez `.env.example` en `.env`
- Remplissez les variables d'environnement avec vos identifiants Reddit

## Utilisation
```bash
python -m src.main
```

Le programme vous guidera à travers les étapes suivantes :
1. Choisissez le nombre de posts à traiter (1-20)
2. Sélectionnez une catégorie de contenu
3. Choisissez une option spécifique (subreddit, tri, période)
4. Le programme générera automatiquement :
   - Des images pour chaque post et commentaire
   - Des fichiers Markdown avec le contexte
   - Tout sera sauvegardé dans un dossier organisé

## Structure du projet
- `src/`
  - `controller/` : Logique métier
  - `model/` : Gestion des données et interaction Reddit
  - `view/` : Génération des images et styles
  - `main.py` : Point d'entrée du programme

## Dépendances
Voir `requirements.txt` pour la liste complète des dépendances nécessaires.
