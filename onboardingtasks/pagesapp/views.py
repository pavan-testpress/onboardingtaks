from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import PagesForm
from .models import Pages


class HomePageView(TemplateView):
    template_name = 'pagesapp/home.html'

    def get(self, request):
        data = Pages.objects.all().order_by('ordering', '-modified')
        form = PagesForm()
        return render(request, self.template_name, {'form': form, 'data': data})

    def post(self, request):
        data = Pages.objects.all().order_by('ordering', '-modified')
        form = PagesForm(request.POST)
        if form.is_valid:
            form.save()
        form = PagesForm()
        return render(request, self.template_name, {'form': form, 'data': data})


class NavPageView(TemplateView):
    template_name = 'pagesapp/navpages.html'

    def get(self, request):
        pat = request.path.split('/')[2]
        h = Pages.objects.get(slug=pat)
        html = h.content_html
        title = h.title
        data = Pages.objects.all().order_by('ordering', '-modified')
        return render(request, self.template_name, {'data': data, 'html': html, 'title': title})
