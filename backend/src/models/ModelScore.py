from src.services.db.DatabaseConnection import connection

class Score():
    def __init__(self, enrollment, subject_id, group_id, score) -> None:
        self.enrollment = enrollment
        self.subject_id = subject_id
        self.group_id = group_id
        self.score = score

    def search_subject(self):
        conn = connection()
        cursor = conn.cursor()
        sql = 'SELECT id FROM Materias \
            WHERE NombreMateria = %s'
        cursor.execute(sql, self.subject_id)
        res = cursor.fetchone()
        cursor.close()
        conn.close()
        return res
    
    def search_group(self):
        conn = connection()
        cursor = conn.cursor()
        sql = 'SELECT id FROM Grupos \
            WHERE Grupo = %s'
        cursor.execute(sql, self.group_id)
        res = cursor.fetchone()
        cursor.close()
        conn.close()
        return res