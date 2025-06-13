import mysql.connector

class Database:
    def __init__(self):
        self.database = mysql.connector.connect(
            host = "localhost",
            username = "root",
            password = "your_sql_password_here",
            database = "pasteit"
        )
        self.cursor = self.database.cursor()
        
    def insert(self,title="Untitled", content="", slug=None):
        query = "INSERT INTO pastes (title, content, slug) VALUES (%s, %s, %s)"
        values = (title, content, slug)
        self.cursor.execute(query, values)
        self.database.commit()
        
        
    def fetch(self, slug):
        query = "SELECT title, content, created_at FROM pastes where slug=%s"
        self.database.execute(query, (slug))
        result = self.cursor.fetchone()
        if result:
            title, content, created_at = result
            return {
                "title": title,
                "content": content,
                "created_at": created_at
            }
        else:
            return None

    def remove(self, slug):
        query = "DELETE FROM pastes WHERE slug=%s"
        self.cursor.execute(query, (slug,))
        self.database.commit()

if __name__ == "__main__":
    db = Database()
    db.cursor.execute("Select * from pastes;")
    result = db.cursor.fetchone()
    if result:
        print(result)
    else:
        print("No records fetched.")