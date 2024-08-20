from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators  import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth.models import User
from  .forms import RegistrationForm

# Create your views here.

#regiter view
def register_view(request):
  if request.method == "POST":
    form = RegistrationForm(request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      # email = form.changed_data.get('email')
      password = form.cleaned_data.get('password')
      user = User.objects.create_user(username=username, password=password)
      login(request, user)
      return redirect('home')
  else:
    form = RegistrationForm()
  return render(request, 'accounts/register.html', { 'form': form })

#login view
def login_view(request):
  if request.method == "POST":
    username = request.POST.get('username') or  request.POST.get('email')
    password = request.POST.get('password')
    user = authenticate(request, user=username, password=password )
    if user is not None:
      login(request, user)
      next_url = request.POST.get('next') or request.GET.get('next') or 'home'
      return redirect(next_url)
  else:
    error = "Invalid Credintials!"
    return render(request, 'accounts/login.html', { 'error': error })

#logout view
def logout_view(request):
  if request.method == "POST":
    logout(request)
    return redirect('login')
  else:
    return redirect('home')

#Home view , using  decorators
@login_required
def home(request):
  return render(request, 'authApp/home.html' )

#Protected view. The view that can only be accessed by the authorized user, user logged in
class ProtectedView(LoginRequiredMixin, View):
  login_url ='/login'
  #next -to redirect URL
  redirect_field_name = 'redirect_to'
  
  def get(self, request):
    return render(request, 'registration/protected.html')