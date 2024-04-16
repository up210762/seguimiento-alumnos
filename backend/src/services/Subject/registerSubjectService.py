from src.services.db.DatabaseConnection import connection
import time

def register_subject(values=[]) -> str:
    conn = connection()
    cursor = conn.cursor()
    to_insert = []
    actual_value: str = ''
    try:
        search_subject = 'SELECT * FROM  Materias \
            WHERE NombreMateria=%s;'
        sql = 'INSERT IGNORE INTO \
            Materias (NombreMateria) \
            VALUES (%s);'
        for value in values:
            cursor2 = conn.cursor()
            searched = cursor2.execute(search_subject, value)
            if searched == 0 and value != actual_value:
                to_insert.append(value)
                actual_value = value    
            else:
                continue
            cursor2.close()
            time.sleep(0.01)
        if len(to_insert) == 0:
            res = "No hay registros por ingresar"
        else:
            res = cursor.executemany(sql, to_insert)
            conn.commit()
        cursor.close()
        conn.close()
        return res
    except Exception as ex:
        return ex