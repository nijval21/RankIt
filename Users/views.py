from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from .models import User
from .serializers import UserSerializer
import jwt
from django.conf import settings
import datetime 
from django.http import JsonResponse
import requests
from bs4 import BeautifulSoup
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
# import sqlite3
from .models import josaa2023, josaa2022, josaa2021, josaa2020, josaa2019, josaa2018, josaa2017, josaa2016
from django.db.models import Avg, F, IntegerField, ExpressionWrapper, FloatField, Count
from django.db.models.functions import Cast
from django.apps import apps


from selenium.webdriver.support.ui import Select
import requests
import re
import os
# from datetime import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
# Create your views here.



def is_superuser(user):
    return user.is_superuser

@user_passes_test(is_superuser)
def admin_only_view(request):
    # Initialize the Chrome driver using WebDriver Manager
    chrome_options = Options()
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('ignore-certificate-errors')

    driver = webdriver.Chrome(options=chrome_options)

    # Set up Chrome options
    chrome_options = webdriver.ChromeOptions()

    # Navigate to the website
    for i in range(1, 9):
        # ModelClass = 'josaa'
        year ='select'
        if i==1:
            year = '2023'
            ModelClass = josaa2023
        elif i==2:
            year = '2022'    
            ModelClass = josaa2022
        elif i==3:
            year = '2021'    
            ModelClass = josaa2021
        elif i==4:
            year = '2020'   
            ModelClass = josaa2020
        elif i==5:
            year = '2019'    
            ModelClass = josaa2019
        elif i==6:
            year = '2018'    
            ModelClass = josaa2018
        elif i==7: 
            year = '2017'    
            ModelClass = josaa2017
        elif i==8:
            year = '2016'  
            ModelClass = josaa2016  
        # table_name = f'seat{year}'
        # cursor.execute(f'''
        # CREATE TABLE IF NOT EXISTS {table_name} (
        #     round_no TEXT,
        #     institute_type TEXT,
        #     institute_name TEXT,
        #     academic_program TEXT,
        #     seat_type TEXT,
        #     gender TEXT,
        #     open_rank TEXT,
        #     close_rank TEXTS
        # )''')
        driver.get('https://josaa.admissions.nic.in/applicant/seatmatrix/openingclosingrankarchieve.aspx')

        # Wait for the dropdowns to be available and interact with them
        wait = WebDriverWait(driver, 5)

        # Select the year
        year_dropdown_wait = wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ContentPlaceHolder1_ddlYear_chosen')))
        year_dropdown_parent = year_dropdown_wait.find_element(By.XPATH, '..')
        year_dropdown_parent.click()
        year_dropdown_search = year_dropdown_wait.find_element(By.CLASS_NAME, 'chosen-search')
        year_dropdown_options = year_dropdown_wait.find_element(By.CLASS_NAME, 'chosen-results')
        year_dropdown_options.find_elements(By.TAG_NAME, 'li')[i].click()

        sleep(2)
        # for j in range()
        # Select the round number
        round_dropdown_wait = wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ContentPlaceHolder1_ddlroundno_chosen')))
        round_dropdown_parent = round_dropdown_wait.find_element(By.XPATH, '..')
        round_dropdown_parent.click()
        round_dropdown_search = round_dropdown_wait.find_element(By.CLASS_NAME, 'chosen-search')
        round_dropdown_options = round_dropdown_wait.find_element(By.CLASS_NAME, 'chosen-results')

        round_dropdown_options.find_elements(By.TAG_NAME, 'li')[6].click()

        sleep(2)

        # Select the institute type
        institute_type_dropdown_wait = wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ContentPlaceHolder1_ddlInstype_chosen')))
        institute_type_dropdown_parent = institute_type_dropdown_wait.find_element(By.XPATH, '..')
        institute_type_dropdown_parent.click()
        institute_type_dropdown_search = institute_type_dropdown_wait.find_element(By.CLASS_NAME, 'chosen-search')
        institute_name_dropdown_options = institute_type_dropdown_wait.find_element(By.CLASS_NAME, 'chosen-results')

        institute_name_dropdown_options.find_elements(By.TAG_NAME, 'li')[3].click()

        sleep(2)

        # Select the institute name
        institute_name_dropdown_wait = wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ContentPlaceHolder1_ddlInstitute_chosen')))
        institute_name_dropdown_parent = institute_name_dropdown_wait.find_element(By.XPATH, '..')
        institute_name_dropdown_parent.click()
        institute_name_dropdown_search = institute_name_dropdown_wait.find_element(By.CLASS_NAME, 'chosen-search')
        institute_name_dropdown_options = institute_name_dropdown_wait.find_element(By.CLASS_NAME, 'chosen-results')

        institute_name_dropdown_options.find_elements(By.TAG_NAME, 'li')[1].click()

        sleep(2)

        # Select the academic program
        academic_program_dropdown_wait = wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ContentPlaceHolder1_ddlBranch_chosen')))
        academic_program_dropdown_parent = academic_program_dropdown_wait.find_element(By.XPATH, '..')
        academic_program_dropdown_parent.click()
        academic_program_dropdown_search = academic_program_dropdown_wait.find_element(By.CLASS_NAME, 'chosen-search')
        academic_program_dropdown_options = academic_program_dropdown_wait.find_element(By.CLASS_NAME, 'chosen-results')

        academic_program_dropdown_options.find_elements(By.TAG_NAME, 'li')[1].click()

        sleep(2)

        # Select the seat type/category
        seat_type_dropdown_wait = wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ContentPlaceHolder1_ddlSeatType_chosen')))
        seat_type_dropdown_parent = seat_type_dropdown_wait.find_element(By.XPATH, '..')
        seat_type_dropdown_parent.click()
        seat_type_dropdown_search = seat_type_dropdown_wait.find_element(By.CLASS_NAME, 'chosen-search')
        seat_type_dropdown_options = seat_type_dropdown_wait.find_element(By.CLASS_NAME, 'chosen-results')

        seat_type_dropdown_options.find_elements(By.TAG_NAME, 'li')[1].click()

        sleep(2)

        # Submit the form
        submit_button = wait.until(EC.element_to_be_clickable((By.ID, 'ctl00_ContentPlaceHolder1_btnSubmit')))
        submit_button.click()

        print("GOT THE TABLE!")
        sleep(5)

        # Wait for the results to be displayed and print the page source
        wait.until(EC.presence_of_element_located((By.ID, 'ctl00_ContentPlaceHolder1_GridView1')))

        # Print the page source or parse it with BeautifulSoup
        page_source = driver.page_source

        # Close the browser

        # Parse the page source with BeautifulSoup
        soup = BeautifulSoup(page_source, 'html.parser')

        # Find the desired table or data
        table = soup.find('table', {'id': 'ctl00_ContentPlaceHolder1_GridView1'})
        rows = table.find_all('tr')[1:]
        # round_no = '6'
        # institute_type = 'Indian Institute of Technology'
        for row in rows:
            cols = row.find_all('td')
            institute_name = cols[0].text.strip()
            academic_program = cols[1].text.strip()
            seat_type = cols[3].text.strip()
            gender = cols[4].text.strip()
            open_rank = cols[5].text.strip()
            close_rank = cols[6].text.strip()

            model_instance = ModelClass(
                round_no='6',  # Assuming round number is constant for this example
                institute_type='Indian Institute of Technology',  # Adjust as per your requirement
                institute_name=institute_name,
                academic_program=academic_program,
                seat_type=seat_type,
                gender=gender,
                open_rank=open_rank,
                close_rank=close_rank
            )
            model_instance.save()
        # print(table.prettify())
        sleep(5)

    driver.quit()
    return HttpResponse("This view is only accessible by admins.")

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
        
