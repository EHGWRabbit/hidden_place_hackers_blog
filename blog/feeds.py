from django.contrib.syndication.views import Feed#framework sindication 
from django.template.defaultfilters import truncatewords 
from .models import Post 


class LatestPostsFeed(Feed):
    title = 'Убежище хакера'#rss element
    link = '/blog/'#rss element
    description = 'Новые записи в блоге'#rss element 

    def items(self):
        return Post.published.all()[:7]#get out objects into the feed  
    
    def item_title(self, item):
        return item.title#ttile every element 

    def item_description(self, item):
        return truncatewords(item.body, 30)#desciption every element 