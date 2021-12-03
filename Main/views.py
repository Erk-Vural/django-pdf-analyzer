from django.shortcuts import render, redirect

from Main.forms import *
from Main.models import *
from Main.Services.login import *
from Main.Services.admin_panel import *


# Create your views here.

def login_view(request):
    if request.method == 'POST':
        admin_form = AdminForm(request.POST)
        is_exist = login_admin(admin_form)

        if is_exist:
            return redirect('admin-panel')

    admin_form = AdminForm()

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        is_exist = login_user(user_form)

        if is_exist:
            return redirect('user-panel')

    user_form = UserForm()

    context = {
        'admin_form': admin_form,
        'user_form': user_form
    }

    return render(request, "login.html", context)


def admin_panel_view(request):
    users = read_all_user()

    context = {
        'users': users,
    }

    return render(request, "admin-panel.html", context)


def user_panel_view(request):
    context = {
    }

    return render(request, "user-panel.html", context)