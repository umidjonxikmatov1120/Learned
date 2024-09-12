from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404

from core import settings
from learn.forms import ContactModelForm
from learn.models import SubjectModel, BlogModel, VideoModel, CategoryModel


def home_page_view(request):
    if request.method == "POST":
        form = ContactModelForm(request.POST)
        if form.is_valid():
            sending = form.save()

            subject = 'New Sending Message'
            message = (
                f'First_name : {sending.first_name}\n'
                f'Last_name : {sending.last_name}\n'
                f'Email : {sending.email}\n'
                f'Message : {sending.message}\n'
                f'Detail : {sending.details}\n'
            )

            recipient_list = [settings.EMAIL_RECIPIENT_LIST]
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)

            return redirect("home_page")

        else:
            print('Form is not valid')
            print(form)

    else:
        form = ContactModelForm()

    blogs = BlogModel.objects.all()
    categories = CategoryModel.objects.all()

    context = {
        "blogs": blogs,
        "form": form,
        "categories": categories,
    }

    return render(request, 'index.html', context=context)


def category_page_view(request, slug):
    # videos = VideoModel.objects.all()
    category = CategoryModel.objects.get(slug=slug)
    # Filter subjects based on the category's service_id
    subjects = SubjectModel.objects.filter(service_id=category.id)

    cats = CategoryModel.objects.all()
    context = {
        # "videos": videos,
        "category": category,
        "subjects": subjects,
        "categories": cats,
    }
    return render(request, 'course.html', context=context)


def course_page_view(request):
    categories = CategoryModel.objects.all()
    context = {
        "categories": categories,
    }
    return render(request, 'gate.html', context=context)


def view_page_view(request, pk):
    subject_detail = get_object_or_404(SubjectModel, pk=pk)
    cat = CategoryModel.objects.all()
    related_products = SubjectModel.objects.all()[:4]
    context = {
        "categories": cat,
        "subject_detail": subject_detail,
        "related_products": related_products,
    }
    return render(request, 'view.html', context=context)


