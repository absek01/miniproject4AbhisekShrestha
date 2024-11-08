from django.shortcuts import render
from .forms import SampleForm

def home(request):
    return render(request, 'home.html')

def page1(request):
    return render(request, 'page1.html')

def page2(request):
    return render(request, 'page2.html')

def page3(request):
    return render(request, 'page3.html')

def page4(request):
    return render(request, 'page4.html')

def page5(request):
    if request.method == 'POST':
        form = SampleForm(request.POST)
        if form.is_valid():
            # Process the data from the form here
            print(form.cleaned_data)
            return render(request, 'page5.html', {'form': form, 'message': "Form submitted successfully!"})
    else:
        form = SampleForm()
    return render(request, 'page5.html', {'form': form})
