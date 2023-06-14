from django.shortcuts import render
from .models import Email

# Create your views here.
def index(request):
    if request.method == "POST":
        email_id = request.POST.get('email')
        subject = request.POST.get('subject')
        composedEmail = request.POST.get('composedEmail')
        composed_email = Email(email_id = email_id, subject = subject, composedEmail = composedEmail)
        composed_email.save()
    return render(request, "index.html")
    # return HttpResponse("hii")
