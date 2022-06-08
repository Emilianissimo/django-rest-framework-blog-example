# Django Rest Framework (DRF) - Test blog

Simple tutorial blog, included two standard models: Post and Category
with one to many from Category to Post.

Here I used all different types of API generation, that available in DRF.

Project map:
- 
- Models are locating in *'news'* folder
- *'news'* has their own serializer with different two side relation
- Serializers for class based views are locating in *'news_viewset'* and have PrimaryKey Category -> Post relation

Styles for api generating, I'd used there:
- 
- Regular Django func style
- ClassBased style
- MixinBased style
- GenericBased style
- View-sets

Routes for View-sets are generating inside *'drf_test'* project folder's *'urls.py'* file.

Endpoint map for 127.0.0.1 (standard host + port):
- 
- Regular - <a href="http://127.0.0.1:8000/api/func-based/">http://127.0.0.1:8000/api/func-based/
- Class based - <a href="http://127.0.0.1:8000/api/class-based/">http://127.0.0.1:8000/api/class-based/
- View sets - <a href="http://127.0.0.1:8000/api/view-sets/">http://127.0.0.1:8000/api/view-sets/
- Other doesn't have root, <a href="https://youtu.be/XvyLtlcCyNs?t=5" target="_blank">'cause </a>
- Mixins
- - Posts - <a target="_blank" href="http://127.0.0.1:8000/api/mixin-based/posts/">http://127.0.0.1:8000/api/mixin-based/posts/
- - Categories - <a href="http://127.0.0.1:8000/api/mixin-based/categories/">http://127.0.0.1:8000/api/mixin-based/categories/
- Generics
- - Posts - <a href="http://127.0.0.1:8000/api/generic-based/posts/">http://127.0.0.1:8000/api/generic-based/posts/
- - Categories - <a href="http://127.0.0.1:8000/api/generic-based/categories/">http://127.0.0.1:8000/api/generic-based/categories/
