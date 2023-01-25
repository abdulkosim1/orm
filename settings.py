import peewee

db = peewee.PostgresqlDatabase(
    database = 'orm_py25',
    user = 'postgres',
    password = '1',
    host = 'localhost',
    port = 5432
    )