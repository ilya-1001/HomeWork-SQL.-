import sqlalchemy
from sqlalchemy.orm import sessionmaker

from ORM_models import create_tables, Publisher, Sale, Book, Stock, Shop

sql = 'postgresql'
login = 'postgres'
password = 'postgres'
host = 'localhost'
port = '5432'
data_base = 'hw_netology_db'
DSN = f'{sql}://{login}:{password}@{host}:{port}/{data_base}'
engine = sqlalchemy.create_engine(DSN)

Session = sessionmaker(bind=engine)
session = Session()

create_tables(engine)

if __name__ == '__main__':

    publisher1 = Publisher(name = 'Пушкин')
    publisher2 = Publisher(name = 'Достоевский')
    publisher3 = Publisher(name = 'Толстой')

    book1 = Book(title = 'Капитанская дочка', id_publisher = 1)
    book2 = Book(title = 'Руслан и Людмила', id_publisher = 1)
    book3 = Book(title = 'Евгений Онегин', id_publisher = 1)
    book4 = Book(title = 'Преступление и наказание', id_publisher = 2)
    book5 = Book(title = 'Идиот', id_publisher = 2)
    book6 = Book(title = 'Игрок', id_publisher = 2)
    book7 = Book(title = 'Война и мир', id_publisher = 3)
    book8 = Book(title = 'Анна Каренина', id_publisher = 3)
    book9 = Book(title = 'Кавказский пленник', id_publisher = 3)

    shop1 = Shop(name = 'Буквоед')
    shop2 = Shop(name = 'Лабиринт')
    shop3 = Shop(name = 'Книжный дом')

    stock1 = Stock(id_book = 1, id_shop = 1, count = 2)
    stock2 = Stock(id_book = 2, id_shop = 1, count = 1)
    stock3 = Stock(id_book = 3, id_shop = 3, count = 1)
    stock4 = Stock(id_book = 1, id_shop = 2, count = 1)
    stock5 = Stock(id_book = 4, id_shop = 1, count = 2)
    stock6 = Stock(id_book = 5, id_shop = 3, count = 1)
    stock7 = Stock(id_book = 6, id_shop = 3, count = 1)
    stock8 = Stock(id_book = 7, id_shop = 2, count = 1)
    stock9 = Stock(id_book = 8, id_shop = 3, count = 1)
    stock10 = Stock(id_book = 9, id_shop = 1, count = 1)
    stock11 = Stock(id_book = 7, id_shop = 1, count = 1)
    stock12 = Stock(id_book = 5, id_shop = 2, count = 1)

    sale1 = Sale(price = '600', data_sale = '09-11-2022', id_stock = 1, count = 1)
    sale2 = Sale(price = '500', data_sale = '08-11-2022', id_stock = 2, count = 1)
    sale3 = Sale(price = '580', data_sale = '05-11-2022', id_stock = 4, count = 1)
    sale4 = Sale(price = '490', data_sale = '02-11-2022', id_stock = 3, count = 1)
    sale5 = Sale(price = '600', data_sale = '26-10-2022', id_stock = 1, count = 1)
    sale6 = Sale(price = '570', data_sale = '18-11-2022', id_stock = 5, count = 1)
    sale7 = Sale(price = '570', data_sale = '19-11-2022', id_stock = 5, count = 1)
    sale8 = Sale(price = '610', data_sale = '14-12-2022', id_stock = 6, count = 1)
    sale9 = Sale(price = '550', data_sale = '28-05-2022', id_stock = 7, count = 1)
    sale10 = Sale(price = '580', data_sale = '01-11-2022', id_stock = 8, count = 1)
    sale11 = Sale(price = '620', data_sale = '12-06-2022', id_stock = 9, count = 1)
    sale12 = Sale(price = '600', data_sale = '15-03-2022', id_stock = 10, count = 1)
    sale13 = Sale(price = '600', data_sale = '15-03-2022', id_stock = 10, count = 2)

    session.add_all([publisher1, publisher2, publisher3])
    session.add_all([book1, book2, book3, book4, book5, book6, book7, book8, book9])
    session.add_all([shop1, shop2, shop3])
    session.add_all([stock1, stock2, stock3, stock4, stock5, stock6, stock7, stock8, stock9,
                     stock10, stock11, stock12])
    session.add_all([sale1, sale2, sale3, sale4, sale5, sale6, sale7, sale8, sale9, sale10,
                     sale11, sale12, sale13])
    session.commit()


    publisher_name = input('Ведите имя писателя или id для вывода: ')

    if publisher_name.isnumeric():
        q = (session.query(Book.title, Shop.name, Sale.price, Sale.data_sale)
         .join(Publisher).join(Stock).join(Shop)
          .join(Sale).filter(Book.id_publisher == int(publisher_name)))
        for el in q.all():
            print(f'{el[0]:<25}| {el[1]:<12}| {el[2]:<4}| {el[3].strftime("%d-%m-%Y")}')
    else:
        q = (session.query(Book.title, Shop.name, Sale.price, Sale.data_sale)
         .join(Publisher).join(Stock).join(Shop)
          .join(Sale).filter(Publisher.name.ilike (f'%{publisher_name}%')))
        for el in q:
            print(f'{el[0]:<25}| {el[1]:<12}| {el[2]:<4}| {el[3].strftime("%d-%m-%Y")}')

    session.close()
