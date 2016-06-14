from django.conf import settings

from django.core.mail import send_mail

from django.shortcuts import render

from .forms import ContactForm
# Create your view

def contact(request):
    title = "Request Call Back"
    title_align_center = True
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form_email = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("message")
        form_full_name = form.cleaned_data.get("full_name")
        form_phone_number = form.cleaned_data.get("Phone_number")
        # print(email,message,full_name)
        subject = "Request Call back"
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email, 'kldugaronline@gmail.com']
        contact_message = "%s: %s via %s %s"%(
            form_full_name,
            form_message,
            form_email,
            form_phone_number)
        some_html_message = """
        <h1>Hello this is testing</h1>
        """
        send_mail(subject,
                  contact_message,
                  from_email,
                  to_email,
                  html_message=some_html_message,
                  fail_silently=True)

    context = {
        "form": form,
        "title": title,
    }

    return render(request, "forms.html", context)