from django.shortcuts import redirect, render, get_object_or_404

from .models import Packages, Contact, Safari, Treknep

# Create your views ere.
def home(request):
    ok = Packages.objects.all()
    return render(request, 'treck/home.html', {'ok': ok}) 
def contact(request):
    if request.method=="POST":
        contacts=Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contacts.name = name
        contacts.email = email
        contacts.subject = subject
        contacts.message = message
        contacts.save()
        return redirect("/")
        
    return render(request, 'treck/contact.html') 

def blog(request):
    return render(request, 'treck/blog.html') 

def testimonials(request):
    return render(request, 'treck/testimonials.html') 

def profile(request):
    return render(request, 'treck/profile.html') 

def gnepal(request):
    return render(request, 'treck/gnepal.html') 

def gbhutan(request):
    return render(request, 'treck/gbhutan.html') 

def safari(request):
    safari = Safari.objects.all()
    return render(request, 'treck/safari.html', {'safari':safari }) 

def nepal(request):
    return render(request, 'treck/nepal.html') 

def trecknep(request):
    trek = Treknep.objects.all()
    return render(request, 'treck/trecknep.html', {'trek': trek}) 

def bhutan1(request, id):
    bhu = get_object_or_404(Packages, pk=id)
    return render(request,'treck/bhutan1.html', {'bhu': bhu}) 

def peak(request):
    return render(request, 'treck/peak.html') 