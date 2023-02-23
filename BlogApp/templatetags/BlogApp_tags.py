from django import template
from BlogApp.models import Post
register=template.Library()


@register.simple_tag
def total_posts():
    return Post.objects.count()



@register.inclusion_tag('BlogApp/latest_Posts.html')
def show_latest_Posts(count=2):
    latest_Posts=Post.objects.order_by('-publish')[:count]
    return{'latest_posts':latest_Posts}

from django.db.models import Count
#@register.assignment_tag 	#not-working
@register.simple_tag		#hence use simple_tag
def get_most_commented_posts(count=2):
    return Post.objects.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]



