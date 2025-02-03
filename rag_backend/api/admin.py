from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Document, Question

# Extend the default UserAdmin
class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'is_staff', 'date_joined')
    search_fields = ('username', 'email')
    list_filter = ('is_staff', 'is_superuser', 'date_joined')
    ordering = ('-date_joined',)

# Register Custom User Admin
admin.site.unregister(User)  # Unregister default User model
admin.site.register(User, CustomUserAdmin)  # Register custom User admin

# Register Document Model
@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'file', 'uploaded_at')
    search_fields = ('user__username', 'file')
    list_filter = ('uploaded_at',)

# Register Question Model
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'document', 'question', 'answer', 'created_at')
    search_fields = ('user__username', 'question')
    list_filter = ('created_at',)
