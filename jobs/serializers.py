from rest_framework import serializers
from .models import Job, CV
from .models import ContactRequest


class ContactRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactRequest
        fields = '__all__'  


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['id','title', 'description', 'location', 'company_name', 'type','posted_at']  # Match the model fields
        read_only_fields = ['id','posted_at']  # Optional: Make posted_at read-only

# class CVSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CV
#         fields = '__all__'

# class CVSerializer(serializers.ModelSerializer):
   
#     class Meta:
#         model = CV
#         fields =['id','name', 'email', 'phone', 'age', 'salary', 'file', 'accept_terms', 'job','submitted_at']
        
#     # job = JobSerializer()
class CVSerializer(serializers.ModelSerializer):
    job_title = serializers.CharField(source='job.title', read_only=True)  # Fetch the job title from the related Job model
    company_name=serializers.CharField(source='job.company_name', read_only=True)
    class Meta:
        model = CV
        fields = ['id', 'name', 'email', 'phone', 'age', 'salary', 'file', 'accept_terms', 'job', 'submitted_at', 'job_title','company_name']
        read_only_fields = ['job_title','company_name'] 



    # def get_job(self, obj):
    #     # Return job details if a related job exists
    #     if obj.job:
    #        return {"id": obj.job.id, "title": obj.job.title}
    #     return None