
from django.urls import path,include
from .views import *
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('blogs/', BlogListView.as_view(), name='blog-list'),
    path('blogs/<int:id>/', BlogDetailView.as_view(), name='blog-detail'),
    path('blogs/create/', BlogCreateView.as_view(), name='blog-create'),
    path('blogs/update/<int:id>/', BlogUpdateView.as_view(), name='blog-update'),
    path('blogs/delete/<int:id>/', BlogDeleteView.as_view(), name='blog-delete'),
     path('testimonials/', TestimonialListView.as_view(), name='testimonial-list'),
    path('testimonials/create/', TestimonialCreateView.as_view(), name='testimonial-create'),
    path('testimonials/<int:pk>/', TestimonialRetrieveView.as_view(), name='testimonial-retrieve'),
    path('testimonials/<int:pk>/update/', TestimonialUpdateView.as_view(), name='testimonial-update'),
    path('testimonials/<int:pk>/delete/', TestimonialDeleteView.as_view(), name='testimonial-delete'),
    path('contact-form/', ContactFormCreateView.as_view(), name='contact-form-create'),
    path('api/get-in-touch/',GetinTouchFormView.as_view(), name='get-in-touch'),

    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
