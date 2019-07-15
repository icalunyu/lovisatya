from django.shortcuts import render, redirect
from cms.models import Rsvp, Code
from cms.forms import InvitationForms
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.
def index(request):
    if request.method == 'POST':
        rsvp_form = InvitationForms(request.POST)
        if rsvp_form.is_valid() and request.POST.get("keypass") != 'NGOMBECIU' and request.POST.get("keypass") != '':
            messages.error(request, 'gagal.')
        elif rsvp_form.is_valid() and request.POST.get("keypass") == 'NGOMBECIU':
            rsvp_form.save()
            messages.success(request, 'berhasil.')
            return redirect('dresscode')
        elif rsvp_form.is_valid() and request.POST.get("keypass") == '':
            rsvp_form.save()
            messages.success(request, 'berhasil.')
            return redirect('thanks')
    else:
        rsvp_form = InvitationForms()
    return render(request, 'index.html', {'form': rsvp_form})

def thanks(request):
    return render(request, 'thanks.html')

def dresscode(request):
    return render(request, 'dresscode.html')

def validate_code(request):
    keypass = request.GET.get('keypass', None)
    data = {
        'is_true': Code.objects.filter(code__iexact=keypass).exists()
    }
    return JsonResponse(data)

# TODO: 1. validasi ngombeciu; 2. kalo codenya bener, arahin ke thanks, kalo salah, kasi alert, kalo gak pake code, ke thanks2
