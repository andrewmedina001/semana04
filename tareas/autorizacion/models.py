from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

"""Clase que sirve para manejar el comportamiento al crear el usuario con el
comando createsuperuser"""
class ManejoUsuario(BaseUserManager):
    def create_user(self,correo,nombre,apellido,password):
        if not correo:
            return ValueError("The user debe have obligatoriamente un correo.")
        # Normalizacion del correo>aliminacion de caracteres especiales y tambien 
            # quita los espacios
        correo=self.normalize_email(correo)
        nuevoUsuario=self.model(correo=correo,nombre=nombre,apellido=apellido)
        # hashear (encriptar) la contraseña > genera un string aleatorio
        nuevoUsuario.set_password(password)

        nuevoUsuario.save()
        return nuevoUsuario
    
    def create_superuser(self,correo,nombre,apellido,password):
        """Creacion de un super usuario por consola, este metodo se mandara
        a llamar cuando se haga la llamada por consola."""
        nuevoUsuario=self.create_user(correo,nombre,apellido,password)
        # modificacion de valores que corresponden a un superusuario
        nuevoUsuario.is_superuser=True
        nuevoUsuario.is_staff=True
        nuevoUsuario.save()


class Usuario(AbstractBaseUser):
    id=models.AutoField(primary_key=True,unique=True)
    nombre=models.CharField(max_length=45)
    apellido=models.CharField(max_length=45)
    correo=models.EmailField(unique=True)
    password=models.TextField()

    # Opcional y sirve si aun vamos a utilizar el panel administrativo
        # (CMS) Control Management System
    # is_staff > indica si el usuario es parte del staff que puede ingresar al CMS
    is_staff=models.BooleanField(default=False)

    # is_active > indica si el usuario esta activo y por lo tanto
        # pueda tener acceso al CMS , sino esta activo asi sea del staff no podra
        # ingresar
    is_active=models.BooleanField(default=True)

    # python manage.py createsuperuser > comportamiento que va a tener
    objects=ManejoUsuario()

    # sirve para que el login del panel administrativo nos pida el username
        # que le coloquemos
    USERNAME_FIELD='correo'

    # columnas que me solicitara cuando haga el registro de un superusuario por consola
    REQUIRED_FIELDS=['nombre','apellido']

    class Meta:
        db_table='usuarios'
