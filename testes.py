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

p5 = Pessoa(nome="Vovô", idade=82, endereco="Rua C 12, Bahia, Brasil")

session.add(p5)
session.commit()