class CRLAvailInstiView(APIView):
    def get(self, request):
        user_id = get_user_from_token(request)
        if isinstance(user_id, Response):  
            return user_id
        year = request.query_params.get('year')
        crl = request.query_params.get('crl')
        branch = request.query_params.get('branch')
        ModelClass = apps.get_model('users', 'josaa' + str(year))
        try:
            if branch=='All':
                results = ModelClass.objects.filter(close_rank__gte=crl, seat_type='OPEN').order_by('open_rank')
            else :
                results = ModelClass.objects.filter(close_rank__gte=crl, academic_program = branch, seat_type='OPEN').order_by('open_rank')
            results_data = list(results.values())
            if len(results_data)==0:
                return Response({'message': 'Sorry no institutes are available for this rank and branch.'}, status=404)
            return JsonResponse(results_data, safe=False)
            
        except ModelClass.DoesNotExist:
            return Response({'error': 'Sorry no institutes are available for this rank and branch.'}, status=404)
        except Exception as e:
            return HttpResponse(f'An error occurred: {e}', status=500)
        
class CatAvailInstiView(APIView):
    def get(self, request):
        user_id = get_user_from_token(request)
        if isinstance(user_id, Response):  
            return user_id
        year = request.query_params.get('year')
        category = request.query_params.get('category')
        cat_rank = request.query_params.get('category_rank')
        branch = request.query_params.get('branch')
        ModelClass = apps.get_model('users', 'josaa' + str(year))
        try:
            if branch == 'ALL':
                if category == 'ALL':
                    results = ModelClass.objects.annotate(
                        close_rank_int=Cast('close_rank', IntegerField())
                    ).filter(
                        close_rank_int__gte=cat_rank
                    ).order_by('open_rank')
                else:
                    results = ModelClass.objects.annotate(
                        close_rank_int=Cast('close_rank', IntegerField())
                    ).filter(
                        close_rank_int__gte=cat_rank,
                        seat_type=category
                    ).order_by('open_rank')
            else:
                if category == 'ALL':
                    results = ModelClass.objects.annotate(
                        close_rank_int=Cast('close_rank', IntegerField())
                    ).filter(
                        close_rank_int__gte=cat_rank,
                        academic_program=branch
                    ).order_by('open_rank')
                else:
                    results = ModelClass.objects.annotate(
                        close_rank_int=Cast('close_rank', IntegerField())
                    ).filter(
                        close_rank_int__gte=cat_rank,
                        seat_type=category,
                        academic_program=branch
                    ).order_by('open_rank')
            results_data = list(results.values())
            if len(results_data)==0:
                return Response({'message': 'Sorry no institutes are available for this rank and branch.'}, status=404)
            return JsonResponse(results_data, safe=False)
            
        except ModelClass.DoesNotExist:
            return Response({'error': 'Sorry no institutes are available for this rank and branch.'}, status=404)
        except Exception as e:
            return HttpResponse(f'An error occurred: {e}', status=500)
        
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
        
