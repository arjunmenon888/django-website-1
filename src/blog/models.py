from django.db import models
from django.db.models.signals import post_delete, pre_save
from django.utils.text import slugify
from django.conf import settings
from django.dispatch import receiver    


def upload_locations(instance, filename):
    file_path = "blog/{author_id}/{title}-{filename}".format(author_id=str(instance.author_id), title=str(instance.title), filename=filename)
    return file_path

class BlogPost(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    body = models.TextField(null=False, blank=False)
    image = models.ImageField(upload_to=upload_locations)
    date_published = models.DateTimeField(auto_now_add=True, verbose_name='date_published')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='date_updated')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.title

@receiver(post_delete, sender=BlogPost)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)

def pre_save_blog_post_receiver(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.author.username +'-'+ instance.title)

pre_save.connect(pre_save_blog_post_receiver, sender=BlogPost)

