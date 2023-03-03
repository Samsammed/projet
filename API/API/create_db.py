import mysql.connector

# Créer une connexion à la base de données
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="entreprise"
)

# Création de la table employees
cur = conn.cursor()
cur.execute("""CREATE TABLE employees (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    firstName VARCHAR(255) NOT NULL,
                    lastName VARCHAR(255) NOT NULL,
                    emailId VARCHAR(255) NOT NULL
                );""")

conn.commit()
cur.close()

# Fermer la connexion à la base de données
conn.close()
