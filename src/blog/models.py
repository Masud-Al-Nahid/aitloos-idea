from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify
from django.utils.crypto import get_random_string

# Create your models here.
class Categories(models.Model):
    title = models.CharField(max_length=200, unique=True, blank=False, null=False, help_text='Title of the category', verbose_name='Title')
    slug = models.SlugField(unique=True, blank=True, null=True, help_text='Slug of the category')

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            while BlogPost.objects.filter(slug=self.slug).exists():
                self.slug = f'{slugify(self.title)}-{get_random_string(length=4)}'
        super().save(*args, **kwargs)

    
class BlogPost(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
        ('edit', 'Edit'),
    )
    title = models.CharField(max_length=200, unique=True, blank=False, null=False, help_text='Title of the post', verbose_name='Title')
    slug = models.SlugField(unique=True, blank=True, null=True, help_text='Slug of the post', editable=True, db_index=True )
    content = RichTextUploadingField()
    featured_image = models.ImageField(upload_to='blog/', blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    mod_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            while BlogPost.objects.filter(slug=self.slug).exists():
                self.slug = f'{slugify(self.title)}-{get_random_string(length=4)}'
        super().save(*args, **kwargs)

    # class Meta:
    #     verbose_name_plural = 'blog posts'
    # this is class name changer method or functions

    
