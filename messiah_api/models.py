from django.db import models


# Create your models here.
class Messes(models.Model):
    messID = models.AutoField(primary_key=True, auto_created=True)
    messName = models.CharField(max_length=25)
    password = models.CharField(max_length=100)


class Student(models.Model):
    studentID = models.AutoField(prima  ry_key=True, auto_created=True)
    name = models.CharField(max_length=30)
    rollNo = models.IntegerField()
    messID = models.ForeignKey(Messes, on_delete=models.CASCADE)
    pref = models.CharField(max_length=10)
    password = models.CharField(max_length=100)


class Menu(models.Model):
    menuID = models.AutoField(primary_key=True, auto_created=True)
    messID = models.ForeignKey(Messes, on_delete=models.CASCADE)
    day = models.CharField(max_length=10)
    nameOfFood = models.CharField(max_length=15)
    mealType = models.CharField(max_length=15)


class foodStats(models.Model):
    foodID = models.AutoField(primary_key=True, auto_created=True)
    preparedQ = models.IntegerField()
    consumedQ = models.IntegerField()
    leftoverQ = models.IntegerField()
    menuID = models.ForeignKey(Menu, on_delete=models.CASCADE)


class Visited(models.Model):
    messID = models.ForeignKey(Messes, on_delete=models.CASCADE)
    date = models.CharField(max_length = 25)
    mealType = models.CharField(max_length=15)
    studentID = models.ForeignKey(Student, on_delete=models.CASCADE)


class Reviews(models.Model):
    messID = models.ForeignKey(Messes, on_delete=models.CASCADE)
    review = models.CharField(max_length=100)


