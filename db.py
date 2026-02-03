import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="Client_query",
        user="postgres",
        password="Saran@4686",
        port=5432
    )
