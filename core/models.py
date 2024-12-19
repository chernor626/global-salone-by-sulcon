from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone




class SEOSettings(models.Model):
    # Meta tags
    keywords = models.TextField(default="real estate Sierra Leone, top realtors in Sierra Leone, luxury homes Freetown, land for sale Sierra Leone, beachfront properties Sierra Leone, commercial real estate Freetown, rent homes Sierra Leone, property investment Sierra Leone, trusted real estate agency, affordable housing Sierra Leone, buy property Freetown")
    description = models.TextField(default="Global Salone is your trusted global partner for premium real estate services in Sierra Leone. Whether you're buying, selling, or renting luxury homes, commercial spaces, or land, we deliver unparalleled expertise to help you secure your dream property. Start your property journey today.")
    author = models.CharField(max_length=255, default="Global Salone Real Estate")
    language = models.CharField(max_length=50, default="en")
    
    # Structured Data (JSON)
    schema_json = models.JSONField(default=dict)  # For structured data like Schema.org

    # Open Graph / Twitter metadata
    og_title = models.CharField(max_length=255, default="Global Salone | Real Estate in Sierra Leone")
    og_description = models.TextField(default="Searching for top-tier real estate services in Sierra Leone? Global Salone offers luxury homes, beachfront estates, commercial spaces, and land investment opportunities. With expertise in property buying, selling, and renting, we help you find your dream property today.")
    og_image = models.URLField(default="https://globalsalone.com/images/featured-property.jpg")  # URL to the featured image
    twitter_title = models.CharField(max_length=255, default="Global Salone | Real Estate in Sierra Leone")
    twitter_description = models.TextField(default="Discover the finest real estate in Sierra Leone with Global Salone. From luxury homes to beachfront estates, we offer premium properties for sale and rent. Start your global property journey today.")
    twitter_image = models.URLField(default="https://globalsalone.com/images/featured-property.jpg")
    
    # Canonical URL
    canonical_url = models.URLField(default="https://globalsalone.com/")
    
    def __str__(self):
        return f"SEO Settings for {self.language} language"


# Slider Model
class Slider(models.Model):
    image = models.ImageField(upload_to='slider_images/')
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    description = models.TextField()
    video_link = models.URLField(blank=True, null=True)
    learn_more_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title



class Banner(models.Model):
    background_image = models.ImageField(upload_to='banner_images/')
    title = models.CharField(max_length=255)
    subtitle = models.TextField()
    button_text = models.CharField(max_length=50, blank=True, null=True)
    button_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title



from django.db import models

class ProjectsSection(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class ProjectTab(models.Model):
    section = models.ForeignKey(ProjectsSection, on_delete=models.CASCADE, related_name="tabs")
    icon = models.CharField(max_length=50, help_text="Enter FontAwesome icon class, e.g., 'fas fa-bolt'")
    tab_title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='project_images/', help_text="Upload an image for the project tab")
    content_title = models.CharField(max_length=255)
    content_description = models.TextField()
    button_text = models.CharField(max_length=50, blank=True, null=True)
    button_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.tab_title} ({self.section.title})"



from django.db import models

class ServicesSection(models.Model):
    title = models.CharField(max_length=255, default="Our Services")
    subtitle = models.CharField(max_length=255, default="The Best Service For You")
    description = models.TextField()

    def __str__(self):
        return self.title


class ServiceCategory(models.Model):
    section = models.ForeignKey(ServicesSection, on_delete=models.CASCADE, related_name="categories")
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class ServiceItem(models.Model):
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, related_name="items")
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="services/")
    description = models.TextField()
    button_text = models.CharField(max_length=50, default="Read More")
    button_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

# About Us Model
class AboutUs(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    description = models.TextField()
    highlight_1 = models.CharField(max_length=255)
    highlight_2 = models.CharField(max_length=255)
    highlight_3 = models.CharField(max_length=255)
    image_main = models.ImageField(upload_to='about_images/')
    experience_years = models.PositiveIntegerField(default=0)  # Default set to 0
    experience_text = models.CharField(max_length=100, default="years of experience")
    image_secondary = models.ImageField(upload_to='about_images/')

    def __str__(self):
        return self.title


# Blog Category Model
class Category(models.Model):
    """Blog category model"""
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# Blog Post Model
class BlogPost(models.Model):
    """Blog post model"""
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    short_description = models.TextField(blank=True, null=True)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_detail', args=[self.slug])


# Contact Us Model
class ContactUs(models.Model):
    """Contact us model"""
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# Team Member Model
class TeamMember(models.Model):
    """Team member model"""
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    image = models.ImageField(upload_to='team_images')
    description = models.TextField()
    linkedin_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


# FAQ Model
class FAQ(models.Model):
    question = models.CharField(max_length=500)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set timestamp

    def __str__(self):
        return self.question


# Testimonial Model
class Testimonial(models.Model):
    """Testimonial model"""
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    testimonial = models.TextField()
    image = models.ImageField(upload_to='testimonial_images')

    def __str__(self):
        return self.name


# Service Model
class Service(models.Model):
    """Service model"""
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='service_images')
    description = models.TextField()

    def __str__(self):
        return self.name