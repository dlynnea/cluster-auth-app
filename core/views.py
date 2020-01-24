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
from .models import Headline
from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage

from .forms import BookForm
from .models import Book

class Home(TemplateView):
    template_name = 'home.html'

def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'upload.html', context)

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {
        'books': books
    })

def upload_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'upload_book.html', {
        'form': form
    })

def delete_book(request, pk):
    if request.method == 'POST':
        book = Book.objects.get(pk=pk)
        book.delete()
    return redirect('book_list')

## india times
toi_r = requests.get("https://timesofindia.indiatimes.com/briefs")
toi_soup = BeautifulSoup(toi_r.content, 'html.parser')

toi_headings = toi_soup.find_all('h2')
toi_headings = toi_headings[0:-13] #this removes the footers
# print(toi_headings)
toi_news = []

for th in toi_headings:
    toi_news.append(th.text)

#nyb




def index(request):
    context = {'toi_news':toi_news}
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

# def news_list(request):
#     headlines = Headline.objects.all()
#     context = {
#         'object_list': headlines,
#     }
#     return render(request, 'home.html', context)

# def scrape(request):
#     session = requests.Session()
#     session.headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:12.0) Gecko/20100101 Firefox/12.0. Your User Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0. 1132.27 Safari/536.11."}
    
#     url = 'https://www.nytimes.com/column/bits'

#     content = session.get(url, verify=False).content

#     # content = requests.get("https://www.nytimes.com/column/bits")
#     nyb_soup = BeautifulSoup(content, 'html.parser')

#     posts = nyb_soup.find_all('div', {'class':'css-1l4spti'})

#     for i in posts:
#         link = i.find_all('a', {'href': True})[0]
#         title = i.find('h2', {'class':'css-1j9dxys'}).text

#         new_headline = Headline()
#         new_headline.title = title
#         new_headline.url = link
#         new_headline.save()

#     return redirect('/home/')



# ny bits
# url = "https://www.nytimes.com/column/bits"
# content = requests.get(url)
# soup = BeautifulSoup(content, 'html.parser')
# for div in soup.find_all('div', {'class':'css-1l4spti'}):
#     link = i.find_all('a', {'href': True})[0]
#     title = i.find('h2', {'class':'css-1j9dxys'}).text
#     for h in link:
#         href = link.get('href')

# nyb_news = []

# for nth in posts:
#     nyb_news.append(title)
#     nyb_news.append(link)


nyb_r = requests.get("https://www.nytimes.com/column/bits")
nyb_soup = BeautifulSoup(nyb_r.content, 'html.parser')

posts = nyb_soup.find_all('div', {'class':'css-1l4spti'})

for i in posts:
    link = i.find_all('a', {'href': True})[0]
    title = i.find('h2', {'class':'css-1j9dxys'}).text

nyb_news = []

for i in posts:
    nyb_news.append(title)
    nyb_news.append(link)







# @login_required
# def secret_page(request):
#     return render(request, 'secret_page.html')

# class SecretPage(LoginRequiredMixin, TemplateView):
#     template_name = 'secret_page.html'

# def index(request):
#     context = {'toi_news':toi_news}
#     return render(request, 'home.html', context)