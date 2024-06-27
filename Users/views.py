from django.shortcuts import render
from rest_framework.views import APIView
import datetime 
from django.conf import settings
from .serializers import UserSerializer
import jwt
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


def get_user_from_token(request):
    authorization_header = request.META.get('HTTP_AUTHORIZATION')
    if not authorization_header:
        return Response({"error": "Authorization header is missing"}, status=status.HTTP_401_UNAUTHORIZED)
    try:
        token = authorization_header.split(' ')[1]
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms='HS256')
        # Extract the id from the payload
        user_id = payload.get('user_id')
        # Return the id
        return user_id
    except jwt.ExpiredSignatureError:
        return Response({"error": "Token has expired"}, status=status.HTTP_401_UNAUTHORIZED)
    except jwt.InvalidTokenError:
        return Response({"error": "Invalid token"}, status=status.HTTP_401_UNAUTHORIZED)
    except IndexError:
        return Response({"error": "Invalid token format"}, status=status.HTTP_401_UNAUTHORIZED)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_401_UNAUTHORIZED)
    
class SignupView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = generate_jwt_token(user)
            return Response({'token': token}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def generate_jwt_token(user):
    payload = {
        'user_id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24),
        'iat': datetime.datetime.utcnow()
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    return token