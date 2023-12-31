## FastAPI_GenAno
Le code fourni est un serveur FastAPI permettant de générer des nombres aléatoires, de les stocker dans un fichier CSV et de chiffrer ou déchiffrer les données d'un fichier CSV.### Voici les étapes pour appliquer les différentes fonctionnalités du code via l'URL http://localhost:8000/docs :
### Voici les étapes pour utiliser les différentes fonctionnalités du code via l'URL http://localhost:8000/docs :
1. Exécution du serveur FastAPI :

* Assurez-vous d'avoir installé FastAPI et ses dépendances.
* Lancez le serveur FastAPI en exécutant le code sur votre machine locale:
    * Utilisez un terminal pour vous rendre dans le répertoire du projet et exécuter la commande suivante:
    * uvicorn main:app --reload
  

2. Accès à l'interface Swagger UI :

Ouvrez votre navigateur et accédez à l'URL http://localhost:8000/docs.
Vous verrez une interface Swagger UI conviviale qui répertorie toutes les routes disponibles dans l'API.


3. Route GET "/" :Cette route renvoie un message de salutation "Hello world" pour vérifier que l'API fonctionne correctement.

* Cliquez sur la route "/" pour voir les détails de la route, y compris sa méthode (GET), son chemin ("/") et une description.
* Pour exécuter la route, cliquez sur le bouton "Try it out" puis sur le bouton "Execute".
* Le résultat s'affichera dans la section "Response".

4. Route POST "/generate" :Cette route génère des données aléatoires en fonction des paramètres spécifiés.

* Cliquez sur la route "/generate" pour voir les détails.
* Pour exécuter la route, cliquez sur le bouton "Try it out" puis dans la section "Request body", vous verrez un exemple d'objet JSON attendu avec les attributs "min_value", "max_value" et "count".
Exemple :{
"count": 10,
"min_value": 0,
"max_value": 100
} 
* Modifiez les valeurs selon vos besoins ou utilisez l'exemple fourni.
* Cliquez sur "Execute" pour exécuter la route et obtenir les données générées dans la section "Response".

5. Route POST "/generate_and_store" :Cette route génère des données aléatoires et les enregistre dans un fichier CSV.

* Cliquez sur la route "/generate_and_store" pour voir les détails.
* Pour exécuter la route, cliquez sur le bouton "Try it out" et ensuite Dans la section "Request body", vous verrez un exemple d'objet JSON attendu avec les attributs "num_rows", "file_path" et "column_types".exemple:{
    "num_rows": 10,
    "file_path": "C:/Users/hp/Desktop/fastApi_resultat/random_data.csv",
    "column_types": {
        "id": "int",
        "name": "str",
        "age": "int",
        "is_student": "bool"
    }
* Modifiez les valeurs selon vos besoins ou utilisez l'exemple fourni.
* Cliquez sur "Execute" pour exécuter la route et vérifiez le message de réussite ou d'erreur dans la section "Response".


6. Route PUT "/update":Cette route met à jour une ligne spécifique dans un fichier CSV.

* Cliquez sur la route "/update" pour voir les détails.
* Pour exécuter la route, cliquez sur le bouton "Try it out" et ensuite Dans la section "Request body", vous verrez un exemple d'objet JSON attendu avec les attributs "file_path", "line_number" et "new_values".exemple:
{
    "file_path": "C:/Users/hp/Desktop/fastApi_resultat/random_data.csv",
    "line_number": 2,
    "new_values": {
       "id": 100,
        "name": "azerty",
        "age": 20,
        "is_student": "False"
        
    }
* Modifiez les valeurs selon vos besoins ou utilisez l'exemple fourni.
* Cliquez sur "Execute" pour exécuter la route et vérifiez le message de réussite ou d'erreur dans la section "Response".


7. Route DELETE "/delete"  :Cette route supprime une ligne spécifique d'un fichier CSV.
* Cliquez sur la route "/delete" pour voir les détails.
* Pour exécuter la route, cliquez sur le bouton "Try it out" et ensuite Dans la section "Request body", vous verrez un exemple d'objet JSON attendu. Modifiez les valeurs selon vos besoins ou utilisez l'exemple fourni. 
* exemple pour supprimer une ligne d'un fichier csv  :
{
    "file_path": "C:/Users/hp/Desktop/fastApi_resultat/random_data.csv",
    "line_number": 2
}
* exemple pour supprimer un fichier csv:
{
  "file_path":"C:/Users/hp/Desktop/fastApi_resultat/random_data.csv",
  "delete_file": true
}
* Vérifiez la section "Response" pour voir le résultat de la fonction. Vous obtiendrez un message indiquant si la ligne a été supprimée avec succès ou s'il y a eu une erreur.

8. Route POST /encrypt_file: chiffrer ou déchiffrer les données d'un fichier CSV en utilisant l'algorithme AES-256-CBC ou de hasher les données en utilisant l'algorithme SHA256. L'API prend en entrée le chemin du fichier source, le chemin du fichier de sortie, l'opération à effectuer (chiffrement, déchiffrement ou hashage), la clé de chiffrement, le mode de chiffrement, le vecteur d'initialisation, les colonnes à chiffrer/déchiffrer (optionnel), le séparateur de champ (optionnel) et retourne le fichier de sortie modifié.
*  Cliquez sur la route "/encrypt_file" pour voir les détails 
* Pour exécuter la route, cliquez sur le bouton "Try it out" puis dans la section "Request body", vous verrez un exemple d'objet JSON attendu. Modifiez les valeurs selon vos besoins ou utilisez l'exemple fourni. Par exemple :
   { "fichier_entree": "C:/Users/hp/Desktop/fastApi_resultat/random_data.csv",
    "fichier_sortie": "C:/Users/hp/Desktop/fastApi_resultat/data.csv",
    "operation": "chiffrement",
    "cle_chiffrement": "ma_cle_secrete12",
    "mode_chiffrement": "CBC",
    "vecteur": "monvecteursecret",
    "colonnes": "id",
    "separateur": ","

} 
* Vérifiez la section "Response" pour voir le résultat de la fonction. Vous obtiendrez un message indiquant si le traitement du fichier a été effectué avec succès ou s'il y a eu une erreur.
* ### Le code importe également les modules random et csv, ainsi que le module fct (contient les fct de chiffrement,dechiffrement et hachage), et définit les modèles de données RandomData et RandomData1 à l'aide de la bibliothèque Pydantic.# fastapi_encrypt
