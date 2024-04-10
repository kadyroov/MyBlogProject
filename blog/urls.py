from django.urls import path
from blog.views import index, index_detail, ballon_types,types_detail

# "/" - главная страница
urlpatterns = [
    path("", index, name="main-page"),
    path("detail/<int:pk>", index_detail, name="detail-page" ),
    path("ballon-types", ballon_types, name="ballon-type" ),
    path("type-detail/<int:pk>", types_detail, name="type-detail")
]
