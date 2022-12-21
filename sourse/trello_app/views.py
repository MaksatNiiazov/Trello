from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from trello_app.models import *
from trello_app.forms import *


class BoardListView(ListView):
    template_name = 'trello_app/board_list.html'

    def get_queryset(self):
        return Board.objects.filter(users=self.request.user)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_id'] = self.request.user
        return context


class BoardDetailView(DetailView):
    model = Board
    template_name = 'trello_app/board_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lists'] = List.objects.filter(board_id=self.object.id)
        return context


class BoardUserAddView(UpdateView):
    form_class = BoardCreateForm
    template_name = 'trello_app/board_user.html'


    def get_queryset(self):
        queryset = Board.objects.filter(id=self.kwargs['pk'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.exclude(username=self.request.user)
        context['board_id'] = self.kwargs['pk']
        return context


class ListDetailView(ListView):
    model = List
    template_name = 'trello_app/list_detail.html'


class CardView(DetailView):
    model = Card
    template_name = 'trello_app/card.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(card_id=self.object.id)
        context['checklists'] = CheckList.objects.filter(card_id=self.object.id)
        context['marks'] = CardMark.objects.filter(card_id=self.object.id)
        context['board_id'] = self.kwargs['board_id']
        context['list_id'] = self.kwargs['list_id']
        return context


class BoardCreateView(CreateView):
    form_class = BoardCreateForm
    template_name = 'trello_app/board_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        users = User.objects.get(username=self.request.user)
        print(users)
        context['users'] = users
        return context

    def get_success_url(self):
        return reverse_lazy('board_list')


class BoardUpdateView(UpdateView):
    form_class = BoardCreateForm
    template_name = 'trello_app/board_update.html'

    def get_queryset(self):
        queryset = Board.objects.filter(id=self.kwargs['pk'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.get(username=self.request.user)
        context['board_id'] = self.kwargs['pk']
        return context

    def get_success_url(self):
        return reverse_lazy('board_list')


class BoardDeleteView(DeleteView):
    model = Board


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.get(username=self.request.user)
        context['board_id'] = self.kwargs['pk']
        return context

    def get_success_url(self):
        return reverse_lazy('board_list')


class ListCreateView(CreateView):
    form_class = ListCreateForm
    template_name = 'trello_app/list_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['board_id'] = self.kwargs['board_id']
        return context

    def get_success_url(self):
        return reverse_lazy("board_detail", args=[self.object.board_id])


class ListUpdateView(UpdateView):
    form_class = ListCreateForm
    template_name = 'trello_app/list_update.html'

    def get_queryset(self):
        queryset = List.objects.filter(id=self.kwargs['pk'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['board_id'] = self.kwargs['board_id']
        context['list_id'] = self.kwargs['pk']
        return context

    def get_success_url(self):
        return reverse_lazy("board_detail", args=[self.object.board_id])


class ListDeleteView(DeleteView):
    model = List

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['board_id'] = self.kwargs['board_id']
        context['list_id'] = self.kwargs['pk']
        return context

    def get_success_url(self):
        return reverse_lazy("board_detail", args=[self.object.board_id])


class CardCreateView(CreateView):
    form_class = CardCreateForm
    template_name = 'trello_app/card_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['board_id'] = self.kwargs['board_id']
        context['list_id'] = self.kwargs['list_id']
        return context

    def get_success_url(self):
        return reverse_lazy("board_detail", args=[self.kwargs['board_id']])


class CardUpdateView(UpdateView):
    form_class = CardCreateForm
    template_name = 'trello_app/card_update.html'

    def get_queryset(self):
        queryset = Card.objects.filter(id=self.kwargs['pk'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['board_id'] = self.kwargs['board_id']
        context['list_id'] = self.kwargs['list_id']
        context['card_id'] = self.kwargs['pk']
        return context

    def get_success_url(self):
        return reverse_lazy("card", args=[self.kwargs['board_id'], self.kwargs['list_id'], self.kwargs['pk']])


class CardDeleteView(DeleteView):
    model = Card

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['board_id'] = self.kwargs['board_id']
        context['list_id'] = self.kwargs['list_id']
        context['card_id'] = self.kwargs['pk']
        return context

    def get_success_url(self):
        return reverse_lazy("board_detail", args=[self.kwargs['board_id']])


class MarkCreateView(CreateView):
    form_class = MarkCreateForm
    template_name = 'trello_app/mark_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['board_id'] = self.kwargs['board_id']
        context['list_id'] = self.kwargs['list_id']
        context['card_id'] = self.kwargs['card_id']
        return context

    def get_success_url(self):
        return reverse_lazy("card", args=[self.kwargs['board_id'], self.kwargs['list_id'], self.kwargs['card_id']])


class MarkUpdateView(UpdateView):
    form_class = MarkCreateForm
    template_name = 'trello_app/mark_update.html'

    def get_queryset(self):
        queryset = CardMark.objects.filter(id=self.kwargs['pk'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['board_id'] = self.kwargs['board_id']
        context['list_id'] = self.kwargs['list_id']
        context['card_id'] = self.kwargs['card_id']
        context['pk'] = self.kwargs['pk']
        return context

    def get_success_url(self):
        return reverse_lazy("card", args=[self.kwargs['board_id'], self.kwargs['list_id'], self.kwargs['card_id']])

class MarkDeleteView(DeleteView):
    model = CardMark
    template_name = 'trello_app/mark_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy("card", args=[self.kwargs['board_id'], self.kwargs['list_id'], self.kwargs['card_id']])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['board_id'] = self.kwargs['board_id']
        context['list_id'] = self.kwargs['list_id']
        context['card_id'] = self.kwargs['card_id']
        return context


class CheckListCreateView(CreateView):
    form_class = CheckListCreateForm
    template_name = 'trello_app/checklist_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['board_id'] = self.kwargs['board_id']
        context['list_id'] = self.kwargs['list_id']
        context['card_id'] = self.kwargs['card_id']
        return context

    def get_success_url(self):
        return reverse_lazy("card", args=[self.kwargs['board_id'], self.kwargs['list_id'], self.kwargs['card_id']])


class CheckListUpdateView(UpdateView):
    form_class = CheckListCreateForm
    template_name = 'trello_app/checklist_update.html'

    def get_queryset(self):
        queryset = CheckList.objects.filter(id=self.kwargs['pk'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['board_id'] = self.kwargs['board_id']
        context['list_id'] = self.kwargs['list_id']
        context['card_id'] = self.kwargs['card_id']
        context['pk'] = self.kwargs['pk']
        return context

    def get_success_url(self):
        return reverse_lazy("card", args=[self.kwargs['board_id'], self.kwargs['list_id'], self.kwargs['card_id']])


class CheckListDeleteView(DeleteView):
    model = CheckList

    def get_success_url(self):
        return reverse_lazy("card", args=[self.kwargs['board_id'], self.kwargs['list_id'], self.kwargs['card_id']])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['board_id'] = self.kwargs['board_id']
        context['list_id'] = self.kwargs['list_id']
        context['card_id'] = self.kwargs['card_id']
        return context


class CheckListItemsCreateView(CreateView):
    form_class = CheckListItemCreateForm
    template_name = 'trello_app/checklist__item_create.html'

    def get_queryset(self):
        queryset = CheckListItem.objects.filter(id=self.kwargs['pk'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['board_id'] = self.kwargs['board_id']
        context['list_id'] = self.kwargs['list_id']
        context['card_id'] = self.kwargs['card_id']
        context['checklist_id'] = self.kwargs['checklist_id']

        return context

    def get_success_url(self):
        return reverse_lazy("card", args=[self.kwargs['board_id'], self.kwargs['list_id'], self.kwargs['card_id']])


class CheckListItemsUpdateView(UpdateView):
    form_class = CheckListItemCreateForm
    template_name = 'trello_app/checklist__item_update.html'

    def get_queryset(self):
        queryset = CheckListItem.objects.filter(id=self.kwargs['pk'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['board_id'] = self.kwargs['board_id']
        context['list_id'] = self.kwargs['list_id']
        context['card_id'] = self.kwargs['card_id']
        context['checklist_id'] = self.kwargs['checklist_id']
        context['pk'] = self.kwargs['pk']
        return context

    def get_success_url(self):
        return reverse_lazy("card", args=[self.kwargs['board_id'], self.kwargs['list_id'], self.kwargs['card_id']])


class CheckListItemDeleteView(DeleteView):
    model = CheckListItem

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['board_id'] = self.kwargs['board_id']
        context['list_id'] = self.kwargs['list_id']
        context['card_id'] = self.kwargs['card_id']
        context['checklist_id'] = self.kwargs['checklist_id']
        context['pk'] = self.kwargs['pk']
        return context

    def get_success_url(self):
        return reverse_lazy("card", args=[self.kwargs['board_id'], self.kwargs['list_id'], self.kwargs['card_id']])


class CommentCreateView(CreateView):
    form_class = CommentCreateForm
    template_name = 'trello_app/comment_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['board_id'] = self.kwargs['board_id']
        context['list_id'] = self.kwargs['list_id']
        context['card_id'] = self.kwargs['card_id']
        users = User.objects.get(username=self.request.user)

        context['users'] = users

        return context

    def get_success_url(self):
        return reverse_lazy("card", args=[self.kwargs['board_id'], self.kwargs['list_id'], self.kwargs['card_id']])


class CommentUpdateView(UpdateView):
    form_class = CommentCreateForm
    template_name = 'trello_app/comment_update.html'

    def get_queryset(self):
        queryset = Comment.objects.filter(id=self.kwargs['pk'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['board_id'] = self.kwargs['board_id']
        context['list_id'] = self.kwargs['list_id']
        context['card_id'] = self.kwargs['card_id']
        context['pk'] = self.kwargs['pk']
        return context

    def get_success_url(self):
        return reverse_lazy("card", args=[self.kwargs['board_id'], self.kwargs['list_id'], self.kwargs['card_id']])


class CommentDeleteView(DeleteView):
    model = Comment

    def get_success_url(self):
        return reverse_lazy("card", args=[self.kwargs['board_id'], self.kwargs['list_id'], self.kwargs['card_id']])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['board_id'] = self.kwargs['board_id']
        context['list_id'] = self.kwargs['list_id']
        context['card_id'] = self.kwargs['card_id']
        return context


def dashboard(request):
    return render(request, "trello_app/dashboard.html")


