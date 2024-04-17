from src.services.db.DatabaseConnection import connection
import time

def register_student(values=[]):
    conn = connection()
    cursor = conn.cursor()
    to_insert = []
    try:
        search_student = 'SELECT * FROM Alumnos \
            WHERE Matricula=%s;'
        insert = 'INSERT IGNORE \
            INTO Alumnos \
            (Matricula, Nombre) \
            VALUES (%s, %s);'
        for value in values:
            cursor2 = conn.cursor()
            searched = cursor2.execute(search_student, value[0])
            if searched == 0:
                to_insert.append(value)
            else:
                continue
            cursor2.close()
            time.sleep(0.01)
        if len(to_insert) == 0:
            res = "No hay registros por realizar"
        else:
            res = cursor.executemany(insert, to_insert)
            conn.commit()
        cursor.close()
        conn.close()
        return res
    except Exception as ex:
        return ex