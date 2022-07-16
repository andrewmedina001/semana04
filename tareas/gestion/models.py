from urllib.parse import MAX_CACHE_SIZE
from django.db import models

# Create your models here.
class Tarea(models.Model):
    # documentacion DjangoProject -> field options, field types

    # AutoField -> columna autoincrementable por defecto con valor INT
    id=models.AutoField(primary_key=True,unique=True)

    # para que sea varchar se tiene que poner la longitud como maxima
    nombre=models.CharField(db_column='name_tarea',max_length=100)

    # Segun la documentacion si no va nada en este caso cumple
    descripcion=models.TextField(null=True)

    # 
    fechaVencimiento=models.DateTimeField(db_column='fecha_venc')

    estadoOpciones=[('POR_HACER','POR_HACER'),('HACIENDO','HACIENDO'),('HECHO','HECHO')]

    estado=models.CharField(choices=estadoOpciones,max_length=10,default='POR_HACER')


    # django Project model options
    class Meta:
        db_table='tareas'

        # Ordering por default es ascendente
        ordering=['-fechaVencimiento','nombre']
        # Asi seria de forma descendente del mas viejo al mas nuevo
            # ordering=['-fechaVencimiento']
        