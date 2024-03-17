from rest_framework.decorators import api_view
from rest_framework.response import Response 

@api_view(['GET'])
def endpoint(request):
    data = ['/advocates', 'advocates/:username']
    return Response(data)

@api_view(['GET'])
def advocate_list(request):
    data = ['Mahi', 'Kumar', 'Raju']
    return Response(data)

@api_view(['GET'])
def advocate_details(request, username):
    data = username
    return Response(data)