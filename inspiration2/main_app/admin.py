from django.contrib import admin
# import your models here
from .models import Inspiration, Gallery, Note

# Register your models here
admin.site.register(Inspiration)
admin.site.register(Gallery)
admin.site.register(Note)
