from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from .serializers import UserRegistrationSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from django.middleware.csrf import get_token

class UserListView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

def get_csrf_token(request):
    token = get_token(request)
    return JsonResponse({'csrfToken': token})