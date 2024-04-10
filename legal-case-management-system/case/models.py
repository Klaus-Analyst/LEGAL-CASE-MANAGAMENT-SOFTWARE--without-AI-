from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

#..............Client Model............#

class client_detail(models.Model):
    GENDER_CHOICES = [ ('Male','Male'), ('Female','Female'), ('Other','Other'),]
    COUNTRY_CHOICES = [ ('pakistan','Pakistan'),('Other','Other'),]
    CITY_CHOICES = [ ('Peshawar','Peshawar'), ('Lahore','Lahore'), ('Islamabad','islamabad'),]
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 11 digits allowed."
        )
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    address = models.CharField(max_length=50, default='')
    country = models.CharField( max_length=9, choices=COUNTRY_CHOICES)
    city = models.CharField(max_length=9,choices=CITY_CHOICES)
    gender = models.CharField(max_length=7,choices=GENDER_CHOICES)
    contact = models.CharField(validators=[phone_regex], max_length=11, blank=True)
    email = models.EmailField(max_length=50)
    refname = models.CharField(max_length=50)
    refcontact = models.CharField(validators=[phone_regex], max_length=11, blank=True)


    def __str__(self):
        return self.fname +" " + self.lname
    

#..............Client Model End............#


#..............Team Member............#

class team_member(models.Model):
    COUNTRY_CHOICES = [ ('pakistan','Pakistan'),('O','Other'),]
    CITY_CHOICES = [ ('peshawar','Peshawar'), ('islamabad','Islamabad'), ('lahore','Lahore'),]
    ROLE_CHOICES = [ ('Admin','Administratore'), ('Data_Entry','Data_Entry'),]
    
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 11 digits allowed."
        )
    fname = models.CharField(max_length=50 ,null=True, blank=True)
    lname = models.CharField(max_length=50  ,null=True ,blank=True)
    profile = models.ImageField(upload_to='profile/')
    contact = models.CharField(validators=[phone_regex], max_length=11, blank=True)
    email = models.EmailField(max_length=50 ,null=True, blank=True)
    address = models.CharField(max_length=50 ,null=True ,blank=True)
    password = models.CharField(max_length=15 ,null=True, blank=True)
    zip_code = models.CharField(max_length=7 , blank=True)
    country = models.CharField(max_length=9,choices=COUNTRY_CHOICES ,null=True, blank=True)
    city = models.CharField(max_length=10,choices=CITY_CHOICES ,null=True ,blank=True)
    role = models.CharField(max_length=11,choices=ROLE_CHOICES ,null=True, blank=True)

    def __str__(self):
        return self.fname +" " + self.lname
    


#..............Team Member End............#




#..............Appiontment start............#


class appiontment(models.Model):
   
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 11 digits allowed."
        )
    name = models.CharField(max_length=50 ,null=True, blank=True)
    address = models.CharField(max_length=100,null=True ,blank=True)
    contact = models.CharField(validators=[phone_regex], max_length=11, blank=True ,null=True)
    date = models.CharField(max_length=15,null=True ,blank=True)
    time = models.CharField(max_length=15,null=True, blank=True)

    
    def __str__(self):
        return self.name
    


 
#..............Appiontment End............#



#..............Case Status Start............#

class case_status(models.Model):
   
    status_name = models.CharField(max_length=50 ,null=True, blank=True)
    discription = models.CharField(max_length=500,null=True ,blank=True)

    def __str__(self):
        return self.status_name +" " + self.discription
    

#..............Case status End............#


#..............Case Status Start............#

class case_type(models.Model):
   
    type_name = models.CharField(max_length=50 ,null=True, blank=True)
    discription = models.CharField(max_length=500,null=True ,blank=True)

    def __str__(self):
        return self.type_name +" "+ self.discription
    

#..............Case status End............#

#..............Court Start............#

class court(models.Model):
   
    court_name = models.CharField(max_length=100 ,null=True, blank=True)
    detail = models.CharField(max_length=500,null=True ,blank=True)

    def __str__(self):
        return self.court_name
    

#..............Court End............#

