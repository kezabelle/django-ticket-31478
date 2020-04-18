from django.template.response import TemplateResponse
from django.urls import path


def example(request, template):
    return TemplateResponse(
        request=request,
        template=template,
        context={}
    )

urlpatterns = [
    path("problem", example, kwargs={'template': "subtemplate.html"}),
    path("fine", example, kwargs={'template': "base.html"}),
]
