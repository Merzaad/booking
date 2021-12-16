from django.contrib import admin
from .models import room
from .models import room_number
from .models import reservation

admin.site.register(room)
admin.site.register(room_number)
admin.site.register(reservation)

