from sqlalchemy import Column,Integer,String,Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

#LLamar a la base de datos

#Definir las tablas del API
class Proveedor():
    __tablename__='proveedores'
    nombres=Column(String(50))
    documento=Column(String(50))
    direccion=Column(String(50))
    ciudad = Column(String(50))
    representante = Column(String(50))
    telefono_contacto = Column(String(20))
    correo = Column(String(100))
    fecha_envio = Column(Date)
    costo_envio = Column(Float)
    descripcion = Column(Text)
