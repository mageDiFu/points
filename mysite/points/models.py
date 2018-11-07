from django.db import models
import datetime

# Create your models here.
class Employee(models.Model):
    employeename = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=40, blank=True, null=True)
    employeeid = models.CharField(primary_key=True, max_length=1)
    initialpoints = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'employee'



    class Meta:
        managed = False
        db_table = 'employee'

class Admin(models.Model):
    adminid = models.BigIntegerField(primary_key=True)
    adminname = models.CharField(max_length=20)
    password = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin'

class Give(models.Model):
    giveid = models.CharField(primary_key=True, max_length=20)
    giverid = models.ForeignKey(Employee, models.DO_NOTHING, db_column='giverid',related_name='giveid')
    reciverid = models.ForeignKey(Employee, models.DO_NOTHING, db_column='reciverid',related_name='reciveid')
    givedate = models.DateField(default=datetime.date.today)
    amount = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'give'

class Use(models.Model):
    useid = models.CharField(primary_key=True, max_length=20)
    employeeid = models.ForeignKey(Employee, models.DO_NOTHING, db_column='employeeid', blank=True, null=True)
    usedate = models.DateField(default=datetime.date.today)
    useamount = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'use'


class RECENT_MONTH_UNUSED_POINTS(models.Model):
    EMPLOYEENAME = models.CharField(primary_key=True, max_length=20)
    UNUSED_POINT = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'RECENT_MONTH_UNUSED_POINTS'

class MONTH_REDEMPTION(models.Model):
    EMPLOYEENAME = models.CharField(primary_key=True, max_length=20)
    MONTH = models.BigIntegerField()
    Times = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'MONTH_REDEMPTION'

class MONTH_USEAGE(models.Model):
    employeename = models.CharField(primary_key=True, max_length=20)
    recivemonth = models.BigIntegerField()
    givemonth = models.BigIntegerField()
    totalrecive = models.BigIntegerField()
    totalgive = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'MONTH_USEAGE'
