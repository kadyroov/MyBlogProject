from django.shortcuts import render, redirect
from contacts.forms import ContactForm
from contacts.models import Contact

# Create your views here.
#  во вьюшке принимает только POST и GET

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('main-page')
        
    else:
        form = ContactForm()
    return render(request, 'contacts.html', {'form': form})
    
