
from django.shortcuts import render

from.forms import SignUpForm
from .models import SignUp

# Create your views here.
def home(request):
    title = "Singup Form"
    form = SignUpForm(request.POST or None)

    context = {
        "template_title": title,
        "form": form
    }
    if form.is_valid():
        instance = form.save(commit=False)

        full_name = form.cleaned_data.get("full_name")
        if not full_name:
            full_name = "New full name"
        instance.full_name = full_name
        instance.save()
        context = {
            "template_title": "Thank You"
        }

    # if request.user.is_authenticated() and request.user.is_staff:
    #     queryset = SignUp.objects.all().order_by('-timestamp') #.filter(full_name__iexact="Justin")
    #     context = {
    #         "queryset": queryset
    #     }


    return render(request, "home.html", context)
