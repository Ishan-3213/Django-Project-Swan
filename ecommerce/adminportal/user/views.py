from django import forms
import django
from django.http.response import  HttpResponse, HttpResponseRedirect, JsonResponse
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages
from django.views.generic import TemplateView, CreateView, View
from .forms import UserForm, UserProfileInfoForm
# Create your views here.


class HomeView(TemplateView):
    template_name = 'userportal/index.html'

class AdminHomeView(TemplateView):
    template_name = 'adminportal/index.html'




class LoginView(TemplateView):
        
    @login_required(login_url='adminportal/login.html')
    def user_logout(request):
        logout(request)
        return HttpResponseRedirect(reverse('admin_customized'))

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:    
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect("user_urls:index")
    
    def get(self, request, *args, **kwargs):
        return render(request, 'adminportal/login.html', {})

    def post(self, request, *args, **kwargs):
        try:
            print("inside user_login func")
            print("Entering Username nd Password")
            username = request.POST.get('username')
            password = request.POST.get('password')

            print("Checking Username nd Password")

            user = authenticate(username=username, password=password)
            print("user", user)
            token, created = Token.objects.get_or_create(user=user)

            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse("user_urls:index"))

                else:
                    return HttpResponse("Account not active")

        except Exception as e:
            messages.add_message(request, messages.INFO, "Please Enter Valid Username or Password")
            return render(request, 'adminportal/login.html', {})


class RegisterUser(CreateView):
    form_class_1 = UserForm
    form_class_2 = UserProfileInfoForm
    template_name = 'adminportal/registration.html'
    

    def get(self, request, *args, **kwargs):
        form_U = self.form_class_1()
        form_P = self.form_class_2()
        return render(request, self.template_name, {'form_U': form_U, 'form_P': form_P})

    def post(self, request, *args, **kwargs):
        form_U = self.form_class_1(request.POST)
        form_P = self.form_class_2(request.POST)
         
        if form_U.is_valid() and form_P.is_valid():
            user = form_U.save()
            user.set_password(user.password)
            user.save()
            profile = form_P.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
            return render(request, 'adminportal/login.html', {})
        else:
            print(form_U.errors, form_P.errors)
            messages.add_message(request, messages.ERROR, messages.error)
            return render(request, self.template_name, context={"login_page" : True})
            raise forms.ValidationError('Please enter valid data')

