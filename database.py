import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="nanthini",
    port="5432"
)
conn.autocommit= True

cursor =conn.cursor()

cursor.execute("CREATE DATABASE student_db")

cursor.close()
conn.close()

print("Database created")

conn = psycopg2.connect(
    host="localhost",
    database="student_db",
    user="postgres",
    password="nanthini",
    port="5432"
)

cursor=conn.cursor()

cursor.execute(""" 
CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
)
""")
cursor.execute(
    "ALTER TABLE users ADD COLUMN dept VARCHAR(30)"
)
cursor.execute("""
CREATE TABLE products(
    productid INTEGER PRIMARY KEY,
    prod_name VARCHAR(40)
    )
""")

cursor.execute("""
INSERT INTO products(productid, prod_name)
VALUES (12, 'Laptop')
""")

cursor.execute("ALTER TABLE users ADD COLUMN productid INTEGER REFERENCES products(productid)"
)
cursor.execute("""INSERT INTO users(name,email,dept,productid) VALUES('zayn','zayn7@gmail.com','Computer Science',12)"""
)
conn.commit()

cursor.execute("SELECT * FROM users")
cursor.execute("SELECT * FROM products")

for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()