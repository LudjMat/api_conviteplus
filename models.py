from sqlalchemy import Column, String, DateTime, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import uuid

Base = declarative_base()

class Aniversariante(Base):
    __tablename__ = "aniversariantes"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    nome = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

class Convite(Base):
    __tablename__ = "convites"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    aniversariante_id = Column(String, ForeignKey("aniversariantes.id"), nullable=False)
    localizacao = Column(String, nullable=False)
    code_dress = Column(String, nullable=False)
    horario = Column(String, nullable=False)
    data = Column(String, nullable=False)
    #created_at = Column(DateTime, default=datetime.utcnow)

class Felicitacao(Base):
    __tablename__ = "felicitacoes"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    convite_id = Column(String, ForeignKey("convites.id"), nullable=False)
    nome = Column(String, nullable=False)
    mensagem = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

class Convidados(Base):
    __tablename__ = "convidados"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    convite_id = Column(String, ForeignKey("convites.id"), nullable=False)
    nome = Column(String, nullable=False)
    sobrenome = Column(String, nullable=False)
    telefone = Column(String, nullable=False)
    confirmado = Column(String, nullable=False, default="nao")
    created_at = Column(DateTime, default=datetime.utcnow)
