from django.contrib import admin

# Register your models here.
from .models import Question, Choice

class ChoiceInline(admin.TabularInline): 
	'''class object admin.StackedInline changed to 
	admin.TabularInline for better look.'''
	model = Choice
	extra = 3

class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
	('Question', {'fields': ['question_text']}),
	('Date information', {'fields': ['pub_date'], 
		'classes': ['collapse']}),
	]
	inlines = [ChoiceInline]

	list_display = ('question_text', 'pub_date', 
		'was_published_recently')
	list_filter = ['pub_date']
	search_fields = ['question_text']
	#search_fields = ['choice_text']

admin.site.register(Question, QuestionAdmin)
"""Removed the register() call for the Choice model and editted the 
Question registration code to read."""

#admin.site.register(Choice)