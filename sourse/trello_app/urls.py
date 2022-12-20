from django.urls import path

from trello_app.views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('boards/', BoardListView.as_view(), name='board_list'),
    path('board/<int:pk>/', BoardDetailView.as_view(), name='board_detail'),
    path('board/<int:board_id>/list/<int:list_id>/card/<int:pk>/', CardView.as_view(), name='card'),

    path('board-create/', BoardCreateView.as_view(), name='board_create'),
    path('board-update/<int:pk>', BoardUpdateView.as_view(), name='board_update'),
    path('board-delete/<int:pk>', BoardDeleteView.as_view(), name='board_delete'),

    path('board/<int:board_id>/list-create/', ListCreateView.as_view(), name='list_create'),
    path('board/<int:board_id>/list-update/<int:pk>/', ListUpdateView.as_view(), name='list_update'),
    path('board/<int:board_id>/list-delete/<int:pk>/', ListDeleteView.as_view(), name='list_delete'),

    path('board/<int:board_id>/list/<int:list_id>/card-create/', CardCreateView.as_view(), name='card_create'),
    path('board/<int:board_id>/list/<int:list_id>/card-update/<int:pk>', CardUpdateView.as_view(), name='card_update'),
    path('board/<int:board_id>/list/<int:list_id>/card-delete/<int:pk>', CardDeleteView.as_view(), name='card_delete'),

    path('board/<int:board_id>/list/<int:list_id>/card/<int:card_id>/mark-create/', MarkCreateView.as_view(),
         name='mark_create'),
    path('board/<int:board_id>/list/<int:list_id>/card/<int:card_id>/mark-update/<int:pk>/', MarkUpdateView.as_view(),
         name='mark_update'),
    path('board/<int:board_id>/list/<int:list_id>/card/<int:card_id>/mark-delete/<int:pk>/', MarkDeleteView.as_view(),
         name='mark_delete'),

    path('board/<int:board_id>/list/<int:list_id>/card/<int:card_id>/checklist-create/', CheckListCreateView.as_view(),
         name='checklist_create'),
    path('board/<int:board_id>/list/<int:list_id>/card/<int:card_id>/checklist-update/<int:pk>/',
         CheckListUpdateView.as_view(), name='checklist_update'),
    path('board/<int:board_id>/list/<int:list_id>/card/<int:card_id>/checklist-delete/<int:pk>/',
         CheckListDeleteView.as_view(), name='checklist_delete'),

    path('board/<int:board_id>/list/<int:list_id>/card/<int:card_id>/checklist/<int:checklist_id>/items-create/',
         CheckListItemsCreateView.as_view(), name='checklist__items_create'),
    path('board/<int:board_id>/list/<int:list_id>/card/<int:card_id>/checklist/<int:checklist_id>/items-update/<int:pk>/',
        CheckListItemsUpdateView.as_view(), name='checklist__items_update'),
    path('board/<int:board_id>/list/<int:list_id>/card/<int:card_id>/checklist/<int:checklist_id>/items-delete/<int:pk>/',
            CheckListItemDeleteView.as_view(), name='checklist__items_delete'),


    path('board/<int:board_id>/list/<int:list_id>/card/<int:card_id>/add-comment/', CommentCreateView.as_view(),
         name='comment_create'),
    path('board/<int:board_id>/list/<int:list_id>/card/<int:card_id>/update-comment/<int:pk>',
         CommentUpdateView.as_view(), name='comment_update'),
    path('board/<int:board_id>/list/<int:list_id>/card/<int:card_id>/delete-comment/<int:pk>',
         CommentDeleteView.as_view(), name='comment_delete'),

]
