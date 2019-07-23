from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from myproject import views
urlpattern=[url(r'admin/',admin.site.urls),
            url(r'Officer',views.employeeList.as_view() )]
#Call on web page by writing localhost8000/Officer