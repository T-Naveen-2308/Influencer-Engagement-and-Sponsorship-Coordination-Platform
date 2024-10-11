from django.urls import path

from .apis import admin, influencer, main
from .apis import sponsor

urlmain = [
    ("func", main.func)
]

urladmin = [
    ("func", admin.func)
]

urlsponsor = [
    ("func", sponsor.func)
]

urlinfluencer = [
    ("func", influencer.func)
]

urlpatterns = (
                [path("main-api/"+tup[0]+"/", tup[1]) for tup in urlmain]
               + [path("admin-api/"+tup[0]+"/", tup[1]) for tup in urladmin]
               + [path("sponsor-api/"+tup[0]+"/", tup[1]) for tup in urlsponsor]
               + [path("influencer-api/"+tup[0]+"/", tup[1]) for tup in urlinfluencer]
            )