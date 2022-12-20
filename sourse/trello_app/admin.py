from django.contrib import admin
from trello_app.models import *

# Register your models here.

admin.site.register(Board)
admin.site.register(List)
admin.site.register(Card)
admin.site.register(CardSignedUser)
admin.site.register(Comment)
admin.site.register(CardMark)
admin.site.register(CheckList)
admin.site.register(CheckListItem)
