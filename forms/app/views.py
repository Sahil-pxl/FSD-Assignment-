from django.shortcuts import render
from django.shortcuts import render, redirect 
from .forms import FeedbackForm 
def feedback_view(request): 
    if request.method == 'POST': 
        form = FeedbackForm(request.POST) 
        if form.is_valid(): 

# Process the data in form.cleaned_data 
            name = form.cleaned_data['name'] 
            email = form.cleaned_data['email'] 
            message = form.cleaned_data['message'] 
# Redirect to a new URL or display a success message 
            return redirect('thank_you') 
        else: 
            form = FeedbackForm() 
        return render(request, 'feedback.html', {'form': form}) 