#..............Court type Start............#

class court_type(models.Model):
   
    court_type_name = models.CharField(max_length=100 ,null=True, blank=True)
    detail = models.CharField(max_length=500,null=True ,blank=True)

    def __str__(self):
        return self.court_type_name 
    

#..............Court type End............#

#.............. judge Start............#

class judge(models.Model):
   
    judge_name = models.CharField(max_length=100 ,null=True, blank=True)
    detail = models.CharField(max_length=500,null=True ,blank=True)

    def __str__(self):
        return self.judge_name
    

#..............judge End............#

#..............services Start............#

class services(models.Model):
   
    service_name = models.CharField(max_length=100 ,null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)
    detail = models.CharField(max_length=500,null=True ,blank=True)

    def __str__(self):
        return self.service_name
    

#..............services End............#

#..............services Start............#

class taxes(models.Model):
   
    tax_name = models.CharField(max_length=100 ,null=True, blank=True)
    percentage = models.IntegerField(null=True, blank=True)
    detail = models.CharField(max_length=500,null=True ,blank=True)

    def __str__(self):
        return self.tax_name
    

#..............services End............#


#..............Case Detail start............#

class case_detail(models.Model):

    client_name = models.CharField(max_length=200, null=True, blank=True)
    adovcate_name = models.CharField(max_length=100, null=True, blank=True)
    case_type_name = models.CharField(max_length=100, null=True, blank=True)
    case_no = models.IntegerField(null=True, blank=True)
    respondent_name = models.CharField(max_length=100,null=True ,blank=True)
    case_status_name = models.CharField(max_length=100, null=True, blank=True)
    act = models.CharField(max_length=100,null=True, blank=True)
    next_date = models.CharField(max_length=20,null=True, blank=True)
    filing_no = models.IntegerField(null=True, blank=True)
    filing_date = models.CharField(max_length=20,null=True ,blank=True)
    reg_no = models.IntegerField(null=True, blank=True)
    reg_date = models.CharField(max_length=20,null=True, blank=True)
    hiring_date = models.CharField(max_length=20,null=True, blank=True)
    cnr_no = models.IntegerField(null=True ,blank=True)
    description = models.CharField(max_length=500,null=True, blank=True)


    #............FIR detail..............
    police_station_name = models.CharField(max_length=200,null=True, blank=True)
    fir_no = models.IntegerField(null=True ,blank=True)
    fir_date = models.CharField(max_length=20, blank=True)

     #............Court detail..............
    court_no = models.IntegerField(null=True ,blank=True)
    court_name = models.CharField(max_length=200, null=True, blank=True)
    court_type_name = models.CharField(max_length=200, null=True, blank=True)
    judge_name = models.CharField(max_length=200,null=True, blank=True)
    judge_type_name = models.CharField(max_length=200, null=True, blank=True)
    

#..............Case Detail End............#

#..............Invioce start............#

class invioces(models.Model):

    client_name = models.CharField(max_length=200, null=True, blank=True)
    invioce_no = models.IntegerField(null=True, blank=True)
    invioce_date = models.CharField(max_length=100, null=True, blank=True)
    services_name = models.CharField(max_length=100, null=True, blank=True)
    services_description = models.CharField(max_length=100,null=True ,blank=True)
    taxes_name = models.CharField(max_length=100,null=True, blank=True)
    taxes_description = models.CharField(max_length=20,null=True ,blank=True)
    qty = models.IntegerField(null=True, blank=True)
    amount = models.IntegerField(null=True ,blank=True)
    due = models.IntegerField(null=True ,blank=True)
    pay = models.IntegerField(null=True ,blank=True)
    total_amount = models.IntegerField(null=True ,blank=True)

    def __str__(self):
        return self.client_name
    
#..............Invioce End............#

#..............payment start............#

class payment(models.Model):

    invioce_no = models.IntegerField(null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)
    payment_method = models.CharField(max_length=100, null=True, blank=True)
    note = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True,blank=True,null=True)

    def __str__(self):
        return self.amount

    
#..............payment End............#


#................Login start..........#

