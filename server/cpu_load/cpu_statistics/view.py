from django.http import JsonResponse
from django.shortcuts import render

from .models import CPULoad


def cpu_loads_view(request):
    return render(request, 'table.html')


def get_cpu_loads(request):
    cpu_loads = CPULoad.objects.order_by("-pub_date")[:100]
    cpu_load_fields = [field.name for field in CPULoad._meta.fields]
    return JsonResponse({"fields": cpu_load_fields, "cpu_loads": list(cpu_loads.values())})
