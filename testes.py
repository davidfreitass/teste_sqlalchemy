from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///teste.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Pessoa(Base):
    __tablename__ = 'pessoas'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)
    email = Column(String)
    endereco = Column(String)

Base.metadata.create_all(engine)

p1 = Pessoa(nome='David', idade='22', email='david@gmail.com', endereco='Rua A 78, Bahia, Brasil')
p2 = Pessoa(nome='Raquel', idade='19', email='raquel@google.com', endereco='Rua B 14, Bahia, Brasil')

session.add_all([p1, p2])
session.commit()
