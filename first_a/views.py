from django.shortcuts import render
from django.views.generic import ListView

from first_a.models import Pupil


class PupilView(ListView):
    model = Pupil
    template_name = 'table.html'
