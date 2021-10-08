from django.db import models


class Review(models.Model):
    userId = models.ForeignKey("User", on_delete=models.CASCADE, verbose_name="Пользователь", db_index=True);
    text = models.TextField(verbose_name="Отзыв");
    rating = models.ForeignKey("Rating", on_delete=models.CASCADE, verbose_name="Рейтинг");

    def __str__(self):
        return self.userId;