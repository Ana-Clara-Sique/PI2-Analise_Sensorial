from sqlalchemy import Column, Integer, String, ForeignKey
from models.conexao import Base, engine

class Avaliador(Base):
    __tablename__ = 'avaliadores'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    genero = db.Column(db.String(20), nullable=False)
    faixa_etaria = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Avaliador {self.nome}>'