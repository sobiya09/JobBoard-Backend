from rest_framework import viewsets
from .models import Job, CV
from .serializers import JobSerializer, CVSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from django.shortcuts import render
from rest_framework import generics
from .models import ContactRequest
from .serializers import ContactRequestSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated

class LoginView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        else:
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
class ContactRequestListCreateView(generics.ListCreateAPIView):
    queryset = ContactRequest.objects.all()
    serializer_class = ContactRequestSerializer

    

class ContactRequestDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContactRequest.objects.all()
    serializer_class = ContactRequestSerializer



class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    

class CVViewSet(viewsets.ModelViewSet):
    # queryset = CV.objects.all()
    queryset = CV.objects.select_related('job').all()
    serializer_class = CVSerializer

    

@api_view(['POST'])
def add_job(request):
    serializer = JobSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_jobs(request):
    jobs = Job.objects.all()
    serializer = JobSerializer(jobs, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def update_job(request, id):
    job = get_object_or_404(Job, id=id)
    serializer = JobSerializer(instance=job, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Job updated successfully'})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_job(request, id):
    job = get_object_or_404(Job, id=id)
    job.delete()
    return Response({'message': 'Job deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

class CVUploadView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CVSerializer(data=request.data)
        if serializer.is_valid():
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)