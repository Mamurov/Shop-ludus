from django.db import models


class Token(models.Model):
    userId = models.ForeignKey("User", on_delete=models.CASCADE, db_index=True);
    refreshToken = models.TextField(verbose_name="Токен");

    def __str__(self):
        return self.userId;