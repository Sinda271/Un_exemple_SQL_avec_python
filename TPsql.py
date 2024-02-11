import pyodbc

# Définissez les parametres de  connexion 
driver = '{Devart ODBC Driver for MySQL}'
server = 'localhost'
port = '3306'
database = 'walmart'
username = 'root'
password = 'password'
 
# ******************** Fonctions *****************************

def create_table(cursor):
    
    # Requette pour créer la table
    query = """CREATE TABLE IF NOT EXISTS WMsales (
	invoice_id  VARCHAR(30) NOT NULL PRIMARY KEY,
	branch  VARCHAR (5) NOT NULL,
    city VARCHAR (30) NOT NULL,
    customer_type VARCHAR (30) NOT NULL,
    gender  VARCHAR(10) NOT NULL,
    product_line VARCHAR (100) NOT NULL,
    unit_price  DECIMAL(10,2) NOT NULL,
    quantity INT NOT NULL,
    VAT  FLOAT(6,4) NOT NULL,
    total DECIMAL (12,4) NOT NULL,
    date DATETIME NOT NULL,
    time TIME NOT NULL,
    payment_method VARCHAR (15)  NOT NULL, 
    cogs  DECIMAL (10, 2) NOT NULL,
    gross_margin_pct FLOAT (11,9),
    gross_income DECIMAL(12, 4) NOT NULL,
    rating FLOAT (3, 1)
    )"""
    
    # Exécuter la requette
    cursor.execute(query)
    
    # Vérifier que la table a été créée avecsuccés
    cursor.execute("SHOW TABLES")
    for x in cursor:
        print(x)
    
    # Charger les données du fichier CSV dans la table WMsales
    query = """
    LOAD DATA INFILE 'chemin_absolut_du_fichier_WalmartSalesData.csv' 
    INTO TABLE WMsales 
    FIELDS TERMINATED BY ',' 
    ENCLOSED BY '"'
    LINES TERMINATED BY '\n' 
    IGNORE 1 ROWS
    """
    cursor.execute(query)
    
    print("CSV chargé avec success")
   
    
def return_table_data(cursor):
    
    # Definir la requette SQL 
    query = "SELECT * FROM WMsales"
    
    # Exécuter la requette
    cursor.execute(query)
    rerults = cursor.fetchall()
    
    # Afficher les résultats
    print(rerults)



if __name__ == '__main__':

    # Se connecter à la base de données MySQL
    conn = pyodbc.connect(
        driver=driver,
        host=server, port=port, database=database, 
        use_pure=True, user=username, password=password
    )

    cursor = conn.cursor()
    
    # Créer la table WMsales dans la base de données walmart
    create_table(cursor=cursor)
    
    # Selectionner toutes les informations de la table WMsales
    return_table_data(cursor=cursor)
    
    # Fermer la connexion
    conn.close()
 