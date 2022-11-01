from django.db import models
from core.models import BaseModel
from core.enums import Box, review_days
from django.contrib.auth.models import User
import datetime


class Card(BaseModel):
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    question = models.CharField(max_length=255)
    answer = models.TextField()
    box = models.CharField(max_length=2, choices=Box.choices, default=Box.LEVEL_1)
    next_review = models.DateTimeField(default=datetime.datetime.now() + datetime.timedelta(days=1))

    def __str__(self) -> str:
        return self.question

    class Meta:
        verbose_name = "Card"
        verbose_name_plural = "Cards"
        db_table = "website_card"

    def next_level(self, know_it):
        new_box = str(int(self.box) + 1) if know_it else self.Box.LEVEL_1
        review_in_days = review_days["3"]
        if new_box in self.Box:
            self.box = new_box
            review_in_days = review_days[new_box]
        self.next_review = datetime.datetime.now() + datetime.timedelta(days=review_in_days)
        self.save()
        return self
