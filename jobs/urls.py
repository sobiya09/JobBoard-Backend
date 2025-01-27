from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JobViewSet, CVViewSet, CVUploadView
from .views import ContactRequestListCreateView, ContactRequestDetailView
from django.contrib import admin
from rest_framework_simplejwt.views import TokenObtainPairView
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
# router.register('jobs', JobViewSet)
router.register(r'jobs', JobViewSet)
router.register(r'cvs', CVViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/upload_cv/', CVUploadView.as_view(), name='upload_cv'),
    path('api/requests/', ContactRequestListCreateView.as_view(), name='contact_request_list_create'),
    path('api/requests/<int:pk>/', ContactRequestDetailView.as_view(), name='contact_request_detail'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)