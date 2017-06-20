from django.contrib import admin
from polls.models import Question, Choice


# derived from admin.TabularInline (as opposed to admin.StackedInline) to create a table-like display.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        # title, map of properties (fields, HTML classes, etc.)
        ('Q', {'fields':['question_text']}),
        ('Date Info', {'fields':['publication_date'], 'classes':['collapse'] }),
    ]

    # Associated/related model to be displayed 'inline'.
    inlines = [ChoiceInline]

    # Columns to display for change-list (enumerate) Question view
    list_display = ('question_text', 'publication_date', 'was_published_recently')

    # side bar list filter. The type of filter possible depends of the type of the field assigned. Must
    # be derived from models.Field, otherwise exception!
    list_filter = ['publication_date']

    # Add search box - list all the Field(s) to do the search!
    search_fields = ['question_text', 'publication_date']

    # Change list pagination - how many items to display per page!
    list_per_page = 3

# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)

# to a new branch
# Edited on root/master branch
