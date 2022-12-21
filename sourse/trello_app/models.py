from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Board(models.Model):
    title = models.CharField(max_length=30, blank=False, null=False)
    image = models.ImageField(blank=False, upload_to='static/board_images')
    created_at = models.DateTimeField(blank=True, auto_now=True)
    users = models.ManyToManyField(User,)

    def __str__(self):
        return self.title


class List(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name="lists")
    title = models.CharField(max_length=30, blank=False, null=False)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Card(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name='cards')
    title = models.CharField(max_length=30, blank=False, null=False)
    description = models.TextField(max_length=500, blank=True, null=True)
    end_date = models.DateField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(max_length=300, blank=False, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now=True)


class CardSignedUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cards = models.ManyToManyField(Card,)


class CheckList(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='checklists')
    title = models.CharField(max_length=100, blank=False)


class CheckListItem(models.Model):
    checklist = models.ForeignKey(CheckList, on_delete=models.CASCADE, related_name='items')
    task = models.CharField(max_length=30, blank=False)
    done = models.BooleanField(default=False)


class CardMark(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='marks')
    text = models.CharField(max_length=20, blank=True)
    color = models.CharField(blank=True, null=False, max_length=8)  # HexCode

