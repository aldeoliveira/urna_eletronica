import psycopg2


class DataBase:

    def connect(self):
        return psycopg2.connect(host="localhost", database="urna_teste", user="postgres", password="cd6432")
