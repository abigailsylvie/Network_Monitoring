from django.db import models


class Vulnerability(models.Model):
    host = models.CharField(max_length=100)
    port = models.IntegerField()
    service = models.CharField(max_length=100)
    state = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.host}:{self.port}'
