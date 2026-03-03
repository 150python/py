from django.contrib.admin.utils import display_for_field
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')