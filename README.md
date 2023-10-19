# TP-Flask

## Introduction

Pour ce projet nous avions a implémenter un site web en flask, pour ce faire nous devions travailler par binôme. Pour le sujet du site, nous avions deux choix:
- Reprendre le travail fait en TD
- Faire un projet à zéro

  Notre choix s'est porté sur cette deuxième option. Peut-être aurions nous pu aller plus loin en reprenant les TD, mais nous avons préféré revoir ce que nous avons vu pour consolider nos acquis.

## Fichier yml

  Comme nous reprenions à zéro, nous avions la possibilité de changer de sujet. Pour ce faire, nous sommes partis sur une liste d'animés en rédigeant manuellement un fichier yml. Dans ce fichier sont stockés des animés et chacun d'entre eux à ces informations suivantes:
  - un auteur, le créateur de l'univers,
  - un illustrateur, car certaines fois l'auteur n'est pas le dessinateur,
  - une image, qui représente l'animé,
  - un nombre d'épisodes, qui représente le nombre d'épisodes actuellement sortis,
  - un titre, le titre de l'animé,
  - une période, qui correspond à la diffusion du premier épisodes et du dernier (si l'animé n'est pas fini alors il est indiqué "en cours")
 
## L'implémentation

  Pour ce travail nous avons utilser git qui permet de simplifier et rendre plus clair le travail en équipe (ici en binôme). De la sorte, nous avons pu travailler en même temps sur des fonctionnalités différentes tout en suivant l'avancée du projet.

  Plusieur branches ont été faites et nous nous sommes répartis le travail équitablement pour aider le projet à avancer correctement.

## Le site web

  Un simple utilisateur peut consulter sur le site les différents animés répertoriés et leurs informations.
  Lors de sa consultation, il peut voir la totalité des animés (seulement les images) ou bien regarder spécifiquement un animé. Lorsqu'il regarde plus en détail il peut swiper d'un animé à un autre.

  Une fois connecté il aura la possibilité de pouvoir modifier les informations de l'auteur d'une oeuvre.


## Les nécessaires de lancement

Pour pouvoir lancer le site, il y a plusieurs pré-requis, les voici :
- il faut avoir créer un virtual environment dont voici les commandes:
  - virtualenv venv
- une fois cela fait, il faut l'activer:
  - sous linux: source venv/bin/activate
  - sous windows: source venv/Scripts/activate
- ensuite, il faut installer tout le nécessaire avec pip install dont:
  - flask
  - python-dotenv
  - flask-sqlalchemy
  - bootstrap-flask
  - flask-wtf
  - pyYAML
  - werkzeug==2.3.7
  - flask-login
- Ensuite, il faut entrer la commande pour créer la bd:
  - flask loaddb anime.yml
- Une fois cela fait, il suffit d'entrer la commande flask run et de se rendre à l'adresse indiqué
