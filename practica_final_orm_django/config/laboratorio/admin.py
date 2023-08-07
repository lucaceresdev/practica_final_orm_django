from django.contrib import admin
from .models import Laboratorio, Directorgeneral, Producto

class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'pais', 'ciudad')

class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'especialidad', 'laboratorio')

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'laboratorio', 'pais_laboratorio', 'ciudad_laboratorio', 'f_fabricacion', 'p_costo', 'p_venta')

    def pais_laboratorio(self, obj):
        return obj.laboratorio.pais

    def ciudad_laboratorio(self, obj):
        return obj.laboratorio.ciudad

    pais_laboratorio.short_description = 'Pais'
    ciudad_laboratorio.short_description = 'Ciudad'

admin.site.register(Laboratorio, LaboratorioAdmin)
admin.site.register(Directorgeneral, DirectorGeneralAdmin)
admin.site.register(Producto, ProductoAdmin)
