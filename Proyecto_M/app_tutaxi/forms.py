from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Cliente_f(forms.Form):
    nombre= forms.CharField(max_length=40)
    apellido=forms.CharField(max_length=40)
    registro=forms.DateField()
    movil_asignado=forms.IntegerField()
    
class Movil_f(forms.Form):
    patente= forms.CharField(max_length=40)
    marca=forms.CharField(max_length=40)
    modelo=forms.DateField()
    chofer_asignado=forms.IntegerField()
    
class Chofer_f(forms.Form):
    
    nombre= forms.CharField(max_length=40)
    apellido=forms.CharField(max_length=40)
    nacimiento=forms.DateField()
    movil_a_cargo=forms.IntegerField()
    
#---------------------Form nuevo para Registro de usuario--------------------------    

class UserRegisterForm(UserCreationForm):
    email= forms.EmailField()
    password1= forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2= forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model= User
        fields= ['username','email','password1','password2']
        help_texts= {k:"" for k in fields}

#-----------------------------Form para editar perflil-----------------------------
class UserEditForm(UserCreationForm):
    email= forms.EmailField(label='Correo')
    password1= forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2= forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model= User
        fields= ['email','password1','password2']
        help_texts= {k:"" for k in fields}

 
        
