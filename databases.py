from model import Base, User, pwd_security

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///users.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_user(name,secret_word):
    """Add a user to the DB."""
    user = User(username=name, password_hash = pwd_security.encrypt(secret_word), fav_food = "not specified")
    session.add(user)
    session.commit()

def get_user(username):
    """Find the first user in the DB, by their username."""
    return session.query(User).filter_by(username=username).first()

def update_fav_food(username, food):
	user = session.query(User).filter_by(username=username).first()
	user.fav_food = food
	session.commit()

