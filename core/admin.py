from django.contrib import admin
from .models import (
    Slider,
    Category,
    BlogPost,
    ContactUs,
    TeamMember,
    FAQ,
    Testimonial,
    AboutUs

)
from django_summernote.admin import SummernoteModelAdmin



from .models import SEOSettings

@admin.register(SEOSettings)
class SEOSettingsAdmin(admin.ModelAdmin):
    list_display = ('language', 'keywords', 'description')
    search_fields = ['language']
    list_filter = ['language']



from .models import Banner

admin.site.register(Banner)



from .models import ServicesSection, ServiceCategory, ServiceItem

class ServiceItemInline(admin.StackedInline):
    model = ServiceItem
    extra = 1


class ServiceCategoryAdmin(admin.ModelAdmin):
    inlines = [ServiceItemInline]
    list_display = ["title", "section"]


class ServicesSectionAdmin(admin.ModelAdmin):
    list_display = ["title", "subtitle", "description"]

admin.site.register(ServicesSection, ServicesSectionAdmin)
admin.site.register(ServiceCategory, ServiceCategoryAdmin)

from .models import ProjectsSection, ProjectTab

class ProjectTabInline(admin.StackedInline):
    model = ProjectTab
    extra = 1  # Number of empty forms to display for adding new tabs
    fields = ['icon', 'tab_title', 'image', 'content_title', 'content_description', 'button_text', 'button_link']
    readonly_fields = []  # Ensure image uploads are editable
    verbose_name_plural = "Project Tabs"

@admin.register(ProjectsSection)
class ProjectsSectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle']
    inlines = [ProjectTabInline]

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'image')
    search_fields = ('title', 'subtitle')






admin.site.register(AboutUs)


class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'experience_years')
    search_fields = ('title', 'subtitle', 'description')
    list_editable = ('experience_years',)

# Define admin interface for Category model
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

# Define admin interface for BlogPost model


@admin.register(BlogPost)
class BlogPostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at', 'category')
    search_fields = ('title', 'content')
    summernote_fields = ('content',)

    prepopulated_fields = {'slug': ('title',)}

# Define admin interface for ContactUs model




@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'message')

# Define admin interface for TeamMember model


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation')
    search_fields = ('name', 'designation', 'description')

# Define admin interface for FAQ model

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation')
    search_fields = ('name', 'designation', 'description')





admin.site.register(FAQ)





