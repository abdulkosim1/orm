# orm  (object relational mapping) (объектно реляционное отображение) - технология которая связывает бд с концепциями ооп

# python    
    # peewee
    # sqlslchemy
    # DjangoORM


# Класс - таблица в бд
# Атрибут класса - поле в бд
# Объект класса - строка в таблице


from views import *
from settings import db


db.connect()


post_category('18')
# delete_category(1)
# post_product('product4', 30, 10, 18)
# get_products()
get_categories()




db.close()
