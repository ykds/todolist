from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import DetailView, UpdateView
from django.contrib import messages

from .forms import RegisterForm

# Create your views here.
def register(request):
    redirect_to = request.POST.get('next', request.GET.get('next', ''))
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'You have registered an account successfully.')
            if redirect_to:
                return redirect(redirect_to)
            else:
                return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', context={'form': form, 'next': redirect_to})


class ProfileView(DetailView):
    model = User
    template_name = 'users/profile.html'
    context_object_name = 'user'


class ProfilEditView(UpdateView):
    model = User
    template_name = 'users/user_update_form.html'
    fields = ['username']

    def get_success_url(self):
        return '/users/users/profile/'+ str(self.request.user.pk)