from src.services.db.DatabaseConnection import connection

def get_results() -> list:
    conn = connection()
    cursor = conn.cursor()
    try:
        sql = 'SELECT g.Grupo, \
            c.Matricula, \
            a.Nombre, \
            m.NombreMateria,\
            c.Intento, \
            c.CalificacionFinal \
            FROM Calificaciones c \
            INNER JOIN Materias m ON c.MateriaId=m.Id \
            INNER JOIN Alumnos a  ON c.Matricula=a.Matricula \
            INNER JOIN Grupos g ON c.GrupoId=g.Id;\
            '
        cursor.execute(sql)
        res = cursor.fetchall()
        return res
    except Exception as ex:
        return ex
    
def get_result(id: str) -> list:
    conn = connection()
    cursor = conn.cursor()
    try:
        sql = 'SELECT Matricula, \
            (SELECT NombreMateria FROM Materias WHERE Id = c.MateriasId), \
                CalificacionFinal \
                    FROM Calificaciones c WHERE Matricula=%s;'
        res = cursor.execute(sql, id)
        return cursor.fetchmany(res)
    except Exception as ex:
        return ex
    
def get_tries(values: list) -> int:
    conn = connection()
    cursor = conn.cursor()
    sql = 'SELECT Intento FROM Calificaciones c \
        INNER JOIN Materias m ON m.Id = c.MateriaId \
        WHERE c.Matricula=%s AND m.NombreMateria=%s'
    if values:
        cursor.execute(sql, values)
        res = cursor.fetchone()
        if res == None:
            return 0
        else:
            return res[0]