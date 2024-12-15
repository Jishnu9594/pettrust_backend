from rest_framework import serializers
from .models import *



class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['title', 'category', 'date', 'image','content']



class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ['name', 'title', 'message', 'image','rating']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.image:
            # Provide the relative path to the image
            representation['image'] = instance.image.url  # This will return the full URL, adjust if needed
        return representation


class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactForm
        fields = ['name', 'phone', 'service', 'email', 'date', 'time', 'message']


class GetinTouchSerializer(serializers.ModelSerializer):
    class Meta:
        model = GetinTouch
        fields = ['name', 'email', 'subject', 'message']