from src.services.db.DatabaseConnection import connection
import time

def register_group(values=[]) -> str:
    conn = connection()
    cursor = conn.cursor()
    to_insert = []
    actual_value: str = ''
    search_group = 'SELECT * FROM Grupos \
        WHERE Grupo=%s;'
    sql = 'INSERT IGNORE INTO Grupos \
        (Grupo) \
        VALUES (%s);'
    try:
        for value in values:
            cursor2 = conn.cursor()
            searched = cursor2.execute(search_group, value)
            if searched == 0 and value != actual_value:
                to_insert.append(value)
                actual_value = value
            else:
                continue
            cursor2.close()
            time.sleep(0.01)
        if len(to_insert) == 0:
            res = "No hay registros por realizar"
        else:
            res = cursor.executemany(sql, to_insert)
            conn.commit()
        cursor.close()
        conn.close()
        return res
    except Exception as ex:
        return ex