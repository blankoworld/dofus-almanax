Version française un peu plus bas.

# Dofus almanax for the 30 next days

This script give a HTML code that display the 30 next days of Dofus almanax.

You can see result here: [Almanax](http://almanax.depotoi.re "Have a look to the result").

## Dependancies

You need:

  * python
  * python-lxml
  * python-mechanize

## Installation

No installation needed

## How to use it?

In a shell, just do this:

    python almanax_next_week.py > index.html

This will build an index.html file with the 30 next days of almanax.

## Tip

You can use a CRON job on GNU/Linux to often build the page.

Example that launch the script every day at midnight:

    30  0  *   *   *     /usr/bin/python /srv/web/almanax/almanax_next_week.py > /srv/web/almanax/www/index.html

# Almanax Dofus des 30 prochains jours

Ce script renvoie un code HTML qui affiche les 30 prochains jours de l'almanax Dofus.

Vous pouvez voir le résultat ici : [Almanax](http://almanax.depotoi.re "Apercevoir le résultat")

## Dépendances

Vous avez besoin de : 

  * python
  * python-lxml
  * python-mechanize

## Installation

Aucune installation nécessaire

## Comment l'utiliser ?

Dans une console, faites simplement ceci : 

    python almanax_next_week.py > index.html

Cela va construire une page index.html avec les 30 prochains jours de l'almanax.

## Astuce

Vous pouvez utiliser une tâche CRON sur GNU/Linux pour construire la page régulièrement.

Exemple qui lance le script tout les jours à minuit:

    30  0  *   *   *     /usr/bin/python /srv/web/almanax/almanax_next_week.py > /srv/web/almanax/www/index.html

