from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float, Boolean, between
from sqlalchemy.ext.declarative import declarative_base
from session import engine

Base = declarative_base(engine)


class Category(Base):
    __table__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    last_update = Column(DateTime)

    def __str__(self):
        return self.name


class FilmCategory(Base):
    __table__ = 'film category'

    film_id = Column(Integer, ForeignKey('film.id'))
    category_id = Column(Integer, ForeignKey('category.id'))
    last_update = Column(DateTime)

    def __str__(self):
        return f'{self.film_id}, {self.category_id}'


class Film(Base):
    __table__ = 'film'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    description = Column(String(62), DateTime)
    release_year = Column(DateTime, nullable=False)
    language_id = Column(Integer, ForeignKey('language.id'), nullable=False)
    rental_duration = Column(DateTime)
    rental_rate = Column(Float, nullable=False)
    length = Column(Float, nullable=False)
    replacement_cost = Column(Boolean, Float, nullable=False)
    rating = Column(Float, nullable=False)
    last_update = Column(DateTime)
    special_features = Column(String(50), nullable=False)
    full_text = Column(String(400), nullable=False)

    def __str__(self):
        return self.title


class Language(Base):
    __table__ = 'language'

    language_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    last_update = Column(DateTime)

    def __str__(self):
        return self.name


class FilmActor(Base):
    __table__ = 'film actor'

    actor_id = Column(Integer, ForeignKey('actor.actor_id'))
    film_id = Column(Integer, ForeignKey('film.id'), nullable=False)
    last_update = Column(DateTime)

    def __str__(self):
        return self.film_id


class Actor(Base):
    __table__ = 'actor'

    actor_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    last_update = Column(DateTime)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'


class Inventory(Base):
    __table__ = 'inventory'

    inventory_id = Column(Integer, primary_key=True, autoincrement=True)
    film_id = Column(Integer, ForeignKey('film.id'))
    store_id = Column(Integer, ForeignKey('store.store_id'))
    last_update = Column(DateTime)

    def __str__(self):
        return f'{self.film_id}, {self.store_id}'


class Rental(Base):
    __table__ = 'rental'

    rental_id = Column(Integer, primary_key=True, autoincrement=True)
    rental_date = Column(DateTime)
    inventory_id = Column(Integer, ForeignKey('inventory.inventory_id'))
    customer_id = Column(Integer, ForeignKey('customer.customer_id'))
    return_date = Column(DateTime)
    stuff_id = Column(Integer, ForeignKey('staff.staff_id'))
    last_update = Column(DateTime)

    def __str__(self):
        return f'{self.rental_date}, {self.return_date}'


class Customer(Base):
    __table__ = 'customer'

    customer_id = Column(Integer, primary_key=True, autoincrement=True)
    store_id = Column(Integer, ForeignKey('store.store_id'))
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    address_id = Column(Integer, ForeignKey('address.address_id'))
    is_active = Column(Boolean)
    create_date = Column(DateTime, nullable=False)
    lastupdate = Column(DateTime)
    rental_id = Column(Integer, ForeignKey('rental.rental_id'))

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'


class Payment(Base):
    __table__ = 'payment'

    payment_id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customer.customer_id'))
    stuff_id = Column(Integer, ForeignKey('staff.staff_id'))
    rental_id = Column(Integer, ForeignKey('rental.rental_id'))
    amount = Column(Float, nullable=False)
    payment_date = Column(DateTime)

    def __str__(self):
        return f'{self.amount}, {self.payment_date}'


class Address(Base):
    __tablename__ = 'address'

    address_id = Column(Integer, primary_key=True, autoincrement=True)
    address = Column(String(100), nullable=False)
    address2 = Column(String(100), nullable=False)
    district = Column(String(50), nullable=False)
    city_id = Column(Integer, ForeignKey('city.city_id'))
    postal_code = Column(String(50), nullable=False)
    phone = Column(String(50), nullable=False)
    last_update = Column(DateTime)

    def __str__(self):
        return f'{self.address}, {self.postal_code}'


class Staff(Base):
    __tablename__ = 'staff'

    staff_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    address_id = Column(Integer, ForeignKey('address.address_id'))
    store_id = Column(Integer, ForeignKey('store.store_id'))
    active = Column(Boolean)
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    last_update = Column(DateTime)
    picture = Column(String(50), nullable=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Store(Base):
    __tablename__ = 'store'

    store_id = Column(Integer, primary_key=True, autoincrement=True)
    manager_staff_id = Column(Integer, ForeignKey('staff.staff_id'))
    address_id = Column(Integer, ForeignKey('address.address_id'))
    last_update = Column(DateTime)

    def __str__(self):
        return f'{self.store_id} ,{self.manager_staff_id}'


class City(Base):
    __tablename__ = 'city'

    city_id = Column(Integer, primary_key=True, autoincrement=True)
    city = Column(String(50), nullable=False)
    country_id = Column(Integer, ForeignKey('country.country_id'))
    last_update = Column(DateTime)

    def __str__(self):
        return self.city


class Country(Base):
    __tablename__ = 'country'

    country_id = Column(Integer, primary_key=True, autoincrement=True)
    country = Column(String(50), nullable=False)
    last_update = Column(DateTime)

    def __str__(self):
        return self.country
