from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, render_to_response, redirect
from django.template.context_processors import csrf
from DTool.models import CarForm, Car, Service, Cost, ServiceForm, CostForm, Notification, NotificationForm, Mark, \
    MarkForm


def home(request):
    if auth.get_user(request).id != None:
        return render(request, 'DTool/my_autos.html', {'username': auth.get_user(request).username, 'autos':Car.objects.filter(owner_id=auth.get_user(request).id)})
    else:
        return render(request, 'DTool/home.html')

def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            args['login_error'] = "Пользователь не найден!"
            return render_to_response('DTool/login.html', args)
    else:
        return render_to_response('DTool/login.html', args)

def logout(request):
    auth.logout(request)
    return redirect("/")

def register(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    if request.POST:
        newuser_form = UserCreationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(username=newuser_form.cleaned_data['username'], password=newuser_form.cleaned_data['password2'])
            auth.login(request, newuser)
            return redirect('/')
        else:
            args['form'] = newuser_form
    return render_to_response('DTool/register.html', args)

def add_auto(request):
    args = {}
    args.update(csrf(request))
    args['form'] = CarForm()
    if request.POST:
        addform = CarForm(request.POST, request.FILES)
        if addform.is_valid():
            some = addform.save(commit=False)
            some.sell = False
            some.notes = 0
            some.owner_id = auth.get_user(request).id
            some.save()
            return my_autos(request)
        else:
            args['form'] = addform
    return render_to_response('DTool/add_auto.html', args)

def my_autos(request):
    return render(request, 'DTool/my_autos.html', {'username': auth.get_user(request).username, 'autos':Car.objects.filter(owner_id=auth.get_user(request).id)})

def service(request, car_id):
    return render(request, 'DTool/service.html', { 'services':Service.objects.filter(car_id=car_id), 'username': auth.get_user(request).username, 'car_identifier':car_id })

def add_service(request, car_id):
    args = {'car_identifier':car_id}
    args.update(csrf(request))
    args['form'] = ServiceForm()
    if request.POST:
        addform = ServiceForm(request.POST)
        if addform.is_valid():
            some = addform.save(commit=False)
            some.car_id = car_id
            some.start_mileage = 0
            some.save()
            return service(request,car_id)
        else:
            args['form'] = addform
    return render_to_response('DTool/add_service.html', args)

def cost(request, car_id):
    return render(request, 'DTool/cost.html', { 'costs':Cost.objects.filter(car_id=car_id), 'services':Service.objects.filter(car_id=car_id), 'username': auth.get_user(request).username, 'car_identifier':car_id})

def add_cost(request, car_id):
    args = {'car_identifier':car_id}
    args.update(csrf(request))
    args['form'] = CostForm()
    if request.POST:
        addform = CostForm(request.POST)
        if addform.is_valid():
            some = addform.save(commit=False)
            some.car_id = car_id
            some.save()
            return cost(request,car_id)
        else:
            args['form'] = addform
    return render_to_response('DTool/add_cost.html', args)

def notification(request, car_id):
    if Car.objects.get(id=car_id).owner_id == auth.get_user(request).id:
        return render(request, 'DTool/notification.html', {'notifications':Notification.objects.filter(car_id=car_id), 'username': auth.get_user(request).username, 'car_identifier':car_id})
    else:
        return render(request, 'DTool/404.html')

def add_notification(request, car_id):
    args = {'car_identifier':car_id}
    args.update(csrf(request))
    args['form'] = NotificationForm()
    if request.POST:
        addform = NotificationForm(request.POST)
        if addform.is_valid():
            some = addform.save(commit=False)
            some.done = False
            some.car_id = car_id
            some.save()
            try:
                this_car = Car.objects.get(id=car_id)
                this_car.notes+=1
                this_car.save()
            except ObjectDoesNotExist:
                raise Http404
            return notification(request,car_id)
        else:
            args['form'] = addform
    return render_to_response('DTool/add_notification.html', args)

def do_notification(request, car_id, note_id):
    if Notification.objects.get(id=note_id):
        this_note = Notification.objects.get(id=note_id)
        this_note.done = True
        this_note.save()
        this_car = Car.objects.get(id=car_id)
        this_car.notes -=1
        this_car.save()
        return notification(request,car_id)
    else:
        return render(request, 'DTool/404.html')

def mark(request,car_id):
    return render(request, 'DTool/mark.html', {'marks':Mark.objects.filter(car_id=car_id), 'car_identifier':car_id, 'username': auth.get_user(request).username})

def add_mark(request, car_id):
    args = {'car_identifier':car_id}
    args.update(csrf(request))
    args['form'] = MarkForm()
    if request.POST:
        addform = MarkForm(request.POST)
        if addform.is_valid():
            some = addform.save(commit=False)
            some.car_id = car_id
            some.save()
            return mark(request,car_id)
        else:
            args['form'] = addform
    return render_to_response('DTool/add_mark.html', args)

def sell(request, car_id):
    if Car.objects.get(id=car_id):
        this_car = Car.objects.get(id=car_id)
        this_car.sell = True
        this_car.save()
        return my_autos(request)
    else:
        return render(request, 'DTool/404.html')

def unsell(request, car_id):
    if Car.objects.get(id=car_id):
        this_car = Car.objects.get(id=car_id)
        this_car.sell = False
        this_car.save()
        return my_autos(request)
    else:
        return render(request, 'DTool/404.html')

def ad(request):
    return render(request, 'DTool/ad.html', {'autos':Car.objects.filter(sell=True)})