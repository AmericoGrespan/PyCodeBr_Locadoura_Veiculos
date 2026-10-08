from django.db import models

#====================================================================#
#Tabela Categoria de Origem   
#====================================================================#

class tbl_categoria_origem(models.Model): 
     id                = models.AutoField(primary_key=True)
     categoria_origem  = models.CharField(max_length=25,blank=True,null=True)
     descricao         = models.CharField(max_length=200,blank=True,null=True)

     def __str__(self):
       return self.categoria_origem  or f"Perfil Sem Nome (ID: {self.id})"

     class Meta:
        db_table = 'tbl_categoria_origem'





#====================================================================#
#Tabela Perfil do Cliente  
#====================================================================#

class tbl_perfil_cliente(models.Model): 
     id              = models.AutoField(primary_key=True)
     perfil_cliente  = models.CharField(max_length=25,blank=True,null=True)
     descricao       = models.CharField(max_length=200,blank=True,null=True)

     def __str__(self):
       return self.perfil_cliente or f"Perfil Sem Nome (ID: {self.id})"

     class Meta:
        db_table = 'tbl_perfil_cliente'


     
#====================================================================#
#Tabela sobre o Ciclo de Vida 
#====================================================================#

class tbl_ciclo_vida(models.Model): 
     id         = models.AutoField(primary_key=True)
     ciclo_vida = models.CharField(max_length=25,blank=True,null=True)
     descricao  = models.CharField(max_length=200,blank=True,null=True)

     def __str__(self):
       return self.ciclo_vida or f"Ciclo Sem Nome (ID: {self.id})"

     class Meta:
        db_table = 'tbl_ciclo_vida'


#====================================================================#
# tabela de Cores 
#====================================================================#
class tbl_cores(models.Model): 
    id     = models.AutoField(primary_key=True)
    cores  = models.CharField(max_length=20,blank=True, null=True)

    def __str__(self):
        return self.cores or f"Cor Sem Nome (ID: {self.id})"
    
    class Meta:
          db_table = 'tbl_cores'
#====================================================================#
# tabela de brand
#====================================================================#
class tbl_brand(models.Model): 
    id    = models.AutoField(primary_key=True)
    brand = models.CharField(max_length=20,blank=True,null=True)

    def __str__(self):
       return self.brand or f"Marca Sem Nome (ID: {self.id})"
 
    class Meta:
          db_table = 'tbl_brand'    

         
#====================================================================#
# tabela de Carros 
#====================================================================#
   
class  tbl_carro(models.Model): 

    id               = models.AutoField(primary_key=True)
    model            = models.CharField(max_length=80,blank=True,null=True) # Modelo
    brand            = models.ForeignKey(tbl_brand, on_delete=models.PROTECT, related_name = 'cars_marca', null=True)
    cor              = models.ForeignKey(tbl_cores, on_delete=models.PROTECT, related_name='cars_cores', null=True)
    ciclo_vida       = models.ForeignKey(tbl_ciclo_vida, on_delete=models.PROTECT, related_name='cars_ciclo',null=True)
    perfil_cliente   = models.ForeignKey(tbl_perfil_cliente,on_delete=models.PROTECT, related_name='cars_cliente',null=True)
    categoria_origem = models.ForeignKey(tbl_categoria_origem,on_delete=models.PROTECT, related_name='cars_origem', null=True)
    factory_year     = models.IntegerField(blank=True, null=True) # Ano Fabricao 
    model_year       = models.IntegerField(blank=True,null=True) # Ano Modelo 
    value            =  models.FloatField(blank=True, null=True) 
    place            = models.CharField(max_length=10,blank=True,null=True)
    photo            = models.ImageField(upload_to='cars/',blank=True,null=True)
    bios             = models.TextField(blank=True,null=True)
   
    def __str__(self):
        return self.model 

    class Meta: 
          db_table = 'tbl_carro'

#====================================================================#
# tabela de CarsInventario     
#====================================================================#

class tbl_carsinventory(models.Model):
    cars_count = models.IntegerField() 
    cars_value = models.FloatField()
    create_at  = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.cars_count} carros - {self.cars_value}"

    class Meta:
        ordering = ['create_at']
        db_table = 'tbl_carsinventory'
######
