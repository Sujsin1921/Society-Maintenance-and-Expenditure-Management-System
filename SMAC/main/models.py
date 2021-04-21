from django.db import models

# Create your models here.
class Members(models.Model):
    members_id=models.AutoField
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    contact=models.CharField(max_length=30)
    join_date=models.DateField()
    flat_no=models.CharField(max_length=30)  
    paid_upto=models.CharField(max_length=20)
    mode = models.CharField(max_length=20)
    date_at=models.DateField()
    status=models.CharField(max_length=40)
    del_reason=models.CharField(max_length=80)

    def __str__(self):
        return self.name

class expence(models.Model):
    expence_id=models.AutoField
    title=models.CharField(max_length=40)
    description=models.CharField(max_length=400)
    expence_date=models.DateField()
    bill_amount=models.IntegerField()
    images=models.FileField(upload_to="main/expence/images")

    def __str__(self):
        return self.description

class Balance(models.Model):
    collection=models.IntegerField()
    this_month_collection=models.IntegerField()
    expence=models.IntegerField()
    this_month_expence=models.IntegerField()
    balance=models.IntegerField()
    
class Invoice(models.Model):
    invoice_id=models.AutoField
    payee_name=models.CharField(max_length=50)
    date=models.DateField()
    payment_method=models.CharField(max_length=20)
    for_month=models.CharField(max_length=50)
    flat_no=models.CharField(max_length=20)
    amount=models.IntegerField()
    status=models.CharField(max_length=20)
    del_reason=models.CharField(max_length=80)
   

    def __str__(self):
        return self.payee_name

class FestivalFunds(models.Model):
    festival_name=models.CharField(max_length=50)
    payee_name=models.CharField(max_length=50)
    date=models.DateField()
    payment_method=models.CharField(max_length=20)
    flat_no=models.CharField(max_length=20)
    amount=models.IntegerField()
    status=models.CharField(max_length=20)
    del_reason=models.CharField(max_length=50)
    
    def __str__(self):
        return self.festival_name

class EmergencyFunds(models.Model):
    Emergency_purpose=models.CharField(max_length=100)
    payee_name=models.CharField(max_length=30)
    date=models.DateField()
    payment_method=models.CharField(max_length=20)
    flat_no=models.CharField(max_length=20)
    amount=models.IntegerField()
    status=models.CharField(max_length=20)
    del_reason=models.CharField(max_length=50)
    
    def __str__(self):
        return self.Emergency_purpose

class SpecialPurposeFunds(models.Model):
    special_purpose=models.CharField(max_length=100)
    payee_name=models.CharField(max_length=30)
    date=models.DateField()
    payment_method=models.CharField(max_length=20)
    flat_no=models.CharField(max_length=20)
    amount=models.IntegerField()
    status=models.CharField(max_length=20)
    del_reason=models.CharField(max_length=50)
    
    def __str__(self):
        return self.special_purpose