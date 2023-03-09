from django.contrib import admin
from .models import Blog_Post, Comment, Meta


# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
    # Let you to search with title name, release year and length of duration of movie
    search_fields = ['title', 'created_on',]
    # There will be a filter on release year
    list_filter = ['created_on',]
    list_display =['title', 'created_on',]
    prepopulated_fields = { 'slug' : ('title',)}
    actions=['really_delete_selected']

    def get_actions(self, request):
        actions = super(BlogPostAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    def really_delete_selected(self, request, queryset):
        for obj in queryset:
            obj.delete()

        if queryset.count() == 1:
            message_bit = "1 Category entry was"
        else:
            message_bit = "%s category entries were" % queryset.count()
        self.message_user(request, "%s successfully deleted." % message_bit)
    really_delete_selected.short_description = "Delete selected entries"


    
admin.site.register(Blog_Post, BlogPostAdmin)
admin.site.register(Comment)

