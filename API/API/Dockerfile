# Utiliser une image de Python 3.9
FROM python:3.9-slim-buster

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier requirements.txt
COPY requirements.txt requirements.txt

# Installer les dépendances
RUN pip install -r requirements.txt

# Copier le code source
COPY . .

# Exposer le port 8080 pour accéder à l'application
EXPOSE 8080

# Variables d'environnement pour la connexion à la base de données
ENV POSTGRES_USER=test
ENV POSTGRES_PASSWORD=test
ENV POSTGRES_HOST=localhost
ENV POSTGRES_PORT=5344
ENV POSTGRES_DB=employees

# Exécuter le script de création de la base de données
RUN python create_db.py

# Lancer l'application Flask
CMD ["python3", "app.py"]
