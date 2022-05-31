from datetime import datetime
from django.http import HttpResponse
from django.template import loader
from .models import SfeduArticle


def sfedu(_):
    date = datetime.today().strftime(r'%a, %d %b %Y %H:%M:%S %Z')
    nl = '\n'
    return HttpResponse(f"""<?xml version="1.0" encoding="utf-8"?>
<rss version="2.0">
<channel>
<title>Sfedu News</title>
<link>https://sfedu.ru/press-center/news</link>
<description>Sfedu Press Center Feed</description>
<language>ru-ru</language>
<pubDate>{date}</pubDate>
<lastBuildDate>{date}</lastBuildDate>
{nl.join(i.to_xml() for i in SfeduArticle.objects.all())}
</channel>
</rss>""")

# Create your views here.
def index(request):
    template = loader.get_template('rss_scraper/index.html')
    context = {}
    return HttpResponse(template.render(context, request))
