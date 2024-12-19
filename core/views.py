from django.shortcuts import render
from django.views.generic import TemplateView, ListView

# Create your views here.
from .models import BlogPost


from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.conf import settings
from .models import SEOSettings



from .models import BlogPost, Slider, AboutUs, FAQ, Banner, ProjectsSection, ServicesSection

class Home(TemplateView):
    template_name = 'base/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Fetch SEO settings (use default language 'en' if not found)
        seo_settings = SEOSettings.objects.first()  # You could also query by language if needed
        if seo_settings:
            context['seo_settings'] = seo_settings
        else:
            context['seo_settings'] = None  # Or some default fallback

        # Other context data
        context['latest_blogs'] = BlogPost.objects.order_by('-created_at')[:3]
        context['sliders'] = Slider.objects.all()
        context['about_us'] = AboutUs.objects.first()  # Assuming you only have one "About Us" entry
        context['faqs'] = FAQ.objects.all()  # Get all FAQs
        context['banner'] = Banner.objects.first()  # Assuming a single banner
        context['projects_section'] = ProjectsSection.objects.prefetch_related('tabs').first()
        context['services_section'] = ServicesSection.objects.prefetch_related('categories__items').first()
        
        return context

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Collect cleaned data from the form
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Send the email to your Google Workspace email
            send_mail(
                f"Message from {username} - {subject}",  # Subject line
                message,  # Message body
                email,  # From email
                [settings.EMAIL_HOST_USER],  # To email (your Google Workspace email)
                fail_silently=False,  # Set to True to suppress errors
            )

            # Redirect to a thank you page or show a success message
            return HttpResponseRedirect('/thank-you/')

    else:
        form = ContactForm()

    return render(request, 'pages/contact.html', {'form': form})


#
# from .models import BlogPost, Slider




class About(TemplateView):
    template_name = 'pages/about.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about_us'] = AboutUs.objects.first()  # Assuming you only have one "About Us" entry
        context['faqs'] = FAQ.objects.all()  # Get all FAQs
        context['banner'] = Banner.objects.first()  # Assuming a single banner
        context['projects_section'] = ProjectsSection.objects.prefetch_related('tabs').first()
        return context


from django.views.generic import TemplateView
from .models import TeamMember  # Import the TeamMember model


class TeamMemberView(TemplateView):
    template_name = 'pages/team.html'  # Set the template to use

    def get_context_data(self, **kwargs):
        # Get the default context data
        context = super().get_context_data(**kwargs)

        # Add team members to the context
        context['team_members'] = TeamMember.objects.all()  # Fetch all team members

        return context

class Testimonial(TemplateView):
    template_name = 'pages/testimonial.html'


class Services(TemplateView):
    template_name = 'pages/services.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['faqs'] = FAQ.objects.all()  # Get all FAQs
        context['banner'] = Banner.objects.first()  # Assuming a single banner
        context['services_section'] = ServicesSection.objects.prefetch_related('categories__items').first()
        return context



from django.views.generic import ListView
from .models import BlogPost

from django.views.generic import ListView
from django.db.models import Q
from .models import BlogPost


class BlogList(ListView):
    model = BlogPost
    template_name = 'pages/blog.html'
    context_object_name = 'blogs'
    queryset = BlogPost.objects.all().order_by('-created_at')  # Order by newest first

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search', '')  # Capture the search query

        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(content__icontains=search_query)
            )

        return queryset





class Contact(TemplateView):
    template_name = 'pages/contact.html'


from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from .models import BlogPost


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'page/blog_detail.html'
    context_object_name = 'blog'

    def get_object(self):
        # Override to fetch blog by slug
        return get_object_or_404(BlogPost, slug=self.kwargs['slug'])


