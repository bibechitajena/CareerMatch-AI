
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages


def register(request):

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            messages.success(
                request,
                "Your account has been created successfully!"
            )

            return redirect('upload_resume')

    else:

        form = UserCreationForm()

    return render(request, 'accounts/register.html', {
        'form': form
    })
