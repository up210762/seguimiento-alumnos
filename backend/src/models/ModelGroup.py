from src.services.db.DatabaseConnection import connection

conn = connection()
cursor = conn.cursor()

class Group():
    def __init__(self, group) -> None:
        self.group = group