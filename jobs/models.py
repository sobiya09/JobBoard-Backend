from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import os
from django.core.exceptions import ValidationError


def validate_file_size(value):
    max_size = 5 * 1024 * 1024  # 5MB
    if value.size > max_size:
        raise ValidationError("File size must not exceed 5MB.")

class ContactRequest(models.Model):
    REQUEST_TYPE_CHOICES = [
        ('JOB', 'Job Vacancies'),
        ('OTH', 'Other'),
    ]
    
    ENTITY_TYPE_CHOICES = [
        ('COMPANY', 'Company'),
        ('INDIVIDUAL', 'Individual'),
    ]
    
    request_type = models.CharField(
        max_length=10,
        choices=REQUEST_TYPE_CHOICES,
        default='OTH'
    )
    entity_type = models.CharField(
        max_length=10,
        choices=ENTITY_TYPE_CHOICES,
        default='INDIVIDUAL'
    )
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    file_upload = models.FileField(
        upload_to='uploads/',
        blank=True,
        null=True,
        validators=[validate_file_size]  
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.get_request_type_display()})"

    class Meta:
        db_table = 'contact_requests'
        verbose_name = 'Contact Request'
        verbose_name_plural = 'Contact Requests'


class Job(models.Model):
    JOB_TYPES = [
        ('Full-time', 'Full-time'),
        ('Part-time', 'Part-time'),
        ('Internship', 'Internship'),
        ('Contract', 'Contract'),
        ('Temporary', 'Temporary'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    minimumqualification = models.TextField(default="• Bachelor's Degree\n• 2+ years of experience\n• Strong communication skills")
    location = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=JOB_TYPES, default='Full-time')  # New field
    posted_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='jobsimages/', blank=True, null=True)  # Image upload field

    def __str__(self):
        return self.title

class CV(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, null=True, blank=True) 
    age = models.IntegerField(null=True) 
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    file = models.FileField(upload_to='cvs/')
    submitted_at = models.DateTimeField(default=timezone.now)
    accept_terms = models.BooleanField(default=False)  # Accept Terms checkbox
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        # Dynamically set the upload_to path based on the job's company name and job title
        if self.job:
            company_name = self.job.company_name.replace(" ", "_") 
            job_title = self.job.title.replace(" ", "_")  
            self.file.name = os.path.join('cvs', company_name, job_title, self.file.name)
        super().save(*args, **kwargs)

    def job_title(self):
        return self.job.title

    job_title.short_description = 'Job Title'

    def company_name(self):
        return self.job.company_name