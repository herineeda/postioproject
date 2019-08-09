from django.contrib import admin
from .models import License
from .models import Career
from .models import Portfolio
from .models import Profile

admin.site.register(Career)
admin.site.register(License)
admin.site.register(Portfolio)
admin.site.register(Profile)
