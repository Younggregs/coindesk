from django.conf.urls import url, include
from django.contrib import admin

from graphene_django.views import GraphQLView

from .schema import schema

urlpatterns = [
    url(r'^', include('challenge.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^graphiql/', GraphQLView.as_view(graphiql=True, schema=schema)),
]