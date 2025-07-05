from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(50), nullable=False)
    apellido: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    fecha_registro: Mapped[str] = mapped_column(String(20), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False, default=True)

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "email": self.email,
            "fecha_registro": self.fecha_registro
        }
class Personaje(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    especie: Mapped[str] = mapped_column(String(50))
    afiliacion: Mapped[str] = mapped_column(String(50))
    altura_cm: Mapped[int] = mapped_column()
    genero: Mapped[str] = mapped_column(String(20))
    anio_nacimiento: Mapped[str] = mapped_column(String(20))
    planeta_id: Mapped[int] = mapped_column(db.ForeignKey('planeta.id'), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "especie": self.especie,
            "afiliacion": self.afiliacion,
            "altura_cm": self.altura_cm,
            "genero": self.genero,
            "anio_nacimiento": self.anio_nacimiento,
            "planeta_id": self.planeta_id
        }
    
class Planeta(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    region: Mapped[str] = mapped_column(String(100))
    clima: Mapped[str] = mapped_column(String(50))
    terreno: Mapped[str] = mapped_column(String(100))
    poblacion_aproximada: Mapped[str] = mapped_column(String(50))

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "region": self.region,
            "clima": self.clima,
            "terreno": self.terreno,
            "poblacion_aproximada": self.poblacion_aproximada
        }
class FavoritoPersonaje(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    usuario_id: Mapped[int] = mapped_column(db.ForeignKey('user.id'), nullable=False)
    personaje_id: Mapped[int] = mapped_column(db.ForeignKey('personaje.id'), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "personaje_id": self.personaje_id
        }
    
class FavoritoPlaneta(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    usuario_id: Mapped[int] = mapped_column(db.ForeignKey('user.id'), nullable=False)
    planeta_id: Mapped[int] = mapped_column(db.ForeignKey('planeta.id'), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "planeta_id": self.planeta_id
        }