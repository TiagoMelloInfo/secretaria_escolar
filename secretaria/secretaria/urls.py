from django.contrib import admin
from django.urls import path, include

from alunos import urls as aluno_urls

urlpatterns = [
    path('alunos/', include(aluno_urls)),
    path('admin/', admin.site.urls),
]