class TopBranchesYearWise(APIView):
    def get(self, request):
        year = request.query_params.get('year')
        ModelClass = apps.get_model('users', 'josaa' + str(year))
        try:
            if year == '2016' or year=='2017':
                gender = 'NA'
            else:
                gender = 'Gender-Neutral'
            results = ModelClass.objects.filter(
            seat_type='OPEN', gender=gender
            ).annotate(
                open_rank_int=Cast('open_rank', FloatField()),
                close_rank_int=Cast('close_rank', FloatField())
            ).annotate(
            avg_rank=ExpressionWrapper((F('open_rank_int') + F('close_rank_int')) / 2, output_field=FloatField())
            ).values('academic_program').annotate(
                avg_of_avg_rank=Avg('avg_rank'),
                institute_count=Count('institute_name')
            ).order_by('avg_of_avg_rank')
            # results3 = results.values()
            results_data = list(results)
            return JsonResponse(results_data, safe=False)
        except Exception as e:
            return HttpResponse(f'An error occurred: {e}', status=500)
        
class YearlyTrend(APIView):
    def get(self, request):

        institute = request.query_params.get('institute')
        category = request.query_params.get('category')     
        branch = request.query_params.get('branch')
        # gender = request.query_params.get('gender')
        yearly_trends = []
        try:
            for i in range(2016, 2024):
                ModelClass = apps.get_model('users', 'josaa' + str(i))
                if i==2016 or i==2017:
                    gender = 'NA'
                else:
                    gender = 'Gender-Neutral'
                # print(f'Querying model: josaa{i}')
                results = ModelClass.objects.filter(
                        seat_type = category,
                        academic_program = branch,
                        gender = gender,
                        institute_name = institute
                    ).values('close_rank', 'open_rank')
                # print(f'Raw query: {results.query}')
                # print(results)
                open_data = list(results.values('open_rank'))
                close_data = list(results.values('close_rank'))
                if len(open_data)>0 :
                    year_data = {'year':i, 'close_rank':close_data[0], 'open_rank':open_data[0]}
                    yearly_trends.append(year_data)
                print(yearly_trends)
            return JsonResponse(yearly_trends, safe=False)
        except Exception as e:
            return HttpResponse(f'An error occurred: {e}', status=500)
        
class Branches(APIView):
    def get(self, request):
        try:
            result = josaa2023.objects.values('academic_program').distinct()
            results_data = list(result)
            return JsonResponse(results_data, safe=False)
        except Exception as e:
            return HttpResponse(f'An error occured: {e}', status=500)

def generate_jwt_token(user):
    payload = {
        'user_id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24),
        'iat': datetime.datetime.utcnow()
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    return token