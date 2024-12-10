# **Comment jouer au jeu Blokus**

Ce guide explique comment jouer au jeu Blokus en utilisant le fichier `main.py`.

---

## **1. Lancement du jeu**

### Étape 1 : Démarrer le script
- Exécutez le fichier `main.py` en utilisant Python.
- Lors du démarrage, le programme demande le nombre de joueurs :
  - **2 joueurs** ou **4 joueurs** sont autorisés.
- Si vous choisissez **2 joueurs**, chaque joueur contrôle deux ensembles de pièces.

### Étape 2 : Entrer les noms des joueurs
- Chaque joueur doit entrer un nom unique.
- En cas de duplication de nom, le programme demandera un autre nom.

---

## **2. Déroulement de la partie**

Le jeu se joue en tours successifs, chaque joueur jouant à son tour.

### Tour d’un joueur
1. **Afficher les pièces restantes** : Le joueur voit les pièces qu’il peut encore utiliser.
2. **Afficher les cases valides** : Les cases où le joueur peut poser une pièce sont mises en **blanc** sur la grille.
3. **Choisir une pièce** : Saisissez le numéro correspondant à la pièce souhaitée.
4. **Transformation de la pièce** :
   - **Rotation** : Tournez la pièce de 90°, -90°, ou 180°.
   - **Symétrie** : Appliquez une symétrie horizontale.
   - Si aucune transformation n’est nécessaire, validez directement la pièce.
5. **Placer la pièce** :
   - Sélectionnez les coordonnées de la grille où placer la pièce.
   - Définissez le point d’ancrage de la pièce.
6. **Validation** :
   - Le programme vérifie si le placement respecte les règles.
   - Si le placement est invalide, vous devez recommencer.

---

## **3. Règles principales**

### **Placement initial**
- La première pièce doit être placée de manière à toucher un **coin attribué** au joueur.

### **Placement ultérieur**
- Chaque pièce doit toucher au moins une autre pièce de la même couleur par un **coin**.
- Une pièce **ne doit pas** toucher une autre pièce de la même couleur par un **bord**.
- Les pièces peuvent toucher les pièces d’autres joueurs sans restrictions.

### **Limites du plateau**
- Les pièces doivent être entièrement dans les limites de la grille 20x20.
- Une pièce ne peut pas chevaucher une pièce existante.

---

## **4. Fin de la partie**

La partie se termine lorsque :
1. Tous les joueurs sont bloqués.
2. Aucun joueur ne peut poser une pièce légalement.

### **Calcul des scores**
- Chaque joueur perd **1 point** pour chaque carré restant dans ses pièces non placées.
- Bonus :
  - Si un joueur place **toutes ses pièces**, il reçoit un **bonus de +15 points**.
  - Si la dernière pièce placée est un carré simple, un **bonus supplémentaire de +5 points** est accordé.
- Le joueur avec le score le plus élevé gagne.

---

## **5. Couleurs et affichage**
- Chaque joueur est associé à une couleur unique :
  - **Cyan** : Joueur 1
  - **Violet** : Joueur 2
  - **Vert** : Joueur 3
  - **Rouge** : Joueur 4
- Les pièces et le plateau s’affichent avec ces couleurs.
- Les cases où le joueur actuel peut poser une pièce sont affichées en **blanc** pour faciliter la sélection.

---

## **6. Code principal**

Le fichier `main.py` contient les éléments suivants :
- **Initialisation du plateau** : Création d’une grille vide et gestion des joueurs.
- **Tour par tour** : Le programme gère les transformations, la validation et le placement des pièces.
- **Validation des règles** : Utilise des fonctions dans les modules annexes pour vérifier les règles du jeu.

---

Amusez-vous bien avec Blokus !
