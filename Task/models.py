from django.db import models

# Create your models here.
class Task(models.Model):
    STATUS_CHOICES = (
        ('Registrado', 'REGISTRADO'),
        ('Culminado', 'CULMINADO'),
        ('Cancelado', 'CANCELADO'),
    )

  

    title = models.CharField(max_length=20)
    description = models.TextField(max_length=500)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Registrado')
   

    date_created= models.DateField(auto_now_add=True)
    date_final= models.DateField()

    def __str__(self):
        return self.title

    
