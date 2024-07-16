# Document Similarity Finder


## Ce projet est conçu pour trouver et afficher des documents similaires à un titre de document donné. Il utilise des techniques d'apprentissage automatique et de traitement du langage naturel pour analyser et comparer les titres de documents en termes de similarité.

## Fonctionnalités
- **Entrée du titre**: Les utilisateurs peuvent entrer le titre d'un document qu'ils souhaitent trouver des documents similaires.
- **Classement de similarité**: L'application classe les documents en fonction de leur similarité avec le titre d'entrée et affiche les 5 documents les plus similaires.

## Fonctionnement
1. **Traitement des données**: L'application commence par lire un ensemble de titres de documents à partir d'un fichier CSV.
2. **Entrée de l'utilisateur**: L'utilisateur est invité à entrer le titre d'un document qui l'intéresse.
3. **Traitement des documents**: Le titre d'entrée ainsi que les titres de l'ensemble de données sont traités pour la comparaison de similarité.
4. **Calcul de similarité**: L'application calcule la similarité cosinus entre le titre du document d'entrée et chaque titre de l'ensemble de données.
5. **Affichage des résultats**: Les 5 titres de documents les plus similaires sont affichés à l'utilisateur.

## Technologies utilisées
- Python
- Streamlit pour l'interface web
- Scikit-learn pour les opérations d'apprentissage automatique
- Pandas pour la manipulation des données

## Configuration et installation
1. Clonez le dépôt sur votre machine locale.
2. Installez les dépendances requises:
