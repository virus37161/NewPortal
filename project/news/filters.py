from django_filters import FilterSet, DateFilter, ModelMultipleChoiceFilter
from .models import Post, Category, Author
from django import forms

# Создаем свой набор фильтров для модели Product.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class NewsFilter(FilterSet):

    some_data = DateFilter(field_name = "some_data",lookup_expr = 'gte', label = 'Date', widget = forms.DateInput(attrs = {'type': 'date'},))
    category = ModelMultipleChoiceFilter(field_name = 'post_category', queryset = Category.objects.all(), label = 'Category', conjoined = True)

    class Meta:
        model = Post
        fields = {
           'name': ['icontains'],
           'post_author__user__username':['icontains'],

        }