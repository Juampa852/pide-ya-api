from django.db import models

# Create your models here.
class Product (models.Model):
    id=models.AutoField(primary_key=True)
    name=models.TextField()
    price=models.DecimalField(decimal_places=2,max_digits=10)
    #image=models.ImageField()

    class Meta:
        ordering=('name',)

class Order (models.Model):
    id=models.AutoField(primary_key=True)
    table=models.CharField(max_length=20)
    total=models.DecimalField(decimal_places=2,max_digits=10)
    date=models.DateTimeField(auto_now_add=True,editable=False)
    products=models.ManyToManyField(Product)
    paid=models.BooleanField(default=False)

    class Meta:
        ordering=('date','table',)