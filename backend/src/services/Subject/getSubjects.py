from src.services.db.DatabaseConnection import connection

sql_query = 'SELECT NombreMateria \
    FROM Materias;'

def get_groups():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute(sql_query)
    return cursor.fetchall()