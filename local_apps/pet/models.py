from django.db import models
from local_apps.main.models import Main

# Create your models here.

class ContactForm(Main):
    name = models.CharField(max_length=255,blank=True,null=True)
    phone = models.CharField(max_length=20,blank=True,null=True)
    service = models.CharField(max_length=255,blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField(blank=True,null=True)

    class Meta:
        ordering = ["-created_at", "-updated_at"]
        verbose_name = 'ContactForm'
        verbose_name_plural = 'ContactForms'

    def __str__(self):
        return self.name
    



class Testimonial(Main):
    name = models.CharField(max_length=100,blank=True,null=True)
    title = models.CharField(max_length=100,blank=True,null=True)
    message = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to='testimonials/', null=True, blank=True)

    class Meta:
        ordering = ["-created_at", "-updated_at"]
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'

    def __str__(self):
        return self.name


class Blog(Main):
    title = models.CharField(max_length=255,blank=True,null=True)
    content = models.TextField(blank=True,null=True)
    category = models.CharField(max_length=100,blank=True,null=True)
    date = models.DateField()
    image = models.ImageField(upload_to='blogs/', null=True, blank=True)

    class Meta:
        ordering = ["-created_at", "-updated_at"]
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

    def __str__(self):
        return self.title

