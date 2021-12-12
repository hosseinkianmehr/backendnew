from django.db import models


class tag(models.Model):
    titel = models.CharField('titel', max_length=50,unique=True )
    

    def __str__(self):
        return self.titel
    class Meta:
        verbose_name = ("tag")
        verbose_name_plural = ("tags")
   
