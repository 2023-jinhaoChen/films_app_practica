from persistencia_pelicula_mysql import Persistencia_pelicula_mysql
from persistencia_pelicula_postgresql import Persistencia_pelicula_postgresql
from pelicula import Pelicula
from typing import List
from llistapelis import Llistapelis
import mysql.connector
import logging

# logging.basicConfig(filename="pelicules.log", encoding="utf-8", level=logging.DEBUG)
credencials = {
    "host": "localhost",
    "user" : "dam_app",
    "password" : "1234",
    "database" : "pelis"
}

pers_pelis = Persistencia_pelicula_postgresql(credencials)
############################################################################################

# print(pers_pelis.totes())
# p = Pelicula("La sociedad sin nieve 2", 2024, 5.0, 10000, pers_pelis)
# print(pers_pelis.desa(p))

# print(pers_pelis.llegeix(1988))
# p = Pelicula("La sociedad sin nieve 3", 2010, 5.0, 10000, pers_pelis, 1693)
# print(pers_pelis.canvia(p))


print(pers_pelis.totes_pag(10))
