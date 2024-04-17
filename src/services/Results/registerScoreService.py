from src.services.db.DatabaseConnection import connection
import time

def change_score(student:str, subject:int, score:int, tries:int) -> str:
    conn = connection()
    cursor = conn.cursor()
    sql = 'UPDATE Calificaciones \
        SET CalificacionFinal=%s, \
        Intento=%s, Fecha=NOW() \
        WHERE Matricula=%s AND MateriaId=%s;'
    try:
        res = cursor.execute(sql, [score, tries, student, subject])
        conn.commit()
        cursor.close()
        conn.close()
        return res
    except Exception as ex:
        return ex

def register_score(values = []) -> str:
    conn = connection()
    cursor = conn.cursor()
    to_insert = []
    to_alter = []
    search_row = 'SELECT * FROM Calificaciones \
        WHERE Matricula=%s;'
    sql = 'INSERT INTO Calificaciones \
            (Matricula, MateriaId, GrupoId, CalificacionFinal, Intento, Fecha, Estado) \
            VALUES (%s, %s, %s, %s, %s, %s, %s);'
    row_alter = 0
    row_insert = 0
    try:
        for value in values:
            cursor2 = conn.cursor()
            searched = cursor2.execute(search_row, value[0])
            if searched == 0:
                to_insert.append(value)
            else:
                to_alter.append(value)
            time.sleep(0.01)
        if to_alter and len(to_insert)==0:
            for row in to_alter:
                row_alter = change_score(row[0], row[1], row[3], row[4])
        elif to_insert and len(to_alter)==0:
            row_insert = cursor.executemany(sql, values)
        res = f'Registros creados: {row_insert}, registros modificados: {row_alter}'
        conn.commit()
        cursor.close()
        conn.close()
        return res
    except Exception as ex:
        return ex