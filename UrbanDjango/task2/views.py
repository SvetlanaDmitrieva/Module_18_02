from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class class_temp(TemplateView):
    template_name = 'class_template.html'


def func_temp(request):
    return render(request, 'func_template.html')
