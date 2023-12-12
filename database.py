import sqlite3

conn = sqlite3.connect('banco.db')

cursor = conn.cursor()

create_department_table_sql = '''
CREATE TABLE IF NOT EXISTS sites (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT NOT NULL
);
'''

create_employee_table_sql = '''
CREATE TABLE IF NOT EXISTS hoteis (
    id TEXT PRIMARY KEY,
    nome TEXT NOT NULL,
    estrelas REAL,
    diaria REAL,
    cidade TEXT,
    site_id INTEGER,
    FOREIGN KEY (site_id) REFERENCES Site(id)
);
'''

cursor.execute(create_department_table_sql)
cursor.execute(create_employee_table_sql)

conn.commit()
conn.close()