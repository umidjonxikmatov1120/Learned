from django.contrib import admin

from learn.models import SubjectModel, BlogModel, VideoModel, ContactModel, CategoryModel

admin.site.register(SubjectModel)
admin.site.register(BlogModel)
admin.site.register(VideoModel)
admin.site.register(ContactModel)
admin.site.register(CategoryModel)
