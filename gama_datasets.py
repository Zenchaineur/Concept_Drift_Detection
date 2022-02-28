import random
import math

"""---

Equilibrage des classes (dans le cas où les données divisées en deux classes) :
"""

def classe_decision(threshold):
    x = random.random()
    if ( x < threshold ):
        return 0
    else :
        return 1

"""---

Ici nous allons définir nos datasets, qui sont ceux de l'article "Learning with Drift Detection" de Gama sorti en 2004, qui ont tous 1000 samples:

1.   **SINE1** : L'ensemble de données a deux attributs pertinents. Chaque attribut a des valeurs uniformément réparties dans
[0; 1]. Dans le premier contexte, tous les points en dessous de la courbe y = sin(x) sont classés comme positif. Après le changement de contexte, la classification est inversée.

2.   **SINE2** : Les deux mêmes attributs pertinents. La fonction de classification est y < 0:5 + 0:3 sin (3 pi x). Après le changement de contexte, la classification est inversée.

3.   **SINIRREL1** : La même fonction de classification que SINE1 mais les exemples ont deux autres attributs aléatoires sans influence sur la fonction de classification.

4.   **SINIRREL2** : La même fonction de classification de SINE2 mais les exemples ont deux autres attributs aléatoires sans influence sur la fonction de classification.

5.   **CIRCLES** : Les attributs sont utilisés avec quatre nouvelles fonctions de classification. Cet ensemble de données a quatre contextes définis par quatre cercles compris dans le carré de taille 1.

6.   **GAUSS** : Exemples positifs avec deux attributs pertinents du domaine R x R qui sont normalement distribués autour du centre [0; 0] avec un écart-type égal à 1. Les exemples négatifs sont normalement distribués autour du centre [2; 0] avec un écart-type égal à 4. Après chaque changement de contexte, la classification est inversée.

7.   **STAGGER** : Les exemples ont trois attributs symboliques - taille (petit, moyen, grand), couleur (rouge, vert), forme (circulaire, non circulaire). Dans le premier contexte seulement les exemples satisfaisant la description size=small ^ color=red sont classifiés positifs. Dans le second contexte, la description du concept est définie par deux attributs, color=green _ shape=circular. Avec le troisième contexte, les exemples sont classés positifs si size=medium _ size= large.

8.   **MIXED** : Quatre attributs pertinents, deux attributs booléens v;w et deux attributs numériques de [0; 1]. Les exemples sont classifiés positifs si deux des trois conditions sont satisfaites : 
v; 
w; 
y < 0:5 + 0:3 sin (3 x). 
Après chaque changement de contexte, la classification est inversée.





"""

def SINE1(drift_number, threshold): 

    scale = 1000 / drift_number

    X = list()
    y = list()

    for j in range (1000):

        context = math.floor( j / scale )
        
        X_elem = list()
        y_elem = classe_decision(threshold)
        y.append(y_elem)

        if (y_elem == abs(context % 2 - 1)):
            
            first = random.random()
            second = random.random()
            while(first > math.sin(second)):
                first = random.random()
                second = random.random()
            X_elem.append(first)
            X_elem.append(second)

        else:
            first = random.random()
            second = random.random()
            while(first <= math.sin(second)):
                first = random.random()
                second = random.random()
            X_elem.append(first)
            X_elem.append(second)

        X.append(X_elem)
    return X,y

def SINE2(drift_number, threshold): 

    scale = 1000 / drift_number

    X = list()
    y = list()

    for j in range (1000):

        context = math.floor( j / scale )
        
        X_elem = list()
        y_elem = classe_decision(threshold)
        y.append(y_elem)

        if (y_elem == abs(context % 2 - 1)):
            first = random.random()
            second = random.random()
            while(first > 0.5+0.3*math.sin(3*math.pi* second)):
                first = random.random()
                second = random.random()
            X_elem.append(first)
            X_elem.append(second)

        else:
            first = random.random()
            second = random.random()
            while(first <= 0.5+0.3*math.sin(3*math.pi* second)):
                first = random.random()
                second = random.random()
            X_elem.append(first)
            X_elem.append(second)

        X.append(X_elem)
    return X,y

