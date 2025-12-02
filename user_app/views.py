from django.shortcuts import render,redirect

# Create your views here.
from django.views.generic import View
from user_app.forms import*
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout

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
        return render(request, "login.html", {"form": form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
        return render(request, "register.html", {"form": form})
    
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("login")    
    
    # items(CRUD)
# create
class ItemCreateView(View):
    def get(self, request):
        form = Formitem()
        return render(request, "create_form.html", {"form": form})    
    
    def post(self, request):
        form = Formitem(request.POST)
        if form.is_valid():
             item = form.save(commit=False)
             item.user = request.user
             item.save()
        return render(request, "create_form.html", {"form": form})
    
# list    

class ItemListView(View):
    def get(self, request):
        items = Item.objects.filter(user=request.user)
        return render(request, "list_item.html", {"items": items})

# update

class ItemUpdateView(View):
    def get(self, request,**kwargs):
        item = kwargs.get("pk")
        if item.user != request.user:
            return redirect("list_item")
        form = Formitem(instance=item)
        return render(request, "update_form.html", {"form": form})
    
    def post(self, request,**kwargs):
        item = kwargs.get("pk")
        if item.user != request.user:
            return redirect("list_item")
        form = Formitem(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("list_item")
        return render(request, "update_form.html", {"form": form})
    
# delete    

class ItemDeleteView(View):
    def get(self, request, **kwargs):
        item = kwargs.get("pk")
        if item.user != request.user:
            return redirect("list_item")
        item.delete()
        return redirect("list_item")
