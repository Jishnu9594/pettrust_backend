from django.shortcuts import render
from .models import*
from .serializers import*
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import ContactForm
from .serializers import ContactFormSerializer
from local_apps.message_utility.views import mail_handler
# Create your views here.

class BlogListView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

# View to retrieve a single blog
class BlogDetailView(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'id'  # or you can use 'pk' if you prefer

# View to create a new blog
class BlogCreateView(generics.CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

# View to update a blog
class BlogUpdateView(generics.UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'id'  # or 'pk'

# View to delete a blog
class BlogDeleteView(generics.DestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'id'  # or 'pk'




# List all Testimonials
class TestimonialListView(generics.ListAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer


# Create a new Testimonial
class TestimonialCreateView(generics.CreateAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer


# Retrieve a single Testimonial by ID
class TestimonialRetrieveView(generics.RetrieveAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer


# Update an existing Testimonial
class TestimonialUpdateView(generics.UpdateAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer


# Delete a Testimonial
class TestimonialDeleteView(generics.DestroyAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer




class ContactFormCreateView(generics.CreateAPIView):
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer

    def perform_create(self, serializer):
        # Save the contact form data
        contact_form = serializer.save()

        # Prepare the data for the emails
        context_data = {
            'user_name': contact_form.name,
            'appointment_time': f'{contact_form.date} {contact_form.time}',
            'service': contact_form.service,
            'phone': contact_form.phone,
            'message': contact_form.message
        }

        # Send an appointment confirmation to the visitor (single email)
        mail_handler(
            mail_type='single',
            to=[contact_form.email],  # Visitor's email
            subject="Appointment Confirmation",
            data=context_data,
            template="message_utility/appointment_confirmation.html",
        )

        # Send hospital confirmation details (single email)
        mail_handler(
            mail_type='single',
            to=['jishnuaswin025@gmail.com'],  # Hospital team email
            subject="New Appointment Scheduled",
            data=context_data,
            template="message_utility/hospital_appointment_details.html",
        )

        # Send lead collection report to backend team (multiple emails)
        mail_handler(
            mail_type='single',
            to=['jishnuunnikrishnanp@gmail.com'],  # Backend team emails
            subject="Lead Collection Report",
            data=context_data,
            template="message_utility/leads_data.html",
        )

        return contact_form

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data = {"message": "Appointment successfully scheduled!"}
        return response
