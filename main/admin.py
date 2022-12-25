from django.contrib import admin
from .models import notes, comment

class comment_admin(admin.StackedInline):
	model = comment

class notes_admin(admin.ModelAdmin):

	inlines = [comment_admin]
	class Meta:
		model = notes

admin.site.register(notes, notes_admin)
admin.site.register(comment)