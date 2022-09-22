from django.db import models
from django.contrib.admin.widgets import AdminDateWidget

class ipModel(models.Model):
    ip=models.CharField(max_length=255)
    time=models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (("ip", "time"),)

    def __str__(self):
        return self.ip

class Announcement(models.Model):
    UID=models.AutoField(primary_key=True)
    Text=models.TextField()
    link=models.TextField()
    Date=models.DateField(auto_now_add=True)

class Notification(models.Model):
    CHOICES = (
    ('army','army'),
    ('navy', 'navy'),
    ('airforce','airforce'),
    ('paramilitary','paramilitary'),
    ('other','other'),
    )
    UID=models.AutoField(primary_key=True)
    Text=models.TextField()
    link=models.TextField()
    Date=models.DateField(auto_now_add=True)
    from_date = models.DateField()
    end_date = models.DateField()
    SubCategory=models.CharField(max_length=255,choices=CHOICES,editable=True)

class Carrer(models.Model):
    UID=models.AutoField(primary_key=True)
    Text=models.TextField()
    link=models.TextField()
    Date=models.DateField(auto_now_add=True)
    from_date = models.DateField()
    end_date = models.DateField()

class Eligility_Conditions(models.Model):
    UID=models.AutoField(primary_key=True)
    Field=models.CharField(max_length=255)
    Category = models.CharField(max_length=255)
    Age_min = models.IntegerField()
    Age_max = models.IntegerField()
    Qualification = models.CharField(max_length=255)
    Qualification_Percentage = models.CharField(max_length=255)
    Health = models.IntegerField()
    Chest_Expansion = models.IntegerField()
    Without_glass = models.CharField(max_length=255)
    With_glass = models.CharField(max_length=255)
    Color = models.CharField(max_length=255)
    remarks = models.CharField(max_length=255,blank=True)

    class Meta:
        db_table = 'Eligility_Conditions'

class Eligility_Conditions_PF_SP(models.Model):
    UID = models.AutoField(primary_key=True)
    Field = models.CharField(max_length=255)
    Entry = models.CharField(max_length=255)
    Age = models.CharField(max_length=255)
    Education = models.CharField(max_length=255)
    Height = models.CharField(max_length=255)
    weight = models.IntegerField()
    Chest = models.CharField(max_length=255)



# e=Eligility_Conditions(1,'Army', 'Army Engg(only SSB)' ,16,19,'INTER(MPC)',70,157,'5','6/6-6/9','6/6-6/6','CP II')
#         e=Eligility_Conditions(2,'Army', 'Army(Tech)' ,17,23,'INTER(MPC)',50,165,'77-82','6/6-6/6','6/6-6/6','CP II')
#         e=Eligility_Conditions(3,'Army', 'Army(Clerk)' ,17,23,'INTER(ANY GROUP)',50,162,'77-82','6/6-6/6','6/6-6/6','CP II')
#         e=Eligility_Conditions(4,'Army', 'Army(Nursing)' ,17,23,'INTER(Bi.P.C)',50,165,'77-82','6/6-6/6','6/6-6/6','CP II')
#         e=Eligility_Conditions(5,'Army', 'Army(G.D)' ,17,21,'10th Class (PASS)',0,166,'77-82','6/6-6/6','6/6-6/6','CP II')
#         e=Eligility_Conditions(6,'Army', 'Army(T.D)' ,17,21,'10th Class (PASS)',0,166,'77-82','6/6-6/6','6/6-6/6','CP II')


#         e=Eligility_Conditions(7,'Navy', 'Navel Engg' ,16,19,'INTER(MPC)',70,157,'5','6/6-6/9','6/6-6/6','CP II')
#         e=Eligility_Conditions(8,'Navy', 'Navel Artificer(apprentice)' ,17,21,'INTER(MPC)',55,157,'5','6/12-6/12','6/9-6/12','CP II')
#         e=Eligility_Conditions(9,'Navy', 'Navy SSR' ,17,21,'INTER(MPC)',50,157,'50','6/6-6/9','6/6-6/6','CP II')
#         e=Eligility_Conditions(10,'Navy', 'Indian Coast Guard' ,16,19,'INTER(MPC)',100,157,'5','6/18-6/36','6/9-6/9','CP II')
#         e=Eligility_Conditions(11,'Navy', 'Navy(Domestic Branch)' ,16,19,'INTER(MPC)(PASS)',0,157,'5','6/18-6/36','6/9-6/9','CP II')
#         e=Eligility_Conditions(12,'Navy', 'Navy MR/NMR' ,16,19,'INTER(MPC)(PASS)',0,157,'5','6/18-6/36','6/9-6/9','CP II')

