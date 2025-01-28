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
from local_apps.message_utility.uitility import async_send_mail
# Create your views here.

class BlogListView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

# View to retrieve a single blog
class BlogDetailView(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'pk'  # Maps to the 'id' field in the model

# View to create a new blog
class BlogCreateView(generics.CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

# View to update a blog
class BlogUpdateView(generics.UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'pk'  # or 'pk'

# View to delete a blog
class BlogDeleteView(generics.DestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'pk'  # or 'pk'




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

        # Prepare data for emails
        context_data = {
            'user_name': contact_form.name or "Valued Customer",
            'appointment_time': f'{contact_form.date} {contact_form.time}',
            'service': contact_form.service or "Not specified",
            'phone': contact_form.phone or "Not provided",
            'message': contact_form.message or "No message provided",
        }

        # Email to the visitor
        async_send_mail(
            subject="Appointment Confirmation",
            template="message_utility/appointment_confirmation.html",
            context=context_data,
            recipient_list=[contact_form.email],
        )

        # Email to the hospital team
        async_send_mail(
            subject="New Appointment Scheduled",
            template="message_utility/hospital_appointment_details.html",
            context=context_data,
            recipient_list=['pettrusthospital@gmail.com'],  # Replace with actual email
        )

        # Email to the backend team
        async_send_mail(
            subject="Lead Collection Report",
            template="message_utility/leads_data.html",
            context=context_data,
            recipient_list=['pettrustmarketing@gmail.com'],  # Replace with actual email
        )

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        # Add a custom message to the response
        response.data = {
              "message": "Kindly wait for confirmation. Our team will contact you shortly. Thank you for choosing us. - Pet Trust Team",
            "appointment_details": response.data,
        }
        return Response(response.data, status=status.HTTP_201_CREATED)
    


class GetinTouchFormView(generics.CreateAPIView):
        queryset = GetinTouch.objects.all()
        serializer_class = GetinTouchSerializer

        def create(self, request, *args, **kwargs):
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(
            {"message": "Your message has been submitted successfully!"},
            status=status.HTTP_201_CREATED
        )