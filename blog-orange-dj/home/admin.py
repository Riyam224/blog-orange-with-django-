from django.contrib import admin

# Register your models here.
from .models import Customer , Post , Recent_Post , Comment , Category , About , Team , Contact

admin.site.register(Customer)
admin.site.register(Post)
admin.site.register(Recent_Post)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(About)
admin.site.register(Team)
admin.site.register(Contact)