#         e=Eligility_Conditions(13,'Air Force', 'TECHNICAL GROUP -X' ,17,21,'INTER(MPC)',50,152,'5','6/36-6/12','6/9-6/6','CP II')
#         e=Eligility_Conditions(14,'Air Force', 'NON-TECHNICAL GROUP-Y' ,17,21,'INTER(ANY GROUP)',50,152,'5','6/18-6/36','6/9-6/6','CP II')
#         e=Eligility_Conditions(15,'Air Force', 'AIR GARUDA POLICE' ,17,21,'INTER(MPC)',50,152,'5','6/6-6/9','6/6-6/6','CP II')
#         e=Eligility_Conditions(16,'Air Force', 'MEDICAL ASSISTANT' ,18,22,'INTER(BiPC)',100,152,'5','6/6-6/9','6/6-6/6','CP II')


        


        # PARAMILITARY,STATE POLICE
        # AR/BSF/CISF/CRPF/ITBP/NSG/SSB	18-23(OC),18-26(OBC),18-28(SC,ST)	SSC	170cms(OC,OBC),162.5(SC,ST)	50	5cm
        # STATE POLICE(CIVIL,AR,TSSP,APSP)	18-23(OC),18-28(BC),18-30(SC,ST)	10+2-PASS(OC/BC),10+2-ATTEND(SC/ST)	167.5cms(OC,BC),162.5(SC,ST)	50	5cm

class Results(models.Model):
    CHOICES = (
    ('Defence','Defence'),
    ('Inter', 'Inter'),
    )
    CHOICES_Image = (
    ('1','1'),
    ('all', 'all'),
    )
   
    Name_Student=models.CharField(max_length=255)
    Field_Student = models.CharField(max_length=255,choices=CHOICES,editable=True)
    Image_Student = models.CharField(max_length=255,choices=CHOICES_Image,editable=True)
    SelectedIN = models.CharField(max_length=255)
    Year = models.DateField()
    Slider_Img = models.ImageField(upload_to='static/media/Results/')
    fields = '__all__'  

# class Slider_home_page_left_top(models.Model):
#     name = models.CharField(max_length=50)
#     Slider_Img = models.ImageField(upload_to='media/home_slider/')
#     fields = '__all__'  


# class testimonial_home_page(models.Model):
#     Name_Student = models.CharField(max_length=255)
#     expressions = models.CharField(max_length=255)
#     Field_Student = models.CharField(max_length=255)
#     Slider_Img = models.ImageField(upload_to='media/home_testimonial/')
#     fields = '__all__'  

# class Selected_candidate_list(models.Model):
#     CHOICES = (
#     ('NDA','NDA'),
#     ('Navy', 'Navy'),
#     ('Inter','Inter'),
#     ('Air-force','Air-Force'),
#     ('Army','Army'),
#     ('State-police','State-police'),
#     )
   
#     Name_Student=models.CharField(max_length=255)
#     Field_Student = models.CharField(max_length=255,choices=CHOICES,editable=True)
#     SelectedIN = models.CharField(max_length=255)
#     District_Student = models.CharField(max_length=255)
#     Slider_Img = models.ImageField(upload_to='media/Selected_candidates/')
#     fields = '__all__'  

# class Media(models.Model):
#     CHOICES=(
#         ('NEWS','NEWS'),
#         ('Videos','Videos'),
#     )
    
#     Name = models.CharField(max_length=255)
#     Link = models.CharField(max_length=10000)
#     Type_of_link = models.CharField(max_length=255,choices=CHOICES,editable=True)
#     img = models.ImageField(upload_to='media/News',blank=True)

# class Gallery(models.Model):
#     Name = models.CharField(max_length=255)
#     img = models.ImageField(upload_to='media/gallery')