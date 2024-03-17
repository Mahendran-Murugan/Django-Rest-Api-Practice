from rest_framework.serializers import ModelSerializer
from .models import Advocate, TestSentiment

class AdvocateSerializer(ModelSerializer):
    class Meta:
        model = Advocate
        fields = '__all__'
        
class TestSentimentSerializer(ModelSerializer):
    class Meta:
        model = TestSentiment
        fields = '__all__'