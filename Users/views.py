from django.shortcuts import render
from rest_framework.views import APIView
import datetime 
from django.conf import settings
from .serializers import UserSerializer
from .models import User
import jwt
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
import requests
from bs4 import BeautifulSoup
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
    
class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            user = User.objects.get(email=email)
            if user.password == password:
                token = generate_jwt_token(user)
                return Response({'token': token}, status=status.HTTP_200_OK)
            return Response({'error': 'Invalid password'}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({'error': 'User does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        
class NewsView(APIView):
    def get(self, request):
        # user_id = get_user_from_token(request)
        # email = request.data.get('email')
        # password = request.data.get('password')
        url = 'https://www.google.com/search?q=josaa&tbm=nws'

    # Headers to mimic a real browser request
        headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
        }

        # Sending the HTTP request with headers
        response = requests.get(url, headers=headers)

        # Checking if the request was successful
        if response.status_code == 200:
        # Ensuring the correct encoding is used
            response.encoding = response.apparent_encoding
            
            # Parsing the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Finding all news articles
            articles = soup.find_all('div', class_='SoaBEf', limit=10)
        
        # List to store title and link of each article
            top_articles = []
            
            # Extracting titles and links
            for article in articles:
                link = article.find('a', class_='WlydOe')['href']
                title = article.find('div', class_='n0jPhd ynAwRc MBeuO nDgy9d').get_text()
                top_articles.append({'title': title, 'link': link})
        
        # Return the top 10 news articles as JSON response
            return JsonResponse({'articles': top_articles})
        else:
        # Return error response if failed to retrieve the webpage
            return JsonResponse({'error': 'Failed to retrieve the webpage'}, status=500)

def generate_jwt_token(user):
    payload = {
        'user_id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24),
        'iat': datetime.datetime.utcnow()
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    return token