"""
# Blokus - Règles Officielles
Ce fichier contient la documentation des règles officielles de Blokus sous forme de commentaires explicites.
Blokus est un jeu de stratégie pour 2 à 4 joueurs où le but est de placer toutes ses pièces sur le plateau
en suivant des règles spécifiques.

## Composants du jeu :
- 1 plateau de jeu de 20x20 cases.
- 4 ensembles de 21 pièces chacun, chaque ensemble ayant une couleur unique (cyan, violet, rouge, vert).
- Les 21 pièces de chaque joueur incluent différentes formes géométriques basées sur des carrés.

"""

# ----------------------------------------------
# 1. Objectif du jeu
# ----------------------------------------------
"""
L'objectif principal de Blokus est de placer le plus grand nombre possible de ses pièces sur le plateau.
Les joueurs gagnent des points en fonction des pièces qu'ils ont réussi à poser, et des pénalités sont infligées
pour les pièces restantes à la fin de la partie. Le joueur ayant le score le plus élevé gagne.
"""

# ----------------------------------------------
# 2. Déroulement de la partie
# ----------------------------------------------
"""
- La partie se joue en tours successifs dans le sens horaire.
- Chaque joueur commence par placer une de ses pièces sur le plateau.
- Le jeu continue jusqu'à ce qu'aucun joueur ne puisse poser une pièce légale.

**Tour d’un joueur :**
1. Choisir une pièce parmi celles encore disponibles.
2. Placer cette pièce sur le plateau en respectant les règles de placement.
3. Si un joueur ne peut pas jouer, il passe son tour.

"""

# ----------------------------------------------
# 3. Règles de placement
# ----------------------------------------------
"""
- **Placement initial :**
  Chaque joueur doit poser sa première pièce de manière à ce qu'elle touche un coin du plateau qui lui est assigné.

- **Placement ultérieur :**
  1. Chaque nouvelle pièce doit toucher au moins une autre pièce de la même couleur **par un coin**.
  2. Une pièce ne peut jamais être placée de manière à toucher une autre pièce de la même couleur **par un bord**.
  3. Les pièces peuvent toucher les pièces d'autres joueurs, sans restrictions.

- **Restriction d'espace :**
  Les pièces doivent être entièrement placées dans les limites du plateau de 20x20 cases.
  Une pièce ne peut pas chevaucher une pièce déjà posée.

"""

# ----------------------------------------------
# 4. Fin de la partie
# ----------------------------------------------
"""
La partie se termine lorsque :
1. Aucun joueur ne peut plus poser de pièce légalement.
2. Tous les joueurs passent leur tour consécutivement.

**Calcul des scores :**
- Chaque joueur perd 1 point pour chaque carré (ou "bloc") des pièces restantes.
- Bonus :
  - Si un joueur place toutes ses pièces, il reçoit un bonus de +15 points.
  - Si la dernière pièce placée est le carré simple, un bonus supplémentaire de +5 points est accordé.
Le joueur avec le score le plus élevé gagne.

"""

# ----------------------------------------------
# 5. Variantes
# ----------------------------------------------
"""
**Mode 2 joueurs :**
- Chaque joueur contrôle 2 couleurs (42 pièces au total).
- Les joueurs alternent entre les deux couleurs pendant la partie.

**Mode 3 joueurs :**
- Une couleur reste inutilisée, et les joueurs jouent normalement avec leurs couleurs respectives.

"""