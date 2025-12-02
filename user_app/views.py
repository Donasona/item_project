from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from user_app.forms import*
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm

class Register_view(View):
    def get(self,request):
        form = RegisterForm()
        return render(request,"register.html",{"form":form})
    
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        return render(request, "register.html", {"form": form})
    
class LoginView(View):

    def get(self, request):
        form = AuthenticationForm()
        return render(request, self.template_name, {'form': form})