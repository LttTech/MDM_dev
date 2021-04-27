from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import UserCaptureForm, CellphoneCaptureForm


def index(request):
    context = {
        'title': 'Home'
    }
    return render(request, 'MDMapp/index.html', context)


@login_required
def enroll(request):

    if request.method == 'POST':
        user_form = UserCaptureForm(request.POST)
        cell_form = CellphoneCaptureForm(request.POST)
        if user_form.is_valid() and cell_form.is_valid():
            name = user_form.cleaned_data['name']
            email = user_form.cleaned_data['email']
            employee_number = user_form.cleaned_data['employee_number']
            department = user_form.cleaned_data['department']
            user_form.save()

    else:
        user_form = UserCaptureForm()
        cell_form = CellphoneCaptureForm()
    return render(request, 'MDMapp/enroll.html',
                  {
                      'title': 'Enroll',
                      'user_form': user_form,
                      'cell_form': cell_form
                  }
                  )


@login_required
def user_info(request):

    if request.method == 'POST':
        user_form = UserCaptureForm(request.POST)
        if user_form.is_valid():
            name = user_form.cleaned_data['name']
            email = user_form.cleaned_data['email']
            employee_number = user_form.cleaned_data['employee_number']
            department = user_form.cleaned_data['department']
            user_form.save()

    else:
        user_form = UserCaptureForm()
    return render(request, 'MDMapp/forms.html', {'user_form': user_form})


@login_required
def cellphone_info(request):

    if request.method == 'POST':
        cell_form = CellphoneCaptureForm(request.POST)
        if cell_form.is_valid():
            phone_manufacturer = cell_form.cleaned_data['phone_manufacturer']
            phone_model = cell_form.cleaned_data['phone_model']
            imei_number = cell_form.cleaned_data['imei_number']
            sim_number = cell_form.cleaned_data['sim_number']
            phone_number = cell_form.cleaned_data['phone_number']
            cell_form.save()

    else:
        cell_form = CellphoneCaptureForm()
    return render(request, 'MDMapp/forms.html', {'cell_form': cell_form})
