from django.contrib.gis.db import models


class Searchs(models.Model):
    address = models.CharField(max_length=200,null=True)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.address
