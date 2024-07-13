from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Author,Kitob

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    fields = ['name', 'slug', 'photo', 'content']
    list_display = ('name', 'post_photo', 'content')
    list_display_links = ("name",)
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name", )}
    save_on_top = True

    @admin.display(description="Photo")
    def post_photo(self, author: Author):
        if author.photo:
            return mark_safe(f"<img src='{author.photo.url}' width='50' height='50' />")
        return "Без фото"


@admin.register(Kitob)
class KitobAdmin(admin.ModelAdmin):
    fields = ['name', 'author', 'slug', 'file', 'photo', 'is_published']
    readonly_fields = ['time_create']
    list_display = ('name', 'author', 'post_photo', 'file', 'time_create', 'is_published')
    list_display_links = ('name', 'author')
    search_fields = ('name', 'author__name')
    prepopulated_fields = {"slug": ("name",)}

    @admin.display(description="Photo")
    def post_photo(self, kitob: Kitob):
        if kitob.photo:
            return mark_safe(f"<img src='{kitob.photo.url}' width='50' height='50' />")
        return "Без фото"
