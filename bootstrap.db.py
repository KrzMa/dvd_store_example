from sqlalchemy.exc import IntegrityError

from models import Base, Category, FilmCategory, Film, Language, Inventory, Rental, FilmActor, Actor, Customer, Payment, \
    Staff, Address, City, Country, Store


def main():
    # create all tables
    Base.metadata.create_all()


if __name__ == "__main__":
    main()