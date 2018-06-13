# accounts urls

from django.conf.urls import url
from accounts.views import login, register, logout, profile



urlpatterns = [
    url(r'^login$',    login,      name='login'),
    url(r'^register$', register,   name='register'),
    url(r'^logout$',   logout,     name='logout'),
    url(r'^profile$',  profile,    name='profile'),
]
