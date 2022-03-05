from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username


class Album(models.Model):
    title = models.CharField(max_length=500)
    artist = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    # orignal_release = models.DateField()

    MINT = 'M'
    NEAR_MINT = 'NM'
    VERY_GOOD_PLUS = 'VG+'
    VERY_GOOD = 'VG'
    GOOD_PLUS = 'G+'
    GOOD = 'G'
    FAIR = 'F'
    POOR = 'P'
    CONDITION_CHOICES = [
        (MINT, 'Mint'),
        (NEAR_MINT, 'Near Mint'),
        (VERY_GOOD_PLUS, 'Very Good Plus'),
        (VERY_GOOD, 'Very Good'),
        (GOOD_PLUS, 'Good Plus'),
        (GOOD, 'Good'),
        (FAIR, 'Fair'),
        (POOR, 'Poor'),
    ]
    condition = models.CharField(
        max_length=3,
        choices=CONDITION_CHOICES,
        default=MINT,
    )
