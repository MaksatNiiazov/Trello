from django.shortcuts import render


def dashboard(request):
    return render(request, "trello_app/dashboard.html")


