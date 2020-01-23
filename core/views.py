from django.shortcuts import render, redirect
# auth imports
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
# scraping imports
import requests
from bs4 import BeautifulSoup


## india times
toi_r = requests.get("https://timesofindia.indiatimes.com/briefs")
toi_soup = BeautifulSoup(toi_r.content, 'html.parser')

toi_headings = toi_soup.find_all('h2')
toi_headings = toi_headings[0:-13] #this removes the footers
# print(toi_headings)
toi_news = []

for th in toi_headings:
    toi_news.append(th.text)

## ny bits
nyb_r = requests.get("https://www.nytimes.com/column/bits")
nyb_soup = BeautifulSoup(nyb_r.content, 'html.parser')

posts = nyb_soup.find_all('div', {'class':'css-1l4spti'})

for i in posts:
        link = i.find_all('a', {'href': True})[0]
        title = i.find('h2', {'class':'css-1j9dxys'}).text

nyb_news = []

for nth in posts:
    nyb_news.append(title)
    nyb_news.append(link)

def home(request):
    context = {'toi_news':toi_news, 'nyb_news':nyb_news}
    return render(request, 'home.html', context)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })

# @login_required
# def secret_page(request):
#     return render(request, 'secret_page.html')

# class SecretPage(LoginRequiredMixin, TemplateView):
#     template_name = 'secret_page.html'

# def index(request):
#     context = {'toi_news':toi_news}
#     return render(request, 'home.html', context)