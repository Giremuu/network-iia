# Cahier des charges

## Contraintes techniques avérées:
- Réaliser avec PlantUML (étendue par VSCode) le diagramme de classe de
la tram Ethernet / du paquet IP du SI et du Switch L2 / L3. Déterminer
l’association existant entre eux
- Réaliser en Python une classe Switch qui correspond au diagramme de
classe réalisé précédemment. Créer une classe mère L2Switch et une
classe enfant L3Switch,
- Utiliser les principes GRAPS et Solid pour définir des comportements
spécifiques à la classe L3Switch malgré certains comportements homonymes
à ceux de sa classe mère.
- Réaliser avec PlantUML le diagramme de classe de l’utilisateur du SI et
du poste de travail. Déterminer l’association existant entre eux
- Réaliser en Python une classe User qui correspond au diagramme de classe
réalisé précédemment
- Réaliser en C++ une classe User
- Déterminer les différences syntaxiques et techniques existant entre les
deux langages de programmation sous l’angle de l’implémentation de cette
classe.

## Objectifs clefs:
- Bien définir aussi bien au niveau des diagrammes que de l’implémentation
des comportements différents entre les switchL2 et le switchL3 malgré
l’existence de comportements similaires et de Users
- C++
- Python

## Différences Python / C++ :
- C++ est plus bas niveau que Python
- C++ est un language à typage statique (Faut définir le type des variables lors de l'initialisation de ces dernières) alors que Python c'est du typage dynamique
- L'écriture dans la console ou même les string en C++ demande des modules importés ou de les recréé

