from django.db import models

class Box(models.TextChoices):
    LEVEL_1 = '1', 'Level 1'
    LEVEL_2 = '2', 'Level 2'
    LEVEL_3 = '3', 'Level 3'

review_days = {'1':1,'2':2,'3':7}
