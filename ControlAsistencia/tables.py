import django_tables2 as tables
from models import Estudiante

class EstTable(tables.Table):
    class Meta:
        model = Estudiante
        sequence = ("Colegio","Codigo","Nombre", "1er Apellido", "2do Apellido", "Direccion", "Dni")
