from django.urls import path, include, re_path

# importa la clase RedirectView que permite redirigir la url

from . import views

urlpatterns = [
    
    re_path(r'^$', views.index, name='index'),
    re_path(r'^books/$', views.BookListView.as_view(), name='books'),
    
    # La vista de detalle genérica basada en clases espera que se le envíe un parámetro llamado pk. 
    # Si estás escribiendo tu propia vista de función, puedes usar el nombre de parámetro que quieras, 
    # o incluso enviar la información como un argumento sin nombre.
    re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),


    # Una característica que no hemos usado aquí, pero que te puede resultar valiosa, es que puedes declarar 
    # y enviar opciones adicionales a la vista. Las opciones se declaran como un diccionario que envías como 
    # el tercer argumento sin nombre a la función url(). Esta estrategia puede resultar útil si quiere usar 
    # la misma vista para múltiples recursos, y enviar información para configurar su comportamiento 
    # en cada caso (abajo suministramos una plantilla diferente en cada caso).
    # url(r'^/url/$', views.my_reused_view, {'my_template_name': 'some_path'}, name='aurl'),
    # url(r'^/anotherurl/$', views.my_reused_view, {'my_template_name': 'another_path'}, name='anotherurl'),

    re_path(r'^autor/$', views.AutorListView.as_view(), name='autores'),
    re_path(r'^autor/(?P<pk>\d+)$', views.AutorDetailView.as_view(), name='autor-detail'),
    re_path(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    re_path(r'^borrowed/$', views.LoanedBooksListView.as_view(), name='all-borrowed'),
    re_path(r'^book/(?P<pk>[-\w]+)/renew/$', views.renew_book_librarian, name='renew-book-librarian'),
    re_path(r'^author/create/$', views.AuthorCreate.as_view(), name='author_create'),
    re_path(r'^autor/(?P<pk>\d+)/update/$', views.AuthorUpdate.as_view(), name='author_update'),
    re_path(r'^autor/(?P<pk>\d+)/delete/$', views.AuthorDelete.as_view(), name='author_delete'),
    re_path(r'^books/create/$', views.BookCreate.as_view(), name='book_create'),
    re_path(r'^book/(?P<pk>\d+)/update/$', views.BookUpdate.as_view(), name='book_update'),
    re_path(r'^book/(?P<pk>\d+)/delete/$', views.BookDelete.as_view(), name='book_delete'),
    
]