from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('postgresql://postgres:12345@localhost/pizzehut', echo=True)

Base = declarative_base()

Session = sessionmaker()
