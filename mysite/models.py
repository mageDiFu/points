# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admin(models.Model):
    adminname = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=40, blank=True, null=True)
    adminid = models.CharField(primary_key=True, max_length=5)

    class Meta:
        managed = False
        db_table = 'admin'


class Areacode(models.Model):
    areaid = models.FloatField(primary_key=True)
    stateid = models.ForeignKey('States', models.DO_NOTHING, db_column='stateid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'areacode'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Customers(models.Model):
    custid = models.FloatField(primary_key=True)
    custname = models.CharField(max_length=35, blank=True, null=True)
    custreg = models.ForeignKey('Managers', models.DO_NOTHING, db_column='custreg', blank=True, null=True)
    custstate = models.CharField(max_length=20, blank=True, null=True)
    custcity = models.CharField(max_length=20, blank=True, null=True)
    custzip = models.IntegerField(blank=True, null=True)
    custseg = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customers'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Employee(models.Model):
    employeename = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=40, blank=True, null=True)
    employeeid = models.CharField(primary_key=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'employee'


class Factcoffee(models.Model):
    productid = models.ForeignKey('Prodcoffee', models.DO_NOTHING, db_column='productid', primary_key=True)
    areaid = models.ForeignKey(Areacode, models.DO_NOTHING, db_column='areaid')
    factdate = models.DateField()
    inventory = models.FloatField(blank=True, null=True)
    budsales = models.FloatField(blank=True, null=True)
    budmargin = models.FloatField(blank=True, null=True)
    budcogs = models.FloatField(blank=True, null=True)
    budprofit = models.FloatField(blank=True, null=True)
    actsales = models.FloatField(blank=True, null=True)
    actmargin = models.FloatField(blank=True, null=True)
    actcogs = models.FloatField(blank=True, null=True)
    actprofit = models.FloatField(blank=True, null=True)
    actexpenses = models.FloatField(blank=True, null=True)
    actmarkcost = models.FloatField(blank=True, null=True)
    quarter = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'factcoffee'
        unique_together = (('productid', 'areaid', 'factdate'),)


class Give(models.Model):
    giveid = models.CharField(primary_key=True, max_length=20)
    giverid = models.ForeignKey(Employee, models.DO_NOTHING, db_column='giverid')
    recieverid = models.ForeignKey(Employee, models.DO_NOTHING, db_column='recieverid')
    givedate = models.DateField()
    amount = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'give'


class Managers(models.Model):
    regid = models.FloatField(primary_key=True)
    region = models.CharField(max_length=10, blank=True, null=True)
    regmanager = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'managers'


class Orderdet(models.Model):
    orderid = models.ForeignKey('Orders', models.DO_NOTHING, db_column='orderid', primary_key=True)
    custid = models.ForeignKey(Customers, models.DO_NOTHING, db_column='custid')
    prodid = models.ForeignKey('Products', models.DO_NOTHING, db_column='prodid')
    ordpriority = models.CharField(max_length=15, blank=True, null=True)
    orddiscount = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    ordshipmode = models.CharField(max_length=15, blank=True, null=True)
    orddate = models.DateField(blank=True, null=True)
    ordshipdate = models.DateField(blank=True, null=True)
    ordshipcost = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    ordqty = models.FloatField(blank=True, null=True)
    ordsales = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orderdet'
        unique_together = (('orderid', 'custid', 'prodid'),)


class Orders(models.Model):
    orderid = models.FloatField(primary_key=True)
    status = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'


class Prodcoffee(models.Model):
    productid = models.FloatField(primary_key=True)
    prodname = models.CharField(max_length=20, blank=True, null=True)
    prodline = models.CharField(max_length=20, blank=True, null=True)
    prodtype = models.CharField(max_length=20, blank=True, null=True)
    prodvar = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prodcoffee'


class Products(models.Model):
    prodid = models.FloatField(primary_key=True)
    prodname = models.CharField(max_length=100, blank=True, null=True)
    prodcat = models.CharField(max_length=30, blank=True, null=True)
    prodsubcat = models.CharField(max_length=30, blank=True, null=True)
    prodcont = models.CharField(max_length=20, blank=True, null=True)
    produnitprice = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    prodmargin = models.DecimalField(max_digits=5, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products'


class StateProductQuarter(models.Model):
    productid = models.FloatField(blank=True, null=True)
    statename = models.CharField(max_length=15, blank=True, null=True)
    quarter = models.CharField(max_length=2, blank=True, null=True)
    total_sales = models.FloatField(blank=True, null=True)
    total_profits = models.FloatField(blank=True, null=True)
    percentage_margin = models.FloatField(blank=True, null=True)
    market_expense = models.FloatField(blank=True, null=True)
    sales_rank_quarters = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'state_product_quarter'


class States(models.Model):
    stateid = models.FloatField(primary_key=True)
    statename = models.CharField(max_length=15, blank=True, null=True)
    statemkt = models.CharField(max_length=15, blank=True, null=True)
    statesize = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'states'


class Use(models.Model):
    useid = models.CharField(primary_key=True, max_length=20)
    employeeid = models.ForeignKey(Employee, models.DO_NOTHING, db_column='employeeid', blank=True, null=True)
    usedate = models.DateField(blank=True, null=True)
    useamount = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'use'
