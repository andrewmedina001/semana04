from django.db import models

# Create your models here.
class Productos(models.Model):
    productId=models.AutoField(primary_key=True)
    productoNombre=models.CharField(max_length=40,null=False)
    estado=models.BooleanField(default=True)
    productoDescription=models.CharField(max_length=80)
    productoPrecio=models.DecimalField(max_digits=5,decimal_places=2)

    class Meta:
        db_table='productos'