from django import forms
from trello_app.models import *


class BoardCreateForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = '__all__'


class ListCreateForm(forms.ModelForm):
    class Meta:
        model = List
        fields = '__all__'


class CardCreateForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = '__all__'


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'


class CheckListCreateForm(forms.ModelForm):
    class Meta:
        model = CheckList
        fields = '__all__'


class CheckListItemCreateForm(forms.ModelForm):
    class Meta:
        model = CheckListItem
        fields = '__all__'


class MarkCreateForm(forms.ModelForm):
    class Meta:
        model = CardMark
        fields = '__all__'
