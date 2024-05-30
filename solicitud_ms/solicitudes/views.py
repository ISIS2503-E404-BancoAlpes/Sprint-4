from django.shortcuts import render

from django.shortcuts import render
from .logic.solicitudes_logic import get_solicitudes ,create_solicitud, get_solicitud
from .forms import SolicitudForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse



def solicitud_list(request):
    solicitudes = get_solicitudes()
    context={'solicitudesList':solicitudes}
    return render(request, 'solicitudes/solicitudes.html',context)


def solicitud_update(request,solicitud_id):
   solicitud= get_solicitud(solicitud_id)
   if request.method == 'POST':
       form= SolicitudForm(request.POST, instance=solicitud)
       if form.is_valid():
        create_solicitud(form) 
        return HttpResponseRedirect(reverse("solicitudesList"))
       else:
        print(form.errors) 
   else: 

       form= SolicitudForm(instance=solicitud)
   context={
           'form': form,
   }    
   return render(request,'solicitudes/update_solicitud.html',context)

def solicitud_create(request):
    if request.method == 'POST':
        form = SolicitudForm(request.POST)
        if form.is_valid():
            create_solicitud(form)
            messages.add_message(request, messages.SUCCESS, 'Successfully created solicitud')
            return HttpResponseRedirect(reverse('solicitudesCreate'))
        else:
            print(form.errors)
    else:
       
       form = SolicitudForm()

    context = {
        'form': form,
    }
    return render(request, 'solicitudes/create_solicitud.html', context)
