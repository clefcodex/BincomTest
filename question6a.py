import psycopg2

conn = psycopg2.connect(database = "assignment", user = "postgres", password = "gospel1759", host = "127.0.0.1", port = "5432")

cu = conn.cursor()

cu.execute('''CREATE TABLE ColorTable (
id serial primary key,
Color text,
Frequency text);
	''')

conn.commit()

print("table successfully created")

conn.close()