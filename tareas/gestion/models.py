from django.db import models

from autorizacion.models import Usuario

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

    # Creando relacion entre el modelo usuario y tarea
    # on_delete > sirve para indicar que accion se debe realizar sobre los registros
        # que pertenecen a ese registro a eliminar y sus valores pueden ser
        # CASCADE > se elimina el usuario y se procede a eliminar sus tareas
        # PROTECT > evita la eliminacion del usuario y emitira un error
        # SET_NULL > elimina el usuario y a todas sus tareas les cambia el valor de 
            # usuario_id a NULL
        # SET_DEFAULT (valor) > elimina el usuario y modifica su valor a un valor por defecto.
    # related_name > sirve para que a raiz del modelo usuario este cree un atributo 
        # en la clase USUARIO para poder acceder a todas sus tareas si no se define
        # el valor predeterminado sera usuario_set_tarea
    usuarioId=models.ForeignKey(to=Usuario,related_name='tareas',db_column='usuario_id',on_delete=models.CASCADE)



    # django Project model options
    class Meta:
        db_table='tareas'

        # Ordering por default es ascendente
        ordering=['-fechaVencimiento','nombre']
        # Asi seria de forma descendente del mas viejo al mas nuevo
            # ordering=['-fechaVencimiento']
        