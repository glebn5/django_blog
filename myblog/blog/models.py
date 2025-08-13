from django.db import models
from django.utils.text import slugify

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(verbose_name='URL', unique=True, db_index=True, max_length=255)

    def __str__(self):
        return self.title
    
    def content_for_admin(self):
        return f'{self.content[:50]}...'
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'posts'
        ordering = ['-created_at']
        unique_together = ['title']
        