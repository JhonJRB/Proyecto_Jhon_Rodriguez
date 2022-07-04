from django.views.generic import ListView
from django.http import HttpResponse
from django.shortcuts import render
from app_tutaxi.forms import *
from app_tutaxi.models import * 
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

def inicio(request):
    if request.user.is_authenticated:
        avatares=Avatar.objects.filter(user=request.user.id)
        return render(request,'inicio.html', {'url':avatares[0].imagen.url})
    else:
        return render(request,'inicio.html')
# *************************Carga de datos *****************************************
@login_required 
def cargar_cliente(request):
    if request.method == "POST":
    # request.POST, es un "diccionario" (django...queryDict) con la informacion cargada en el form de "cargar_cliente.html"
        cliente1=Cliente_f(request.POST) #se genera un objeto segun clase(al imprimir se ve un form html)
       
        if cliente1.is_valid():
            clientes=cliente1.cleaned_data # convierte el objeto en un diccionario         
            clientes1= Cliente(nombre=clientes['nombre'], apellido=clientes['apellido'],registro=clientes['registro'],movil_asignado=clientes['movil_asignado'])            
            clientes1.save()       
            return render(request,'ver_cliente.html', {'cliente_registro':clientes1.nombre})
    return render(request,'cargar_cliente.html')
@login_required 
def cargar_movil(request):
    if request.method == "POST":
        movil1=Movil_f(request.POST)
        if movil1.is_valid():
            moviles=movil1.cleaned_data
            moviles1= Movil(patente=moviles['patente'], marca=moviles['marca'],modelo=moviles['modelo'],chofer_asignado=moviles['chofer_asignado'])
            moviles1.save()      
            return render(request,'ver_movil.html',{'movil_registro':moviles1.patente})
    return render(request,'cargar_movil.html')
@login_required    
def cargar_chofer(request):
    if request.method == "POST":
        chofer1=Chofer_f(request.POST)
        if chofer1.is_valid():
            choferes=chofer1.cleaned_data
            choferes1= Chofer(nombre=choferes['nombre'], apellido=choferes['apellido'],nacimiento=choferes['nacimiento'],movil_a_cargo=choferes['movil_a_cargo'])
            choferes1.save()   
            chofer_registro={'chofer_registrado':choferes1.nombre}
            return render(request,'ver_chofer.html',chofer_registro)
    return render(request,'cargar_chofer.html')

# *******************Visualizacion de datos ****************************************
def ver_chofer(request):
    choferes=Chofer.objects.all()  #choferes es un "SET" (django...QuerySet)
    dicc={"chofer":choferes}
    return render(request,'ver_chofer.html', dicc)
    
def ver_cliente(request):
    clientes=Cliente.objects.all()
    dicc={"cliente":clientes}
    return render(request,'ver_cliente.html', dicc)

def ver_movil(request):
    moviles=Movil.objects.all()
    dicc={"movil":moviles}
    return render(request,'ver_movil.html', dicc)

#**********************Busquedad de datos *******************************************
#Buscar Chofer
def buscar_chofer(request):
    return render(request,'buscar_chofer.html')
 
def traer_chofer(request):
    if request.POST['nombre_chofer']:
        nombre1=request.POST['nombre_chofer']
        chofer_1= Chofer.objects.filter(nombre__icontains=nombre1)
        dicc={"chofer":chofer_1}
        return render(request,'ver_chofer.html',dicc)
    return render(request,'buscar_chofer.html')

#Buscar Movil
def buscar_movil(request):
    return render(request,'buscar_movil.html')

def traer_movil(request):
    if request.POST['patente_movil']:
        patente1=request.POST['patente_movil']
        movil_1= Movil.objects.filter(patente__icontains=patente1)
        return render(request,'ver_movil.html',{"movil":movil_1})
    return render(request,'buscar_movil.html')

#Buscar Cliente
def buscar_cliente(request):
    return render(request,'buscar_cliente.html')

def traer_cliente(request):
    if request.POST['nombre_cliente']:
        nombre1=request.POST['nombre_cliente']
        cliente_1= Cliente.objects.filter(nombre__icontains=nombre1)
        return render(request,'ver_cliente.html',{"cliente":cliente_1})
    return render(request,'buscar_cliente.html')

#***************************Delete datos********************************************
@login_required 
def eliminar_chofer(request, id):
    chofer1=Chofer.objects.get(id=id)
    chofer1.delete()
    chofer1=Chofer.objects.all()
    dicc={"chofer":chofer1}
    return render(request,'ver_chofer.html',dicc)
@login_required 
def eliminar_movil(request, id):
    movil1=Movil.objects.get(id=id)
    movil1.delete()
    movil1=Movil.objects.all()
    return render(request,'ver_movil.html',{"movil":movil1})
