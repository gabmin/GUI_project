import sqlite3
from utils.config import DB_PATH
import os

def init_db(self):
    db_exists = os.path.exists(DB_PATH)

    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS recipe_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ingredients_name TEXT NOT NULL,
                image BLOB,
                recipe_description TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        conn.commit()

    if not db_exists:
        print(f"새로운 DB와 테이블을 생성했습니다: {DB_PATH}")
    else:
        print(f"이미 존재하는 DB에 테이블을 확인/생성했습니다: {DB_PATH}")
