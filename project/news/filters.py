from django_filters import FilterSet, DateFilter, ModelMultipleChoiceFilter,CharFilter
from .models import Post, Category, Author
from django import forms

# Создаем свой набор фильтров для модели Product.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class NewsFilter(FilterSet):

    name = CharFilter (lookup_expr = 'icontains', field_name = "name", label = 'Название')
    some_data = DateFilter(field_name = "some_data",lookup_expr = 'gte', label = 'Дата', widget = forms.DateInput(attrs = {'type': 'date'},))
    category = ModelMultipleChoiceFilter(field_name = 'post_category', queryset = Category.objects.all(), label = 'Категории', conjoined = True)
    post_author = CharFilter(lookup_expr = 'icontains', field_name = "post_author", label = 'Автор')

    class Meta:
        model = Post
        fields = ['name','post_author']
