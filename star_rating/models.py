from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from rest_framework.exceptions import ValidationError

from shop.models import Product, Rating


class Rating(models.Model):
    SCORE_CHOICES = (
        (1, "Terrible"),
        (2, "Poor"),
        (3, "Average"),
        (4, "Very Good"),
        (5, "Excellent"),
    )
    product = models.ForeignKey(Product, related_name='rating',on_delete=models.CASCADE)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    score = models.PositiveSmallIntegerField(
        choices=SCORE_CHOICES, default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])

    def save(self, *args, **kwargs):
        if int(self.score) < 1 or int(self.score) > 5:
            raise ValidationError("Score must be located between 0 to 5")
        super(Rating, self).save(*args, **kwargs)

    class Meta:
        unique_together = ["user"]

    # def __str__(self):
    #     if not settings.STAR_RATINGS_ANONYMOUS:
    #         return "{} rating {} for {}".format(
    #             self.user, self.score, self.rating.content
    #         )
    #     return "{} rating {} for {}".format(self.score, self.rating.content)
