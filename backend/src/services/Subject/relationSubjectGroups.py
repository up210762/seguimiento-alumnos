from src.services.db.DatabaseConnection import connection

conn = connection()

cursor = conn.cursor()

def register_relation(values=[]):
    try:
        sql = 'INSERT IGNORE INTO \
            MateriasGrupos (MateriasId, GruposId) \
                VALUES (%s, %s);'
        res = cursor.executemany(sql, values)
        conn.commit()
        return res
    except Exception as ex:
        return ex

def search_groups_id(group):
    sql = 'SELECT Id FROM Grupos \
        WHERE Grupo=%s;'
    cursor.execute(sql, group)
    return cursor.fetchone()

def search_subjects_id(subject):
    sql = 'SELECT Id FROM Materias \
        WHERE NombreMateria=%s;'
    cursor.execute(sql, subject)
    return cursor.fetchone()