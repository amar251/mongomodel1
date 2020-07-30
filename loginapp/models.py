from django.db import models


class MyModel(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    password=models.CharField(max_length=200)
    down_letter_array= models.CharField(max_length=200)
    press_time_array= models.CharField(max_length=200)
    down_time= models.CharField(max_length=200)
    up_time= models.CharField(max_length=200)
    up_letter_array= models.CharField(max_length=200)

    def __str__(self):
        return self.name

