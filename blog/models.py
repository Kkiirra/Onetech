from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField


class Blog(models.Model):
    title = models.CharField(max_length=225)
    slug = models.SlugField(max_length=255, blank=True, null=True)
    preview_title = models.CharField(max_length=60, blank=True, null=True)
    head = RichTextField()
    date = models.DateTimeField(blank=True, null=True)
    body = RichTextField()
    preview_photo = models.ImageField(upload_to='media/')

    def get_absolute_url(self):
        return reverse('blog:single_blog', args=[self.slug])

    def __str__(self):
        return self.title


class Quote(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="blogs")
    quote_text = models.TextField()
    quote_author = models.CharField(max_length=255)

    def __str__(self):
        return self.quote_author
