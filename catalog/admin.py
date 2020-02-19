from django.contrib import admin

# Register your models here.

# Modelos a importar
from .models import Author, Genre, Book, BookInstance, LanguageBook

# Se crean clases para la gestión en la interfase de administración

# Se crean las clases para la edicion en cadena

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    # extra define el numero de formularios que se muestran en el inline
    extra=0

class BooksAuthorInline(admin.TabularInline):
    model = Book
    fields = ['title', 'isbn', 'languagebook']
    # extra define el numero de formularios que se muestran en el inline
    extra=0


# Se crean la clase para la manipulacion de objetos en la interfas de administración

# Define the AuthorAdmin class
class AuthorAdmin(admin.ModelAdmin):
    # campos a mostrar en la matriz
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    # campos a mostrar en el formulario
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines=[BooksAuthorInline]

# Define la clase BookAdmin
# Añade el decorador admin.register que registra los modelos. Es igual que admin.site.register(Book)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # display_genre es un metodo que se define en el modelo Book.
    list_display = ('title', 'author', 'display_genre')

    # permite la edicion en cadena de bookinstance
    inlines = [BooksInstanceInline]

# Define la clase BookInstanceAdmin
# Añade el decorador admin.register que registra los modelos. Es igual que admin.site.register(BookInstance)
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display=('book', 'borrower', 'status', 'due_back', 'id')
    list_filter = ('status', 'due_back')
    # agrupa los campos en los formularios
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'borrower', 'due_back')
        }),
    )

# Registro en el sitio de administracion de los modelos y clases
# admin.site.register(Book)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
# admin.site.register(BookInstance)
admin.site.register(LanguageBook)


