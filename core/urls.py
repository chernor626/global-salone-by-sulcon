from django.urls import path

from .views import Home, About, Services, BlogDetailView, Contact, BlogList, TeamMember, Testimonial, TeamMemberView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", Home.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('services/', Services.as_view(), name='services'),
    path('contact/', Contact.as_view(), name='contact'),
    path("team/", TeamMemberView.as_view(), name='team'),

    path("testimonial/", Testimonial.as_view(), name='testimonial'),

    path('blog/',BlogList.as_view(), name='blog_list' ),
    path('blog/<slug:slug>/', BlogDetailView.as_view(), name='blog_detail'),

]





# Serve media files in development (only for local development)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
