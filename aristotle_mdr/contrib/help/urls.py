from django.conf.urls import patterns, url
from aristotle_mdr.contrib.help import views, forms


urlpatterns = patterns(
    'aristotle_mdr.contrib.help.views',

    url(r'^concepts/(?P<app>[a-zA-Z_]+)/(?P<model>[a-zA-Z_]+)/?', views.ConceptHelpView.as_view(), name='concept_help'),
    url(r'^concepts/(?P<app>[a-zA-Z_]+)/?', views.ConceptAppHelpView.as_view(), name='concept_app_help'),
    url(r'^concepts/?', views.AllConceptHelpView.as_view(), name='help_concepts'),

    url(r'^page/(?P<slug>.+)?', views.HelpView.as_view(), name='help_page'),
    url(r'^/?', views.AllHelpView.as_view(), name='help_base'),
)
