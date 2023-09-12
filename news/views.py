from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView, ListView


def home_news(request):
    # news = Articles.objects.all()
    news = Articles.objects.order_by('-date')
    return render(request, 'news/home_news.html', {'news': news})


def create(request):
    error = ''
    if request.method == "POST":
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home_news")
        else:
            error = "НЕПРАВИЛЬНАЯ ФОРМА"
    form = ArticlesForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, "news/create.html", data)


def detail_view(request):
    return render(request, 'news/detail_view.html', {'detail_view': detail_view})


class NewsDetailView(DetailView):
    model = Articles
    template_name = "news/detail_view.html"
    context_object_name = 'article'


class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'
    form_class = ArticlesForm


class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news/'
    template_name = 'news/news-delete.html'
    context_object_name = 'article'


class NewsListView(ListView):
    model = Articles
    queryset = Articles.objects.all()
    context_object_name = "news_list"
    template_name = "news/list-view.html"
