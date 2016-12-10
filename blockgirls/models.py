from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
 	autor = models.ForeignKey('auth.User')
 	titulo = models.CharField(max_length=200)
 	texto =  models.TextField()
 	fecha_creacion = models.DateTimeField(default=timezone.now)
 	fecha_publicacion = models.DateTimeField(blank=True, null=True)

 	def publish(self):				# el objeto de esta clase
 		self.published_date = timezone.now()
 		self.save()

 	def __str__(self):
 		return self.titulo		# RETURN LO QUE HACE ES MOSTRAR EL RESUTADO
	