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
