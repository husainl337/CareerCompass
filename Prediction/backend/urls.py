from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib import admin
from django.http import JsonResponse
from django.views import View

class APIRootView(View):
    def get(self, request):
        return JsonResponse({
            'endpoints': {
                'auth': {
                    'signup': '/api/auth/signup/',
                    'signin': '/api/auth/signin/',
                },
                'quiz': '/api/get/quiz/',
                'sentiment': '/api/get/sentiment/',
                'user': '/api/get/user/',
                'chat': '/api/chat/',
                'voice': '/api/voice/',
            }
        })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/api/', permanent=False)),
    path('api/', APIRootView.as_view()),
    path('api/', include('prediction.urls')),   
    path('api/', include('chatapp.urls')),
    path('api/', include('voiceapp.urls')),
]
