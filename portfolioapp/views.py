from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def main(request):
    confirmation_message = None

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        full_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        
        send_mail(
                subject,                   
                full_message,              
                settings.EMAIL_HOST_USER,  
                [settings.RECIPIENT_EMAIL], 
                fail_silently=False,
            )

    return render(request, 'index.html')