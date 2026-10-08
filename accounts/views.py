from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login # Importa com um "apelido" para não dar conflito
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

def register_view(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
      
        if user_form.is_valid(): 
            user_form.save()  # Só pode salvar se for válido!
            return redirect('cars_list') 
    else:
       user_form = UserCreationForm()
        
    return render(request, 'register.html', {'user_form': user_form})

#=====================================================================#
# Views da tela de login                                              #
#=====================================================================#

def login_view(request):
    if request.method == 'POST':
        # É altamente recomendável usar o AuthenticationForm para validar os dados do POST
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            # O form já valida e limpa o usuário e senha para você
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                auth_login(request, user) # Aqui usamos o "apelido" que importamos!
                return redirect('cars_list')
    else:
        form = AuthenticationForm()
        
    return render(request, 'login.html', {'login_form': form})