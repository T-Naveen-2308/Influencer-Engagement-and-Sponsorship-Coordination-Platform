from rest_framework import serializers
from .models import Person, Admin, Sponsor, Influencer, Campaign, Message, ADRequest

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'

class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = '__all__'

class InfluencerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Influencer
        fields = '__all__'

class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class ADRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ADRequest
        fields = '__all__'

