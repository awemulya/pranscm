from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect,render
from forms import CreateUserForm


# for superuser
# from django.contrib.auth.decorators import user_passes_test
# @user_passes_test(lambda u: u.is_superuser)

@login_required
def dashboard(request):
	return render(request,'dashboard.html')

@login_required
def add_user(request):
	if request.POST:
		form = CreateUserForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = User.objects.create_user(username)
			user.set_password(password)
			user.save()
			return redirect('/user/add/save/')
	else:
		form = CreateUserForm()
	base_template = 'dashboard.html'
	return render(request,'fileupload/add_user.html',{'form':form, 'base_template':base_template })

@login_required
def save_user(request):
	return render(request,'fileupload/add_user_sucess.html')