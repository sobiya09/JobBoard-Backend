from rest_framework import serializers
from .models import Job, CV
from .models import ContactRequest


class ContactRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactRequest
        fields = '__all__'  


class JobSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True,required=False, allow_null=True)
    class Meta:
        model = Job
        fields = ['id','title', 'description','minimumqualification', 'location', 'company_name', 'type','posted_at','image']  # Match the model fields
        read_only_fields = ['id','posted_at']  # Optional: Make posted_at read-only

class CVSerializer(serializers.ModelSerializer):
    job_title = serializers.CharField(source='job.title', read_only=True)  # Fetch the job title from the related Job model
    company_name=serializers.CharField(source='job.company_name', read_only=True)
    class Meta:
        model = CV
        fields = ['id', 'name', 'email', 'phone', 'age', 'salary', 'file', 'accept_terms', 'job', 'submitted_at', 'job_title','company_name']
        read_only_fields = ['job_title','company_name'] 

