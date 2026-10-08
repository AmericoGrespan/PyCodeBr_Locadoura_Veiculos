from django.contrib import admin

from cars.models import (
    tbl_brand,
    tbl_carro,
    tbl_ciclo_vida,
    tbl_cores,
    tbl_perfil_cliente,
    tbl_categoria_origem, 
)

class tbl_categoria_origemAdmin(admin.ModelAdmin): 
    list_display = ('id', 'categoria_origem', 'descricao') 
    search_fields = ('categoria_origem', )
admin.site.register(tbl_categoria_origem, tbl_categoria_origemAdmin)



class tbl_carroAdmin(admin.ModelAdmin): 
    list_display = ('model', 'brand', 'value', 'cor',   'factory_year', 'model_year') 
    search_fields = ('brand', 'model',)
admin.site.register(tbl_carro, tbl_carroAdmin)

class tbl_brandAdmin(admin.ModelAdmin): 
    list_display = ('id', 'brand')
    search_fields = ('brand', )
admin.site.register(tbl_brand, tbl_brandAdmin) # Corrigido aqui

class tbl_coresAdmin(admin.ModelAdmin): # Renomeado para não conflitar com o Model
    list_display = ('id', 'cores')
    search_fields = ('cores', )
admin.site.register(tbl_cores, tbl_coresAdmin) 

class tbl_ciclo_vidaAdmin(admin.ModelAdmin): 
    list_display = ('id', 'ciclo_vida','descricao')
    search_fields = ('ciclo_vida', )
admin.site.register(tbl_ciclo_vida, tbl_ciclo_vidaAdmin) 

class tbl_perfil_clienteAdmin(admin.ModelAdmin): 
    list_display = ('id', 'perfil_cliente','descricao')
    search_fields = ('perfil_cliente', )
admin.site.register(tbl_perfil_cliente, tbl_perfil_clienteAdmin) 
