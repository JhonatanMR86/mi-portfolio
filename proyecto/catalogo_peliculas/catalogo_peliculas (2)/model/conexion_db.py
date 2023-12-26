import sqlite3

class ConexionDB:
    def __init__(self):
        self.base_datos='E:\INGENIERIA\Curso Python\Practica3\Practica_3\Practica_3\proyecto\catalogo_peliculas\catalogo_peliculas (2)\database/peliculas.db'
        self.conexion=sqlite3.connect(self.base_datos)
        self.cursor=self.conexion.cursor()

    def cerrar(self):
        self.conexion.commit()
        self.conexion.close()