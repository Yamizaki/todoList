from django.db import models

# Create your models here.
# inyeccion de datos 
# instalar django-seed, agregarlo en setting django_seed, iniciar comando py manage.py seed Task --number=50
class Task(models.Model):
    STATUS_CHOICES = (
        ('Registrado', 'Registrado'),
        ('Culminado', 'Culminado'),
        ('Pausado', 'Pausado'),
    )

  

    title = models.CharField(max_length=20)
    description = models.TextField(max_length=500)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Registrado')
   

    date_created= models.DateField(auto_now_add=True)
    date_final= models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    
