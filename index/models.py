from django import forms
from django.db import models
from django.utils.text import slugify

MEDIA_TYPE_CHOICES = [
    ('image', 'Image'),
    ('video', 'Video'),
    ('pdf', 'PDF'),
    ('archive', 'ZIP'),
]

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=32)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'



class Project(models.Model):
    project_name = models.CharField(max_length=128)
    slug = models.SlugField(unique=True, blank=True)
    project_description = models.TextField()
    project_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    project_image = models.ImageField(upload_to='projects/images/', null=True, blank=True)
    project_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    is_visible = models.BooleanField(default=True)
    added_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.project_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.project_name
