from django import forms

from cars.models import (
    tbl_brand,
    tbl_carro,
    tbl_ciclo_vida,
    tbl_cores,
    tbl_perfil_cliente,
    tbl_categoria_origem , 
)

#====================================================================#
# FORMULÁRIO Categoria de Origem 
#====================================================================#

class frm_categoria_origem(forms.ModelForm):
    class Meta:
         # 1. Define qual modelo este formulário representa
         model = tbl_categoria_origem
         # 2. Define quais campos do modelo vão aparecer no formulário HTML
         fields = ['categoria_origem', 'descricao']
         # 3. (Opcional) Define labels amigáveis para os campos no HTML
         labels = {
             'categoria_origem': 'Categoria Origem',
             'descricao': 'Descrição',
         }
         # 4. (Opcional) Define classes CSS ou atributos extras para renderizar os inputs
         widgets = {
             'categoria_origem': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: uso do carro'}),
             'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descreva o status...'}),
         }
################################# 
class frmcarro(forms.ModelForm):
    class Meta:
        model = tbl_carro
        fields = '__all__'

    def clean_value(self): 
        value = self.cleaned_data.get('value')
        # Verifica primeiro se 'value' NÃO É None antes de fazer a comparação '<'
        if value is not None and value < 10000: 
            self.add_error('value', 'Valor mínimo do veículo deve ser R$ 10.000')
        return value 

    def clean_factory_year(self): 
        factory_year = self.cleaned_data.get('factory_year')
        # Verifica primeiro se 'factory_year' NÃO É None antes de fazer a comparação '<'
        if factory_year is not None and factory_year < 1975: 
            self.add_error('factory_year', 'Só aceita carros fabricados após o ano de 1975')  
        return factory_year
#====================================================================#
# FORMULÁRIO DO CICLO DE VIDA (Usando ModelForm)
#====================================================================#
class frmCicloVida(forms.ModelForm):
    class Meta:
        # 1. Define qual modelo este formulário representa
        model = tbl_ciclo_vida
        # 2. Define quais campos do modelo vão aparecer no formulário HTML
        fields = ['ciclo_vida', 'descricao']
        # 3. (Opcional) Define labels amigáveis para os campos no HTML
        labels = {
            'ciclo_vida': 'Ciclo de Vida',
            'descricao': 'Descrição',
        }
        # 4. (Opcional) Define classes CSS ou atributos extras para renderizar os inputs
        widgets = {
            'ciclo_vida': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Revisão, Em trânsito'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descreva o status...'}),
        }

#====================================================================#
# FORMULÁRIO PERFIL DO CLIENTE  (Usando ModelForm)
#====================================================================#
class frm_perfil_cliente(forms.ModelForm):
    class Meta:
        # 1. Define qual modelo este formulário representa
        model = tbl_perfil_cliente
        # 2. Define quais campos do modelo vão aparecer no formulário HTML
        fields = ['perfil_cliente', 'descricao']
        # 3. (Opcional) Define labels amigáveis para os campos no HTML
        labels = {
            'perfil_cliente': 'Perfil Cliente',
            'descricao': 'Descrição',
        }
        # 4. (Opcional) Define classes CSS ou atributos extras para renderizar os inputs
        widgets = {
            'perfil_cliente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Revisão, Em trânsito'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descreva o status...'}),
        }
       