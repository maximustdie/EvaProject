from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .api_views import CPULoadList
from .view import get_cpu_loads, cpu_loads_view

urlpatterns = [
    path("", cpu_loads_view),
    path("get-cpu-loads/", get_cpu_loads),
    path('load/', CPULoadList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
