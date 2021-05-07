from django.db import models

# Create your models here.
    
class detail(models.Model):
    C_id=models.AutoField(primary_key=True)
    phone=models.CharField(max_length=20,default="")
    date=models.CharField(max_length=20,default="")
    status=models.CharField(max_length=20,default="")
    remark=models.CharField(max_length=50,default="")
    def __str__(self):
        return str(self.phone)


class Connect_call(models.Model):
    C_id=models.AutoField(primary_key=True)
    phone=models.CharField(max_length=20,default="")
    date=models.CharField(max_length=20,default="")
    status=models.CharField(max_length=20,default="")
    remark=models.CharField(max_length=50,default="")
    def __str__(self):
        return str(self.phone)



class upload_detail(models.Model):
    All_call=models.CharField(max_length=10,default="")
    date=models.CharField(max_length=10,default="")
    filetype=models.CharField(max_length=10,default="")
    def __str__(self):
        return str(self.phone)




