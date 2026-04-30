# Aide à la décision Hearthstone Batlleground

Hearthstone est un jeu vidéo de cartes. Son mode de jeu de type auto-chess où la prise de décision est le coeur du gameplay : vos tours s'alternent entre phases d'achat de serviteurs pour renforcer votre armée et phase de combat où vos serviteurs se battent automatiquement sans commande de votre part.

L'objectif est donc de créer une armée capable de vaincre vos adversaires. Plusieurs sites proposent des compositions de serviteurs permettant d'obtenir une armée puissante. Le site le plus connu pour cela est (HSReplay.net)[https://hsreplay.net/battlegrounds/comps/].
Cependant, le site manque de de quelques informations cruciales :
- les serviteurs possèdent des archétypes (Mort-vivant, Dragon, ...). Il y a 10 archétypes au total mais uniquement 5 archétypes seront disponibles par partie, rendant certaines compositions impossibles à recréer,
- les compositions se créaient graduellement, il faut donc connaître des cartes "enablers" qui permettent de changer une armée de début de partie en une armée forte de fin de partie. Ces cartes sont indiquées sur la page de chaque composition mais n'est pas pratique puisqu'on ne peut pas voir les enablers de toutes les compos en même temps
- finalement, les pages de compositions sont plutôt longues car elles sont jolies. Cependant, cela n'est pas pratique en partie. On souhaite avoire toutes les informations côte-à-côte afin de minimiser le temps de recherche et maximiser son temps de réflexion avant la prochaine phase.

Ainsi, j'ai crée ce site en utilisant le module streamlit (python) afin de corriger ces erreurs. Le site est basé sur les données de (HSReplay.net)[https://hsreplay.net/battlegrounds/comps/]. Les données que j'ai importé datent de 30/04/26. Le site et les données sont en français.

### Comment lancer le site
#### Installation des modules
Cette partie a besoin d'être lancé une unique fois au moment de l'installation du projet.
Cloner le projet :
```
git clone <liendurepo>
```
Naviguer vers votre dossier :
```
cd ADAD_Hearthstone_battleground
```
Installer les modules :
```
pip install -r requirements.txt
```

#### Lancer le site
Le site est hébergé localement. Afin de le lancer, il faut ouvrir un terminal de commande est allé jusqu'au dossier du projet :
```
cd <moncheminversledossier>
```
puis lancer la commande :
```
streamlit run main.py
```
Le site sera lancé jusqu'à que vous appuyez sur Ctrl+C dans le terminal.

Le site s'ouvrira automatiquement sur votre navigateur. Si ce n'est pas le cas, Shift+ClicGauche sur l'IP affiché dans votre terminal

### Contenu
Dans la barre qui s'affiche, sélectionner les 5 archétypes présents dans votre partie. Rien ne sera affiché tant qu'il n'y a pas exactement 5 archétypes. Après la sélection, des tableaux vont s'afficher. Cette action peut prendre quelques secondes.

Le premier tableau montre les compos disponibles pour votre partie
Le second montre les cartes qui vous permettent de commencer les compos et quelles cartes pour vous concentrer uniquement sur une compo
Quand vous vous engagez sur une compo, vous pouvez choisir la compo sur laquelle vous vous engagez pour voir les cartes Core (obligatoire) et Addon (optionnelle) ainsi qu'une description de comment jouer la composition.