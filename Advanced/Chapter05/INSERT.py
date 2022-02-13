# 모듈 추가
import sqlite3

# 데이터 베이스 열기
conn = sqlite3.connect('./myvenv/Advanced/Chapter05/SQL_DDL.db')

# 커서 생성
cur = conn.cursor()

# SQL 명령 작성
CREATE_SQL = """
INSERT INTO Item(code,name,price) VALUES (?,?,?)
"""

data = (
    ('A00002', '에어컨 20평형', 3500000),
    ('A00003', '최신형 스마트폰', 8000000),
    ('A00004', '가성비 노트북', 270000)
)
# SQL 명령 실행
cur.executemany(CREATE_SQL, data)

# COMMIT : INSERT, UPDATE, DELETE는 COMMIT을 해야 실제 데이터베이스에 반영이 된다
conn.commit()
# 데이터베이스 닫기
conn.close()
