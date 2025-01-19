from django.contrib import admin
from .models import Queue  # Yaratgan modelingizni import qiling

# Queue modelini admin panelga qo'shish
class QueueAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'phone', 'address', 'reason')  # Panelda ko'rsatiladigan maydonlar
    search_fields = ('name', 'surname', 'phone')  # Qidirish maydonlari
    list_filter = ('address',)  # Filtrlash
    ordering = ['id']

admin.site.register(Queue, QueueAdmin)  # Modelni admin panelga qo'shish
