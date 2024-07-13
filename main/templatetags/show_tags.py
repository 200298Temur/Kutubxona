# Import necessary modules
from django import template
from main.models import Author  # Adjust 'Author' to your actual model name

# Register a new template library
register = template.Library()

# Define an inclusion tag named 'show_avtor'
@register.inclusion_tag("core/list_avtor.html")
def show_avtor(cat_selected=0):
    # Retrieve all Author objects from the database
    users = Author.objects.all()

    return {"users": users, "cat_selected": cat_selected}
