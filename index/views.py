from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Project
from .forms import CustomUserCreationForm, FeedbackForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.conf import settings
import requests


# Create your views here.
def home_page(request):
    projects = Project.objects.all()
    categories = Category.objects.all()
    context = {
        'projects': projects,
        'categories': categories,
        'page': 'home',
    }
    return render(request, 'core/home.html', context)

def project_list(request):
    projects = Project.objects.filter(is_visible=True).order_by('-added_date')
    context = {'page': 'projects',
               'projects': projects}
    return render(request, 'projects/project_list.html', context)

def projects_category(request, pk):
    category = Category.objects.get(id=pk)
    projects = Project.objects.filter(project_category=category)
    context = {
        'category': category,
        'projects': projects,
        'page': 'projects',
    }
    return render(request, 'projects/project_category.html', context)


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'projects/project_detail.html', {'project': project})

def contact(request):
    context = {'page': 'contact'}
    return render(request, 'contact/contact_form.html', context)

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home_page')  # куда угодно после регистрации
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def send_telegram_message(text):
    url = f'https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage'
    payload = {
        'chat_id': settings.TELEGRAM_CHAT_ID,
        'text': text,
        'parse_mode': 'HTML',
    }
    requests.post(url, data=payload)

@login_required
def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            username = request.user.username
            email = request.user.email

            full_message = f'Новое сообщение от {username} ({email}):\n\n{message}'

            # Отправка в Telegram
            send_telegram_message(full_message)

            return render(request, 'contact/thank_you.html')  # Показываем страницу успеха
    else:
        form = FeedbackForm()
        
    context = {'page': 'feedback',
               'form': form}

    return render(request, 'contact/feedback.html', context)

def thank_you(request):
    return render(request, 'contact/thank_you.html')

def about(request):
    context = {'page': 'about'}
    return render(request, 'core/about.html', context)

def service(request):
    context = {'page': 'service'}
    return render(request, 'core/service.html', context)