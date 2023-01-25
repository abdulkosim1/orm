from models import Category, Product
import peewee

def post_category(category_name):
    try:
        category = Category(name=category_name)
        category.save()
        print(category.id)
        print('saved')
    except peewee.IntegrityError:
        print('уже существует')

def get_categories():
    category = Category.select()
    for i in category:
        print(f'{i.id} -- {i.name} -- {i.created_at}')

def delete_category(category_id):
    try:
        category = Category.get(id=category_id)
        category.delete_instance()
        print('deleted')
    except peewee.DoesNotExist:
        print('category not found')

def update_category(category_id, new_name):
    try:
        category = Category.get(id=category_id)
        category.name = new_name
        category.save()
        print('updated')
    except peewee.DoesNotExist:
        print('categoy not found')

def detail_category(id_category):
    try:
        category = Category.get(id=id_category)
        print(category.id, end='\t')
        print(category.name, end='\t')
        print(category.created_at, end='\t')

        for i in category.product:
            print(f'{i.name} -- {i.price} -- {i.amount}')
    except peewee.DoesNotExist:
        print('category not found')

def post_product(name, price, amount, category):
    product = Product(name=name, price=price, amount=amount, category=category)
    product.save()
def get_products():
    product = Product.select()
    for i in product:
        print(f'{i.id} -- {i.name} -- {i.price} -- {i.amount}')
def delete_product(product_id):
    try:
        product = Category.get(id=product_id)
        product.delete_instance()
        print('deleted')
    except peewee.DoesNotExist:
        print('product not found')
def get_product_by_name(name):
    products = Product.select().where(Product.name==name)
    for i in products:
        print(i.name, i.price)