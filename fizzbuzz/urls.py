from django.contrib import admin
from django.urls import path
from fizzbuzz.api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin', admin.site.urls),
    path('fizzbuzz', views.fizzbuzz_list, name='fizzbuzz-list-create'),
    path('fizzbuzz/<int:id>', views.fizzbuzz_detail, name='fizzbuzz-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
