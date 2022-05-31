from abc import ABC, abstractmethod
from datetime import datetime, timedelta
from .models import SfeduArticle
import bs4
import requests


class Parser(ABC):
    url: str
    content: str

    def __init__(self, url: str):
        self.url = url
        self.get_content()
        self.parse()

    def get_content(self):
        self.content = requests.get(self.url).text

    @abstractmethod
    def parse(self):
        ...


class SfeduParser(Parser):
    months = {'января': 1, 'февраля': 2, 'марта': 3, 'апреля': 4, 'мая': 5, 'июня': 6,
              'июля': 7, 'августа': 8, 'сентября': 9, 'октября': 10, 'ноября': 11, 'декабря': 12}

    def __init__(self, url: str):
        super().__init__(url)

    @staticmethod
    def __date(t: str) -> datetime:
        now = datetime.today()
        if t == 'Сегодня':
            return now
        elif t == 'Вчера':
            return now - timedelta(days=1)
        else:
            t = t.split(' ')
            d = datetime.strptime(t[0], '%d')
            d = d.replace(year=now.year, month=SfeduParser.months[t[1]])
            return d

    def parse(self) -> None:
        parser = bs4.BeautifulSoup(self.content, 'html.parser')

        i: bs4.Tag
        for i in parser.find_all('div', {'class': "act"}):
            _image = i.find('img')['src']
            head = i.find('div', {'class': 'acttitle'}).find('a')
            _date = self.__date(i.find('div', {'class': 'actdate'}).text)
            _link = head['href']
            _title = head.text
            _description = i.find('div', {'class': 'acttext'}).text

            a = SfeduArticle(link=_link, title=_title,
                             description=_description, date=_date, imageurl=_image)
            a.save()


# p = SfeduParser('https://sfedu.ru/press-center/newspage/1')
