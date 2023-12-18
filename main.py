import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from sqlalchemy.orm import declarative_base, sessionmaker
from fct import aes_encrypt, aes_decrypt, sha256_hash
import pandas as pd


app = FastAPI()

DATABASE_URL = "sqlite:///./test.db" 

engine = create_engine(DATABASE_URL)
Base = declarative_base()

metadata = MetaData()

# Define the database table
encryption_table = Table(
    "encryption_data",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("original_value", String, nullable=False),
    Column("encrypted_value", String, nullable=False),
)

# Create the table
metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class RandomData(BaseModel):
    min_value: int
    max_value: int
    count:int

@app.get("/")
async def root():
 return {"greeting":"Hello world"}


class EncryptFileInput(BaseModel):
    fichier_entree: str=None
    fichier_sortie: str=None
    operation: str=None
    cle_chiffrement: str=None
    mode_chiffrement: str=None
    vecteur: str=None
    colonnes: str = None
    separateur: str = None


@app.post("/encrypt_file")
async def encrypt_file_endpoint(input_data: EncryptFileInput):
    if input_data.fichier_entree is None:
        return {"message":" le fichier_entree n'est pas spécifié"}
    if input_data.fichier_sortie is None:
        return {"message":"le fichier_sortie n'est pas spécifié "}
    if input_data.operation is None:
        return {"message":"l'operation à effectué n'est pas spécifié"}
    if input_data.cle_chiffrement is None:
        return {"message":"le cle_chiffrement n'est pas spécifié"}
    if input_data.mode_chiffrement is None:
        return {"message":"le mode_chiffrement n'est pas spécifié"}

    # Lire le fichier d'entrée CSV dans un DataFrame
    try:
        df = pd.read_csv(input_data.fichier_entree, sep=input_data.separateur)
    except FileNotFoundError:
        return {"message": "Le fichier d'entrée spécifié n'existe pas."}
    # Appliquer la fonction de cryptage ou de hachage à chaque colonne spécifiée
    if input_data.colonnes:
        colonnes = input_data.colonnes.split(',')
    else:
        colonnes = df.columns.tolist()

    for col in colonnes:
        original_values = df[col].tolist()
        encrypted_values = []

        for value in original_values:
            if input_data.operation == "chiffrement":
                encrypted_value = aes_encrypt(
                    str(value),
                    input_data.cle_chiffrement,
                    input_data.mode_chiffrement,
                    iv=input_data.vecteur
                    if input_data.mode_chiffrement == "CBC"
                    else None,
                )
            elif input_data.operation == "dechiffrement":
                encrypted_value = aes_decrypt(
                    str(value),
                    input_data.cle_chiffrement,
                    input_data.mode_chiffrement,
                    iv=input_data.vecteur
                    if input_data.mode_chiffrement == "CBC"
                    else None,
                )
            elif input_data.operation == "hashage":
                encrypted_value = sha256_hash(str(value))

            encrypted_values.append(encrypted_value)

            # Store values in the database
            db = SessionLocal()
            db.execute(
                encryption_table.insert().values(
                    original_value=str(value), encrypted_value=encrypted_value
                )
            )
            db.commit()
            db.close()

        df[col] = encrypted_values    # Écrire le dataframe modifié dans un nouveau fichier csv
    df.to_csv(input_data.fichier_sortie, index=False, sep=input_data.separateur)

    return {"message": "Le traitement du fichier a été effectué avec succès."}

""" 
exemple d'execution :  http://localhost:8000/encrypt_file
{
    "fichier_entree": "C:/Users/hp/Desktop/fastApi_resultat/random_data.csv",
    "fichier_sortie": "C:/Users/pc/Desktop/stage_inwi/data.csv",
    "operation": "chiffrement",
    "cle_chiffrement": "ma_cle_secrete12",
    "mode_chiffrement": "CBC",
    "vecteur": "monvecteursecret",
    "colonnes": "id",
    "separateur": ";"

}"""



