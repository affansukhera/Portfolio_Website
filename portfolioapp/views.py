from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def main(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Combine all the details into one message
        full_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        # Send the email
        send_mail(
            subject,                   # Email subject
            full_message,              # Email message body
            settings.EMAIL_HOST_USER,  # From email (your email settings in settings.py)
            [settings.RECIPIENT_EMAIL],  # To email (ensure this is a valid email to receive)
            fail_silently=False,
        )

        # Add a success message to the context
        context = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': 'Email sent successfully!'
        }
        return render(request, 'index.html', context)
    else:
        return render(request, 'index.html')