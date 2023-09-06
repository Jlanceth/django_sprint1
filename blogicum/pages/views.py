from django.views.generic import TemplateView


class AboutView(TemplateView):
    template_name = 'pages/about.html'


def about(request):
    return AboutView.as_view()(request)


class RulesView(TemplateView):
    template_name = 'pages/rules.html'


def rules(request):
    return RulesView.as_view()(request)
