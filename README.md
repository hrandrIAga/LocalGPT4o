# Local GPT4o

## Objectifs

Ce projet a pour objectif de créer une application web (locale) interactive permettant aux utilisateurs de discuter avec le modèle GPT-4 d'OpenAI. L'application permet également d'uploader et d'afficher le contenu de différents types de fichiers (images, PDF, fichiers texte, etc.) qui seront pris en compte dans la réponse.

## Contenu du dépôt

Le dépôt contient les fichiers suivants :

- `app.py` : Le fichier principal de l'application Streamlit.
- `requirements.txt` : Un fichier listant toutes les dépendances python nécessaires pour exécuter l'application.
- `README.md` : Ce fichier, qui fournit des instructions et des informations sur le projet.

## Prérequis

- Python 3.7 ou supérieur
- Un compte OpenAI avec accès à une APi key

## Installation (avec un OS unix)

### 1. Installer Python et pip

Assurez-vous d'avoir Python 3.7 ou supérieur et `pip` soient installés sur votre machine. Vous pouvez télécharger Python depuis le site officiel : [python.org](https://www.python.org/). Suivez les instructions pour votre système d'exploitation pour installer Python et `pip`.

Pour vérifier si Python et `pip` sont installés, vous pouvez exécuter les commandes suivantes dans votre terminal :

```bash
python --version
pip --version
```
### 2. Cloner ce repo Github

```bash
cd [le folder de votre choix]
git clone https://github.com/hrandrIAga/LocalGPT4o.git
cd LocalGPT4o
pip --version
```
### 3. Créer un environnement virtuel
```bash
python3 -m venv env
source env/bin/activate
```
### 4. Installer les libraires python
```bash
python3 -m venv env
source env/bin/activate
```

### 5. Configurer l'API key OpenAI
Modifiez la ligne suivante dans le fichier app.py pour y mettre votre propre clé API OpenAI :
```python
openai.api_key = ""
```
## Utilisation

### 1. Lancer l'application
Pour démarrer l'application Streamlit, exécutez la commande suivante :
```bash
streamlit run app.py
```
Puis cliquer/rendez vous sur l'URL afficher sur le terminal
> localhost:NumeroDePort

### 2. Intéragir avec le modèle

* **Chat :** Entrez du texte dans la barre d'input et cliquez sur "Envoyer" pour interagir avec le modèle GPT-4. Le contenu de la barre d'input sera effacé automatiquement après l'envoi.  
* **Upload des fichiers :** Utilisez le bouton de téléchargement pour charger des fichiers et afficher leur contenu.

### 3. Quitter l'application
a. envoyer 'exit', 'quit' ou 'bye'
b. Sur le terminal tapez CTRL+C
c. Désactiver l'environnemnet virtuel :
```bash
deactivate
```
