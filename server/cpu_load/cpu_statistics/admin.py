from django.contrib import admin

from .models import CPULoad


class CPULoadAdmin(admin.ModelAdmin):
    list_display = ["pub_date", "load"]


admin.site.register(CPULoad, CPULoadAdmin)
