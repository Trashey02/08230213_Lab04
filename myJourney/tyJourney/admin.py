from django.contrib import admin
from .models import AboutMe, LearningJourney, Reflection

# Register AboutMe model
@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Show name in the admin list view
    search_fields = ('name', 'description', 'hobbies')  # Allow searching

# Register LearningJourney model
@admin.register(LearningJourney)
class LearningJourneyAdmin(admin.ModelAdmin):
    list_display = ('year', 'skill')  # Show year and skill
    list_filter = ('year',)           # Filter by year
    search_fields = ('skill', 'challenges')  # Search by skill or challenges
    ordering = ('year',)              # Default ordering

# Register Reflection model
@admin.register(Reflection)
class ReflectionAdmin(admin.ModelAdmin):
    list_display = ('author', 'quote', 'date_added')  # Show key info
    search_fields = ('author', 'quote')               # Searchable
    ordering = ('-date_added',)                       # Most recent first
