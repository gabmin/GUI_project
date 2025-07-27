import sqlite3
from utils.config import DB_PATH

def init_db(self):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS image_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            image BLOB,
            prompt TEXT,
            response TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()