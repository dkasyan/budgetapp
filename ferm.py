from sqlalchemy import create_engine, MetaData, Integer, String, Table, Column

# Do logów
#engine = create_engine('sqlite:///database.db', echo=True)
engine = create_engine('sqlite:///database.db')
meta = MetaData()

students = Table(
   'students', meta,
   Column('id', Integer, primary_key=True),
   Column('name', String),
   Column('lastname', String),
)

conn = engine.connect()
a = Table(id = 1, name = 'blue', lastname = '#0F85FF')
s = students.select().where(students.c.id > 2)
result = conn.execute(s)
result = conn.execute(a)

for row in result:
   print(row)