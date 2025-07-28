from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

# Root view redirect
def home(request):
    return redirect('upload_resume')  # You can change this to any page you want as the home page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('job_search/', include('job_search.urls')),
    path('', home),  # Redirect root URL to the home view (job_search)
]
