Version française un peu plus bas.

# Dofus almanax for the 15 next days

This script give a HTML code that display the 15 next days of Dofus almanax.

You can see result here: [Almanax](https://almanax.o9.re "Have a look to the result").

**LICENSE**: This program is under WTFPL conditions (Cf. https://en.wikipedia.org/wiki/WTFPL).

## Dependancies

You need:

  * python3
  * python-lxml
  * python-mechanize

## Installation

No installation needed

## How to use it?

In a shell, just do this:

    cd src
    python almanax_next_week.py > index.html

This will build an index.html file with the 15 next days of almanax.

## Tip

You can use a CRON job on GNU/Linux to often build the page.

Example that launch the script every day at midnight:

    30  0  *   *   *     /usr/bin/python /srv/web/almanax/almanax_next_week.py > /srv/web/almanax/www/index.html

# Almanax Dofus des 15 prochains jours

Ce script renvoie un code HTML qui affiche les 15 prochains jours de l'almanax Dofus.

Vous pouvez voir le résultat ici : [Almanax](https://almanax.o9.re "Apercevoir le résultat")

**LICENCE** : Cette application est délivrée sous les conditions de LPRAB (Cf. https://fr.wikipedia.org/wiki/WTFPL)


## Dépendances

Vous avez besoin de : 

  * python3
  * python-lxml
  * python-mechanize

## Installation

Aucune installation nécessaire

## Comment l'utiliser ?

Dans une console, faites simplement ceci : 

    cd src
    python almanax_next_week.py > index.html

Cela va construire une page index.html avec les 15 prochains jours de l'almanax.

## Astuce

Vous pouvez utiliser une tâche CRON sur GNU/Linux pour construire la page régulièrement.

Exemple qui lance le script tout les jours à minuit:

    30  0  *   *   *     /usr/bin/python /srv/web/almanax/src/almanax_next_week.py > /srv/web/almanax/src/index.html

