# projet 3: Aidez MacGyver à s'échapper !

### Courte description du projet

C'est un jeu de labyrinthe coder en language python,
dont le personnage principale Mac Gyver doit collecter des objets puis endormir le garde qui surveille la sortie du labyrinthe,
afin de remporter la partie en fonction du nombres d'objets collectés.
[Détails du projet](https://openclassrooms.com/fr/projects/aidez-macgyver-a-sechapper/assignment)

### Contraintes et Difficultés Rencontrer

* Suivre les recommandations de la PEP 8 et développer dans un environnement virtuel utilisant Python 3.
* Appréhensions et documentations de pygame (affichage, gestion des évenements etc...).
* l'implémentations des objets, le chargement du fichiers de la générations du labyrinth.
* Methodes de placements des objets sur la cartes.

### Choix Techniques

* Le programme se base sur le module Pygame, notament à cause de son adaptation aux jeux 2D.

- Le programme est découpé en plusieurs modules avec un objectif bien défini:
    - assets contenant les differentes images.
    - Classes contenant les differentes métohdes & classes.
    - Constantes contenant les constantes et le chargements des images.
  
* L'appel entre les modules est effectué dans la fonction main.


Pour installer et executer suivez les instructions suivantes :

* git clone https://github.com/thedev1992/MacgyverGame.git
* python3 macgyver.py on macos/linux or py -3 main.py on windows
