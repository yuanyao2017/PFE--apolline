# PFE--apolline

Documentation
============

Ce document présentera les fichier contient, leur fonction, comment les marchent et les parties inachevées.

Fichier
------------
  * Apolline.py
  * Interpolate.py
  * Pipeline.py
  * AjaxHandler.py
  * AjaxHandlerCallback.py
  * Look.py
  * index.html
  * data

Fonction
------------

  * **Apolline.py**
   
  Il lit les donnés de InfluxDB selon le temps donné, et retire les valeurs de CO2. Après il fait des calculs de base. Comme max, min, avg, stdevp.

  * **Interpolate.py Pipeline.py**
  
  Différentes méthodes d'ajustement de données
  
  * **AjaxHandler.py AjaxHandlerCallback.py Look.py index.html**
  
  AjaxHandler est un serveur. AjaxHandlerCallback est une fonction de rappel, quand le serveur reçoit la requête, il appellera AjaxHandlerCallback. La suite AjaxHandlerCallback distribuera la commande au module approprié. Mais il n'a pas fini. Je veux qu'il puisse appeler Look.py quand AjaxHandlerCallback obtient deux paramètres, et afficher le résultat de Look.py. Mais je ne peux pas lier le Javascript avec Python. Il sera moins difficile si on utilise PHP.
  * **data**
  
  Il contient les données recueillies par `rasp8` en janvier. Je les ai divisés en trois catégories. Week-ends (samedi et dimanche) qui devraient être des lisses courbes, jour (08: 00 ~ 17: 30), nuit (17:30 ~ 08: 00). Et lundi soir n'est pas la même que les autres jours, parce que la veille est le dimanche, donc il devrait être une courbe lisse, et les autres jours devrait être tout d'abord déclin puis lisse.
  
  

Fonctionner
------------

Touts les codes peuvent lancés sans paramètres.

  * **Apolline.py**
  
  
Si on veut les lancer directement dans le terminal avec les paramètres. IL doit être modifié: 

~~~python
stime=str(sys.argv[1])+" "+str(sys.argv[2])
ftime=str(sys.argv[3])+" "+str(sys.argv[4])

results = client.query('select * from "events.stats.rasp8" where time >\'%s\' and time <\'%s\';'%(stime,ftime))
~~~
Et on lancer: 

**python3 Apolline.py 2017-01-27 08:00:00.000 2017-01-27 17:30:00.000**
>YYYY-MM-DD HH:MM:SS.mmm. où mmm est le milliseconds.

  * **Interpolate.py Pipeline.py**
  
  Ils lisent les fichier. Donc on peut les modifier:
  
~~~python
f=str(sys.argv[1])

lie=[]
for line in open("%s"%(f)):
    line=line.replace('\n','')
    lie.append(line)
~~~

Et on lancer: 

**python3 Interpolate.py data/neight/20170127neight.txt**

  * **AjaxHandler.py AjaxHandlerCallback.py Look.py index.html**
  
 Quand exécutez **python AjaxHandlerCallback.py**. Il appellera index.html. Nous pouvons ouvrir **localhost: 8080**. Il y a une simple page, mais la opération back-end n'est pas implémenté.
 
 

Problématique
------------

Now a nested list:

 1. L'analyse des données:

      * Il y a maintenant juste des classifications et traitements simple.
      * Si on souhaite appliquer la fonction d'apprentissage supervisé, il exige également beaucoup de données et le jugement humain. Par exemple, le 31/12/2016, il est un jour férié, mais pendant la nuit, il est apparu des fluctuations anormales dans les données. Cette situation ne peut pas être considérée comme une base de comparaison.Mais il est un bon exemple de détection anormale.

 2. Rationaliser les opérations

      * Si on veut que simplifier l'utilisation, on a besoin d'une interface conviviale. Donc, la connexion back-end et python est aussi un problème.
