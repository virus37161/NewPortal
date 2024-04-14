from django import template

register = template.Library()

b = ['черт', 'редиска', 'number']
@register.filter()
def censor(a):
    a = a.split(' ')
    for i in b:
        if i in a:
            for s in range(len(a)):
                if a[s] == i:
                    a[s] = f"{a[s][0]}{(len(a[s]) - 2) * '*'}{a[s][-1]}"
    a = ' '.join(a)
    return a
