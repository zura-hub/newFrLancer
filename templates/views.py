from django.shortcuts import render, redirect
from .forms import TempForms
from .models import Temp

def templates(request):
    temps = Temp.objects.all()  # Fetch all Temp objects from database
    return render(request, 'templates/templates.html', {'temps': temps})  # Pass Temp objects to the template

def create_template(request):
    form = TempForms()  # Default form to handle GET request and invalid POST request

    if request.method == 'POST':
        form = TempForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('templates')
        else:
            form = TempForms()# Create a new form instance after saving the valid form
    return render(request, 'templates/create_template.html', {'form': form})
