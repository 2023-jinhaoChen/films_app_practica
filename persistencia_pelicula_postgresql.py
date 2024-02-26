#!/bin/usr/python3

from ipersistencia_pelicula import IPersistencia_pelicula
from pelicula import Pelicula
from typing  import List
import psycopg
import logging

class Persistencia_pelicula_postgresql(IPersistencia_pelicula):
    def __init__(self, credencials) -> None:
        self._credencials = credencials
        self._conn = psycopg.connect(
                host=credencials["host"],
                user=credencials["user"],
                password=str(credencials["password"]),
                dbname=credencials["database"]
                )
        if not self.check_table():
            self.create_table()

    def check_table(self):
        try:
            cursor = self._conn.cursor()
            cursor.execute("SELECT * FROM PELICULA;")
            cursor._reset()
        except psycopg.Connection.ProgrammingError:
            return False
        return True
    
    def count(self) -> int:
        cursor = self._conn.cursor()
        query = "select id, titulo, anyo, puntuacion, votos from PELICULA;"
        cursor.execute(query)
        count = cursor.rowcount
        return count
    
    def totes(self) -> List[Pelicula]:
        cursor = self._conn.cursor()
        query = "select id, titulo, anyo, puntuacion, votos from PELICULA;"
        cursor.execute(query)
        registres = cursor.fetchall()
        cursor._reset()
        resultat = []
        for registre in registres:
            pelicula = Pelicula(registre[1],registre[2],registre[3],registre[4],self,registre[0])
            resultat.append(pelicula)
        return resultat
    
    def totes_pag(self, id=None) -> List[Pelicula]:
        cursor = self._conn.cursor()
        select_query = f"SELECT ID, TITULO, ANYO, PUNTUACION, VOTOS FROM PELICULA WHERE ID>{id} LIMIT 10;"
        cursor.execute(select_query)
        registres = cursor.fetchall()
        cursor._reset()
        resultat = []
        for registre in registres:
            pelicula = Pelicula(registre[1],registre[2],registre[3],registre[4],self,registre[0])
            resultat.append(pelicula)
        return resultat
    
    def desa(self,pelicula:Pelicula) -> Pelicula:
        cursor = self._conn.cursor()
        insert_query = f"INSERT INTO PELICULA(TITULO, ANYO, PUNTUACION, VOTOS) VALUES ('{pelicula.titol}', {pelicula.any}, {pelicula.puntuacio}, {pelicula.vots});"
        cursor.execute(insert_query)
        self._conn.commit()
        select_query = f"SELECT ID, TITULO, ANYO, PUNTUACION, VOTOS FROM PELICULA WHERE TITULO='{pelicula.titol}' AND ANYO={pelicula.any};"
        cursor.execute(select_query)
        registre = cursor.fetchone()
        return Pelicula(registre[1], registre[2], registre[3], registre[4], self, registre[0])
    
    def llegeix(self, any: int) -> List[Pelicula]:
        cursor = self._conn.cursor()
        select_query = f"SELECT ID, TITULO, ANYO, PUNTUACION, VOTOS FROM PELICULA WHERE ANYO={any};"
        cursor.execute(select_query)
        registres = cursor.fetchall()
        cursor._reset()
        resultat = []
        for registre in registres:
            pelicula = Pelicula(registre[1],registre[2],registre[3],registre[4],self,registre[0])
            resultat.append(pelicula)
        return resultat
    
    def canvia(self,pelicula:Pelicula) -> Pelicula:
        cursor = self._conn.cursor()
        update_query = (f"UPDATE PELICULA SET TITULO='{pelicula.titol}', "
                        f"ANYO={pelicula.any}, "
                        f"PUNTUACION={pelicula.puntuacio}, "
                        f"VOTOS={pelicula.vots} "
                        f"WHERE ID={pelicula.id}")
        cursor.execute(update_query)
        select_query = f"SELECT ID, TITULO, ANYO, PUNTUACION, VOTOS FROM PELICULA WHERE ID={pelicula.id};"
        cursor.execute(select_query)
        registre = cursor.fetchone()
        return Pelicula(registre[1], registre[2], registre[3], registre[4], self, registre[0])