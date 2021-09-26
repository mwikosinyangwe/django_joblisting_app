from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils import timezone




JOB_TYPE = (
    ('Part Time', 'Part Time'),
    ('Full Time', 'Full Time'),
    ('Freelance', 'Freelance'),
)

CATEGORY = (
    ( 'Accountancy', 'Accountancy'),
    ( 'Bar && Restaurant', 'Bar && Restaurant' ),
    ( 'Agriculture', 'Agriculture'),
    ( 'Banking && Finance', 'Banking && Finance'),
    ( 'Education', 'Education'),
    ( 'Engineering', 'Engineering'),
    ('Graphic Design', 'Graphic Design'),
    ( 'Health', 'Health'),
    ( 'Hospitality', 'Hospitality'),
    ('HR', 'HR'),
    ( 'Human Resource', 'IT && Telecoms'),
    ( 'Legal', 'Legal'),
    ( 'Manufacturing', 'Manufacturing'),
    ('Marketing', 'Marketing'),
    ( 'Public Office', 'Public Office'),
    ( 'Public Relations', 'Public Relations'),
    ( 'Retail && Sales', 'Retail && Sales'),
    ('Software Engineering', 'Software Engineering'),
    ( 'Transport && Logistics', 'Transport && Logistics'),
    ( 'Web Design', 'Web Design'),
    ('Web Developing', 'Web Developing'),
    
    
    
)

GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
)


class Job(models.Model):
    
    title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=200)
    employment_status = models.CharField(choices=JOB_TYPE, max_length=10)
    
    gender = models.CharField(choices=GENDER, max_length=30, null=True)
    category = models.CharField(choices=CATEGORY, max_length=30)
    description = models.TextField()
    responsibilities = models.TextField()
    experience = models.CharField(max_length=100)
    job_location = models.CharField(max_length=120)
    company_logo = models.ImageField(upload_to='company_logos', null=True, blank=True)
    Salary = models.CharField(max_length=100, null=True, blank=True)
    application_deadline = models.DateTimeField()
    published_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.title} at {self.company_name}'





