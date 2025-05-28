from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario
from .forms import UsuarioCreationForm

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    add_form = UsuarioCreationForm
    model = Usuario

    list_display = ('username', 'email', 'dni', 'telefono', 'is_staff', 'obtener_nombre_completo')
    search_fields = ('username', 'dni', 'telefono', 'email')
    ordering = ('username',)

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'dni', 'telefono', 'email', 'password1', 'password2'),
        }),
    )

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Información personal', {'fields': ('first_name', 'last_name', 'email', 'dni', 'telefono')}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Fechas importantes', {'fields': ('last_login', 'date_joined')}),
    )