def SINIRREL1(drift_number, threshold): 

    scale = 1000 / drift_number

    X = list()
    y = list()

    for j in range (1000):

        context = math.floor( j / scale )
        
        X_elem = list()
        y_elem = classe_decision(threshold)
        y.append(y_elem)

        if (y_elem == abs(context % 2 - 1)):
            
            first = random.random()
            second = random.random()
            while(first > math.sin(second)):
                first = random.random()
                second = random.random()
            X_elem.append(first)
            X_elem.append(second)

        else:
            first = random.random()
            second = random.random()
            while(first <= math.sin(second)):
                first = random.random()
                second = random.random()
            X_elem.append(first)
            X_elem.append(second)

        for u in range (2):
          X_elem.append(random.random())
          
        X.append(X_elem)

    return X,y

def SINIRREL2(drift_number, threshold): 

    scale = 1000 / drift_number

    X = list()
    y = list()

    for j in range (1000):

        context = math.floor( j / scale )
        
        X_elem = list()
        y_elem = classe_decision(threshold)
        y.append(y_elem)

        if (y_elem == abs(context % 2 - 1)):
            
            first = random.random()
            second = random.random()
            while(first > 0.5+0.3*math.sin(3*math.pi* second)):
                first = random.random()
                second = random.random()
            X_elem.append(first)
            X_elem.append(second)

        else:
            first = random.random()
            second = random.random()
            while(first <= 0.5+0.3*math.sin(3*math.pi* second)):
                first = random.random()
                second = random.random()
            X_elem.append(first)
            X_elem.append(second)

        for u in range (2):
          X_elem.append(random.random())

        X.append(X_elem)

    return X,y

def CIRCLES(threshold):

  X = list()
  y = list()

 
  for i in range (250):
      elem = list()
      if(classe_decision(threshold)):

        first = random.random()
        second = random.random()
        while((first - 0.2)**2 + (second - 0.5)**2 <= 0.15**2):
            first = random.random()
            second = random.random()
        elem.append(first)
        elem.append(second)
        y.append(0)

      else:
        t = 2*math.pi*random.random()
        u = random.random()+random.random()
        if (u>1):
          r = 2-u
        else:
          r = u
        first = 0.2 + 0.15 * r * math.cos(t)
        second = 0.5 + 0.15 * r * math.sin(t)
        elem.append(first)
        elem.append(second)

        y.append(1)

      X.append(elem)
  
  for i in range (250,500):
      elem = list()
      if(classe_decision(threshold)):
        first = random.random()
        second = random.random()
        while((first - 0.2)**2 + (second - 0.5)**2 <= 0.15**2):
            first = random.random()
            second = random.random()
        elem.append(first)
        elem.append(second)

        y.append(0)

      else:
        t = 2*math.pi*random.random()
        u = random.random()+random.random()
        if (u>1):
          r = 2-u
        else:
          r = u
        first = 0.4 + 0.2 * r * math.cos(t)
        second = 0.5 + 0.2 * r * math.sin(t)
        elem.append(first)
        elem.append(second)

        y.append(1)

      X.append(elem)

  for i in range (500,750):
      elem = list()
      if(classe_decision(threshold)):
        first = random.random()
        second = random.random()
        while((first - 0.2)**2 + (second - 0.5)**2 <= 0.15**2):
            first = random.random()
            second = random.random()
        elem.append(first)
        elem.append(second)

        y.append(0)

      else:
        t = 2*math.pi*random.random()
        u = random.random()+random.random()
        if (u>1):
          r = 2-u
        else:
          r = u
        first = 0.6 + 0.25 * r * math.cos(t)
        second = 0.5 + 0.25 * r * math.sin(t)
        elem.append(first)
        elem.append(second)
        
        y.append(1)

      X.append(elem)


  for i in range (750,1000):
      elem = list()
      if(classe_decision(threshold)):
        first = random.random()
        second = random.random()
        while((first - 0.2)**2 + (second - 0.5)**2 <= 0.15**2):
            first = random.random()
            second = random.random()
        elem.append(first)
        elem.append(second)
        y.append(0)
      
      else:
        t = 2*math.pi*random.random()
        u = random.random()+random.random()
        if (u>1):
          r = 2-u
        else:
          r = u
        first = 0.8 + 0.3 * r * math.cos(t)
        second = 0.5 + 0.3 * r * math.sin(t)
        elem.append(first)
        elem.append(second)
        
        y.append(1)
      
      X.append(elem)


  return X,y

def GAUSS(threshold):
  return

