from django.contrib import admin
from polls.models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [ (None, {'fields':['question_text']}),
                  ('Date Information', {'fields':['publication_date'], 'classes':['collapse'] }),
                ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'publication_date', 'was_published_recently')
    list_filter = ['publication_date']
    search_fields = ['question_text']

# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