@login_required 
def eliminar_cliente(request, id):
    cliente1=Cliente.objects.get(id=id)
    cliente1.delete()
    cliente1=Cliente.objects.all()
    return render(request,'ver_cliente.html',{"cliente":cliente1})

#***************************Editar Datos*********************************************
@login_required 
def editar_chofer (request, id):
    
    chofer=Chofer.objects.get(id=id)
    dicc={'chofer':chofer}
    if request.method=="POST":
        chofer1=Chofer_f(request.POST)     
        if chofer1.is_valid():
            datos=chofer1.cleaned_data
            chofer.nombre=datos['nombre']
            chofer.apellido=datos['apellido']
            chofer.nacimiento=datos['nacimiento']
            chofer.movil_a_cargo=datos['movil_a_cargo']
            chofer.save()
            chofer=Chofer.objects.all()
            dicc={'chofer':chofer}
            return render(request,'ver_chofer.html',dicc)   
    return render(request,'editar_chofer.html',dicc)
@login_required 
def editar_movil (request, id):
    
    movile=Movil.objects.get(id=id)
    dicc={'movil':movile}
    if request.method=="POST":
        movile1=Movil_f(request.POST)   
        if movile1.is_valid():
            datos=movile1.cleaned_data
            movile.patente=datos['patente']
            movile.marca=datos['marca']
            movile.modelo=datos['modelo']
            movile.chofer_asigando=datos['chofer_asignado']
            movile.save()
            movile=Movil.objects.all()
            dicc={'movil':movile}
            return render(request,'ver_movil.html',dicc)   
    return render(request,'editar_movil.html',dicc)
@login_required 
def editar_cliente (request, id):
    
    cliente=Cliente.objects.get(id=id)
    dicc={'cliente':cliente}
    if request.method=="POST":
        cliente1=Cliente_f(request.POST)   
        if cliente1.is_valid():
            datos=cliente1.cleaned_data
            cliente.nombre=datos['nombre']
            cliente.apellido=datos['apellido']
            cliente.nacimiento=datos['registro']
            cliente.movil_asigando=datos['movil_asignado']
            cliente.save()
            cliente=Cliente.objects.all()
            dicc={'cliente':cliente}
            return render(request,'ver_cliente.html',dicc)   
    return render(request,'editar_cliente.html',dicc)
#**************************Login request -*******************************************
def login_r (request):
    if request.method=="POST":
       form=AuthenticationForm(request, data=request.POST) 

       if form.is_valid():  
           usuario=form.cleaned_data.get('username')
           clave= form.cleaned_data.get('password') 
           user=authenticate(username=usuario,password=clave)
           if user is not None:
                login(request, user)
                avatares=Avatar.objects.filter(user=request.user.id)               
               # return render(request,"inicio.html", {"url":avatares[0].imagen.url})
                return render(request,"inicio.html",{"mensaje": f"{usuario}", "url":avatares[0].imagen.url})
           else :        
               form=UserRegisterForm()
               return render(request,"registro.html", {'form':form, 'mensaje':"Usuario No registrado"})
       else:
            form=AuthenticationForm()
            return render(request,"login.html", {'form':form, 'mensaje':"Usuario Invalido"})  
    else:
        form =AuthenticationForm()
        return render(request,"login.html",{'form':form})

#***************Registro de usuario *************************************************
def registro(request):
    if request.method=="POST":
        #form=UserCreationForm(request.POST)
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            form.save()
            return render(request,"registro.html",{'mensaje':'Usuario Creado','usuario':username})
        else:
            #form=UserCreationForm()
            form=UserRegisterForm()
            return render(request,"registro.html",{'mensaje':'   !!Datos incorrectos!!', 'form':form})
    else:
        #form=UserCreationForm()
        form=UserRegisterForm()
    return render(request,"registro.html", {'form':form, 'mensaje':"Registro de Usuario"})

#***************Editar_perfil usuario ***********************************************
@login_required
def editar_perfil(request):
    usuario=request.user
    
    if request.method=="POST":
    
        miform=UserEditForm(request.POST)
        
        if miform.is_valid():
    
            dato=miform.cleaned_data
            usuario.email=dato['email']
            password1=dato['password1']
            usuario.set_password(password1) 
            usuario.save()
    
            return render(request,"inicio.html")   
    
    miform=UserEditForm(initial={'email':usuario.email})
    return render(request,"editar_perfil.html",{'miform':miform, 'usuario':usuario}) 

#***************************Agregar AVATAR*******************
"""
def agregar_avatar(request):
    if request.method=="POST":
       pass 
    else:
        formulario=AvatarFormulario()
        return(request,"agregar_avatar.html", {'form':formulario})       
"""
#***************************Aboutme*******************
def aboutme(request):  
    return render(request, 'aboutme.html')