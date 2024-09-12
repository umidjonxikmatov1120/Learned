from django.db import models
from django.utils.text import slugify


class CategoryModel(models.Model):  # Frontend, Backend, Ingliz tili ...
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

class SubjectModel(models.Model):  # JS, Python, Java, Elementary, Beginner ...
    title = models.CharField(max_length=100)
    image = models.ImageField()
    service_id = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'subject'
        verbose_name_plural = 'subjects'


class VideoModel(models.Model):
    title = models.CharField(max_length=255)
    video = models.URLField()
    subject_id = models.ForeignKey(SubjectModel, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'video'
        verbose_name_plural = 'videos'

class BlogModel(models.Model):
    full_name = models.CharField(max_length=100)
    image = models.ImageField()
    programming_lang = models.CharField(max_length=100)
    long_description = models.TextField()

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'


class ContactModel(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.CharField(max_length=255)
    details = models.TextField()

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'

