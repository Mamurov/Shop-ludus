from django.db import models



class RatingChoices(models.IntegerChoices):
    BAD = 1, 'Bad'
    LOW = 2, 'Low'
    NORMAL = 3, 'Normal'
    GOOD = 4, 'Good'
    BEST = 5, 'Best'


class Rating(models.Model):
    userId = models.ForeignKey("User", on_delete=models.CASCADE, verbose_name="Пользователь", db_index=True);
    rating = models.IntegerField(choices=RatingChoices.choices)

    def __str__(self):
        return self.userId;