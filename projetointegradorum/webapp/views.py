
# Createfrom django.shortcuts import render

# Create your views here.
from django.forms.utils import to_current_timezone
from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import RequestContext, context
from django.core.mail import send_mail, BadHeaderError
from webapp.forms import MeuFormularioForm



def home(request):
    return render(request, 'home.html')

def faq(request):
    return render(request, 'faq.html')


def sobre(request):
    return render(request, 'sobre.html')    

@login_required 
def formulario1(request):
    form = MeuFormularioForm(request.POST or None)
    if request.method == 'POST':
        form = MeuFormularioForm(request.POST)
        if form.is_valid():
         saved_instance = form.save(commit=True)
         return render(request, 'sucesso.html', {'form':  MeuFormularioForm(instance=saved_instance)})  
        else:
            print('error')
    return render(request, 'formulario1.html', {'form': form})
   
   

@login_required 
def formulario2(request):
    return render(request, 'formulario2.html')


# Create your views here.
