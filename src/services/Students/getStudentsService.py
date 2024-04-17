from src.services.db.DatabaseConnection import connection

conn = connection()

cursor = conn.cursor()

def get_students():
    try:
        sql = 'SELECT Matricula, Nombre FROM Alumnos;'
        res = cursor.execute(sql)
        return cursor.fetchmany(res)
    except Exception as ex:
        return ex
    
def get_student(id):
    try:
        sql = 'SELECT Matricula, Nombre FROM Alumnos WHERE Matricula=%s;'
        res = cursor.execute(sql, id)
        return cursor.fetchmany(res)
    except Exception as ex:
        return ex