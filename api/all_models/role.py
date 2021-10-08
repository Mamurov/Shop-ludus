from django.db import models


class Role(models.Model):
    title = models.CharField(max_length=100, verbose_name="Имя");

    def __str__(self):
        return self.title;