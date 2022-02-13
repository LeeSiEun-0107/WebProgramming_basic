# 모듈 추가
import sqlite3

# 데이터 베이스 열기
conn = sqlite3.connect('./myvenv/Advanced/Chapter05/SQL_DDL.db')

# 커서 생성
cur = conn.cursor()

# SQL 명령 작성
UPDATE_SQL = """
UPDATE Item set price = 65000 WHERE code='A00001';
"""

# SQL 명령 실행
cur.execute(UPDATE_SQL)

# COMMIT
conn.commit()

# 데이터베이스 닫기
conn.close()
