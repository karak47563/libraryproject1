
import apps.bookmodule.views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', apps.bookmodule.views.index), #add only this line of code
	path('index2/<int:val1>/', apps.bookmodule.views.index2), #add only this line
	path('books/', include("apps.bookmodule.urls")), #include urls.py of bookmodule app
	path('users/', include("apps.usermodule.urls")) #include urls.py of usermodule app
]
