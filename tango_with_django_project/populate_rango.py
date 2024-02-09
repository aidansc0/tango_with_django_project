import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page

def populate():
    python_pages = [
        {'title': 'Official Python Tutorial','url':'http://docs.python.org/3/tutorial/', 'views': 12, 'likes': 6},
        {'title':'How to Think like a Computer Scientist','url':'http://www.greenteapress.com/thinkpython/', 'views': 34, 'likes': 21},
        {'title':'Learn Python in 10 Minutes','url':'http://www.korokithakis.net/tutorials/python/', 'views': 32, 'likes': 28} 
         ]
    
    django_pages = [
        {'title':'Official Django Tutorial','url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/', 'views': 44, 'likes': 6},
        {'title':'Django Rocks','url':'http://www.djangorocks.com/', 'views': 33, 'likes': 21},
        {'title':'How to Tango with Django','url':'http://www.tangowithdjango.com/', 'views': 56, 'likes': 28}
        ]
    
    other_pages = [
        {'title':'Bottle','url':'http://bottlepy.org/docs/dev/', 'views': 21, 'likes': 12},
        {'title':'Flask','url':'http://flask.pocoo.org', 'views': 78, 'likes': 34}
        ]
    
    cats = {'Python': {'pages': python_pages, 'views': 128, 'likes': 64},
            'Django': {'pages': django_pages, 'views': 64, 'likes': 32},
            'Other Frameworks': {'pages': other_pages, 'views': 32, 'likes': 16}
            }
    
    for cat, cat_data in cats.items():
        c = add_cat(cat, views=cat_data['views'], likes=cat_data['likes'])
        for p in cat_data['pages']:
            add_page(c,p['title'],p['url'], p['views'], p['likes'])

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')

def add_page(cat,title,url,views,likes):
    p = Page.objects.get_or_create(category=cat,title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name)[0]
    c.likes=likes
    c.views=views
    c.save()
    return c

if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()



