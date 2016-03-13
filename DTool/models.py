import datetime
from django.db import models
from django.forms import ModelForm

class User(models.Model):
    name = models.CharField(max_length=20)

TRANSMISSION_SELECT = (
    ('Aвтомат','Автоматическая'),
    ('Mеханика','Механическая'),
)

GEARING_SELECT = (
    ('Передний','Передний'),
    ('Задний','Задний'),
    ('Полный','Полный'),
)

BODY_SELECT = (
    ('Седан','Седан'),
    ('Универсал','Универсал'),
    ('Хетчбэк','Хетчбэк'),
    ('Купе','Купе'),
    ('Минивэн','Минивэн'),
    ('Пикап','Пикап'),
    ('Фургон','Фургон'),
    ('Кабриолет','Кабриолет'),
    ('Микроавтобус','Микроавтобус'),
    ('Лимузин','Лимузин'),
)

YEAR_CHOICES = [(r,r) for r in range(1984, datetime.date.today().year+1)]

FUEL_SELECT = (
    ('Бензин АИ-80','Бензин АИ-80'),
    ('Бензин АИ-92','Бензин АИ-92'),
    ('Бензин АИ-95','Бензин АИ-95'),
    ('Бензин АИ-98','Бензин АИ-98'),
    ('Дизельное топливо','Дизельное топливо'),
    ('ГАЗ','ГАЗ'),
)

class Car(models.Model):
    class Meta():
        db_table = 'Car'
    vin = models.CharField(max_length=50, unique=True)
    number = models.CharField(max_length=10)
    brand = models.CharField(max_length=40)
    model =  models.CharField(max_length=40)
    year = models.IntegerField(max_length=4, choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    engine = models.FloatField()
    horsepower = models.IntegerField()
    transmission = models.CharField(max_length=20,choices=TRANSMISSION_SELECT, default='Не выбрано')
    gearing = models.CharField(max_length=20,choices=GEARING_SELECT, default='Не выбрано')
    fuel = models.CharField(max_length=30,choices=FUEL_SELECT, default='Не выбрано')
    mileage = models.IntegerField()
    body = models.CharField(max_length=20,choices=BODY_SELECT, default='Не выбрано')
    color = models.CharField(max_length=30)
    image = models.ImageField(null=True, blank=True)
    sell = models.BooleanField()
    notes = models.IntegerField()
    owner_id = models.IntegerField()

    def __str__(self):
        return self.vin

class CarForm(ModelForm):
    class Meta:
        model = Car
        exclude = ['notes','owner_id']

class Service(models.Model):
    class Meta():
        db_table = 'Service'
    who = models.CharField(max_length=100)
    what = models.CharField(max_length=1000)
    details = models.CharField(max_length=100)
    when = models.DateField()
    price = models.FloatField()
    reserve = models.IntegerField()
    car_id = models.IntegerField()
    start_mileage = models.IntegerField()

    def __str__(self):
        return self.what

class ServiceForm(ModelForm):
    class Meta:
        model = Service
        exclude = ['car_id','start_mileage']

class Cost(models.Model):
    class Meta():
        db_table = 'Cost'
    what = models.CharField(max_length=1000)
    when = models.DateField()
    price = models.FloatField(max_length=20)
    car_id = models.IntegerField()

    def __str__(self):
        return self.what

class CostForm(ModelForm):
    class Meta:
        model = Cost
        exclude = ['car_id']

class Notification(models.Model):
    class Meta():
        db_table = 'Notification'
    header = models.CharField(max_length=100)
    business = models.CharField(max_length=500)
    time = models.DateField()
    done = models.BooleanField()
    car_id = models.IntegerField()

    def __str__(self):
        return self.header

class NotificationForm(ModelForm):
    class Meta:
        model = Notification
        exclude = ['done','car_id']

class Mark(models.Model):
    class Meta:
        db_table = 'Mark'
    header = models.CharField(max_length=100)
    description = models.CharField(max_length=3000)
    date = models.DateField()
    car_id = models.IntegerField()

    def __str__(self):
        return self.header

class MarkForm(ModelForm):
    class Meta():
        model = Mark
        exclude = ['car_id']