def STAGGER(threshold):
    changement_context = list()
    for k in range (3):    
        changement_context.append(math.floor(k*1000/3))
    changement_context.append(1000)

    """
    size = {1:"small", 2:"medium", 3:"large"}
    color = {1:"red", 2:"green"}
    shape = {1:"circular", 2:"non-circular"}
    """

    X = list()
    y = list()

    for i in range (333):

        elem = list()

        indice_size1 = random.randrange(1,3)
        indice_size2 = random.randrange(1,3)
        indice_color1 = random.randrange(1,3)
        indice_color2 = random.randrange(1,3)
        indice_shape1 = random.randrange(1,3)
        indice_shape2 = random.randrange(1,3)
        
        if(classe_decision(threshold)):

            elem.append(1)
            elem.append(indice_size2)
            elem.append(indice_color1)
            elem.append(1)
            elem.append(indice_shape1)
            elem.append(indice_shape2)

            y.append(1)
            
        else :

            while(indice_size1 == 1 and indice_color2 == 1):
                indice_size1 = random.randrange(1,3)
                indice_color2 = random.randrange(1,3)

            elem.append(indice_size1)
            elem.append(indice_size2)
            elem.append(indice_color1)
            elem.append(indice_color2)
            elem.append(indice_shape1)
            elem.append(indice_shape2)

            y.append(0)

        X.append(elem)

    for i in range (333,666):

        elem = list()

        indice_size1 = random.randrange(1,3)
        indice_size2 = random.randrange(1,3)
        indice_color1 = random.randrange(1,3)
        indice_color2 = random.randrange(1,3)
        indice_shape1 = random.randrange(1,3)
        indice_shape2 = random.randrange(1,3)
        
        if(classe_decision(threshold)):

            elem.append(indice_size1)
            elem.append(indice_size2)
            elem.append(indice_color1)
            elem.append(2)
            elem.append(indice_shape1)
            elem.append(2)

            y.append(1)

        else :

            while(indice_color2 == 2 and indice_shape2 == 2):
                indice_color2 = random.randrange(1,3)
                indice_shape2 = random.randrange(1,3)

            elem.append(indice_size1)
            elem.append(indice_size2)
            elem.append(indice_color1)
            elem.append(indice_color2)
            elem.append(indice_shape1)
            elem.append(indice_shape2)

            y.append(0)

        X.append(elem)


    for i in range (666,1000):

        elem = list()

        indice_size1 = random.randrange(1,3)
        indice_size2 = random.randrange(1,3)
        indice_color1 = random.randrange(1,3)
        indice_color2 = random.randrange(1,3)
        indice_shape1 = random.randrange(1,3)
        indice_shape2 = random.randrange(1,3)
        
        if(classe_decision(threshold)):

            elem.append(2)
            elem.append(indice_size2)
            elem.append(indice_color1)
            elem.append(indice_color2)
            elem.append(indice_shape1)
            elem.append(indice_shape2)

            y.append(1)

        else :

            elem.append(1)
            elem.append(indice_size2)
            elem.append(indice_color1)
            elem.append(indice_color2)
            elem.append(indice_shape1)
            elem.append(indice_shape2)

            y.append(0)

        X.append(elem)


    return X,y

def MIXED(drift_number, threshold):

  changement_context = list()
  for k in range (drift_number):    
      changement_context.append(math.floor(k*1000/drift_number))
  changement_context.append(1000)

  X = list()
  for i in range (1000):
      elem = list()
      elem.append(random.random())
      elem.append(random.random())
      w = random.randrange(1,3)
      y = random.randrange(1,3)
      if(w==1):
        elem.append(True)
      else:
        elem.append(False)
      if(y==1):
        elem.append(True)
      else:
        elem.append(False)
        
      X.append(elem)

  y = list()

  for j in range (drift_number):
    for l in range (changement_context[0], changement_context[1], 1):
        if((X[l][1]>0.5+0.3*math.sin(3*math.pi* X[l][0])) or X[l][2] or X[l][3]):
            y.append(abs(j % 2 - 1))
        else:
            y.append(abs(j % 2 - 0))

  return X,y

"""---

Cette fonction permet de créer le data set que l'on souhaite utiliser
"""

def creating_dataset(dataset):
  switch={
    "SINE1":SINE1(4, 0.50),
    "SINE2":SINE2(4, 0.50),
    "SINIRREL1":SINIRREL1(4, 0.50),
    "SINIRREL2":SINIRREL2(4, 0.50),
    "CIRCLES":CIRCLES(0.50),
    "GAUSS":GAUSS(0.50),
    "STAGGER":STAGGER(0.50),
    "MIXED":MIXED(5, 0.50),
    }
  return switch.get(dataset,"Invalid input")
