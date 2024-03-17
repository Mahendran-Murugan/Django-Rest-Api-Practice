from django.shortcuts import redirect
from django.http import JsonResponse
from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response 
from django.db.models import Q
from .models import Advocate, TestSentiment
from .serializers import AdvocateSerializer, TestSentimentSerializer
from .sentiment import getAnalysis

@api_view(['GET'])
def endpoint(request):
    data = ['/advocates', 'advocates/:username', 'sentiment/']
    return Response(data)

@api_view(['GET','POST'])
def advocate_list(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query == None:
            query = ''
        advocates = Advocate.objects.filter(Q(username__icontains=query) | Q(bio__icontains = query))
        serializer = AdvocateSerializer(advocates, many = True)
        return JsonResponse(serializer.data)
    
    if request.method == 'POST':
        advocate = Advocate.objects.create(
            username  = request.data['username'],
            bio  = request.data['bio'],
        )
        serializer = AdvocateSerializer(advocate, many = False)
        return Response(serializer.data)
  
  
@api_view(['POST', 'GET'])
def sentiment_list(request):
    if request.method == 'POST':
        review = request.data['review']
        sentiment = getAnalysis(review)
        print("The sentiment is",sentiment)
        sentiment = TestSentiment.objects.create(
            review = review,
            sentiment = str(sentiment),
        )
        serializer = TestSentimentSerializer(sentiment, many = False)
        return Response(serializer.data)
    
    if request.method == 'GET':
        sentiment = TestSentiment.objects.all()
        serializer = TestSentimentSerializer(sentiment, many = True)
        return Response(serializer.data)    

    
  
class AdvocateDetail(APIView):
    
    def get_object(self, username):
        try:
            return Advocate.objects.get(username=username)
        except Advocate.DoesNotExist:
            raise Response("Advocate is Not exist")
    
    def get(self, request, username):
        advocate = self.get_object(username=username)
        serializer = AdvocateSerializer(advocate, many=False)
        return Response(serializer.data)
    
    def put(self, request, username):
        advocate = self.get_object(username=username)
        advocate.username = request.data['username']
        advocate.bio = request.data['bio']
        advocate.save()
        serializer = AdvocateSerializer(advocate, many=False)
        return Response(serializer.data)
    
    def delete(self, request, username):
        advocate = self.get_object(username=username)
        advocate.delete()
        return Response('User Deleted')

# @api_view(['GET','PUT','DELETE'])
# def advocate_details(request, username):
#     advocate = Advocate.objects.get(username = username)
#     if request.method == 'GET':
#         serializer = AdvocateSerializer(advocate, many = False)
#         return Response(serializer.data)
    
#     if request.method == 'PUT':
#         advocate.username = request.data['username']
#         advocate.bio = request.data['bio']
#         advocate.save()
        
#         serializer = AdvocateSerializer(advocate, many = False)
#         return Response(serializer.data)
    
#     if request.method == 'DELETE':
#         advocate.delete()
#         return Response('User Deleted')


