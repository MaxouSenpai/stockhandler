# stockhandler

Ce programme servira de stockhandler (c'est dans le titre) avec un lecteur de codes barres

Ici, il utilise un db.py pour aller chercher ses données.

Dans un premier temps, il fonctionnera en local avec une liste de prix insérée dans le db.py et affichera simplement les prix ainsi que le total des prix en scannant des codes bar. à therme, il sera possible de scanner sa carte membre UrLAB avec les produits pour instantanément mettre a jour l'ardoise ainsi que permettre d'indiquer dans une API quelles produits restent au HS (et pourquoi pas mettre tout ça en page sur le site)

# Lancement

	python3 scann.py