from django.contrib import admin
from .models import Hobby
from .models import Place
#from .models import Music
from .models import Photo
from .models import Post
from .models import Visit
from embed_video.admin import AdminVideoMixin



admin.site.register(Hobby)
admin.site.register(Place)
#admin.site.register(Music)
admin.site.register(Photo)
admin.site.register(Visit)

class PostAdmin(AdminVideoMixin, admin.ModelAdmin): 
    list_display = ('title', 'video') 

admin.site.register(Post, PostAdmin)

