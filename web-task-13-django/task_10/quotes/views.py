from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from .models import Author, Quote, Tag

from .forms import AuthorForm, QuoteForm, TagForm
from .utils import get_mongodb
# Create your views here.


def main(request, page=1):
    quotes = Quote.objects.all()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, 'quotes/index.html', context={'quotes': quotes_on_page})


def show_author(request, id_):
    author = Author.objects.get(id=id_)
    return render(request, 'quotes/author.html', context={'author': author})


def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='/')
        else:
            return render(request, 'quotes/add_author.html', {'form': form})

    return render(request, 'quotes/add_author.html', {'form': AuthorForm()})


def add_quote(request):
    authors = Author.objects.all()
    tags = Tag.objects.all()
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            new_quote = form.save()
            choice_tags = Tag.objects.filter(name__in=request.POST.getlist('tags'))
            for tag in choice_tags.iterator():
                new_quote.tags.add(tag)
            return redirect(to='/')
        else:
            return render(request, 'quotes/add_quote.html', {'authors': authors, 'form': form, 'tags': tags})

    return render(request, 'quotes/add_quote.html', context={'authors': authors, 'form': QuoteForm(), 'tags': tags})


def add_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='/')
        else:
            return render(request, 'quotes/add_tag.html', {'form': form})

    return render(request, 'quotes/add_tag.html', {'form': TagForm()})

