from django.db import models

# Create your models here.

class Material(models.Model):
    categorias=[
        ("educativos","Educativos"),
        ("ropa","Ropa"),
        ("cosmeticos","Cosmeticos")

    ]
    nombre =models.CharField(max_length=50)
    categoria=models.CharField(choices=categorias, max_length=50)
    fechaIngreso=models.DateField(auto_now_add=True)
    cantidad=models.IntegerField()

    def __str__(self):
        return self.nombre


