from datetime import datetime, timedelta
import bs4
from base_parser import Parser


class SfeduParser(Parser):
    months = {'января': 1, 'февраля': 2, 'марта': 3, 'апреля': 4, 'мая': 5, 'июня' : 6,
             'июля': 7, 'августа': 8, 'сентября': 9, 'октября': 10, 'ноября': 11 , 'декабря': 12 }

    def __init__(self, url: str):
        super().__init__(url)

    @staticmethod
    def __date(t: str):
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

    def parse(self):
        parser = bs4.BeautifulSoup(self.content, 'html.parser')

        i: bs4.Tag
        for i in parser.find_all('div', {'class': "act"}):
            image = i.find('img')['src']
            head = i.find('div', {'class': 'acttitle'}).find('a')
            date = self.__date(i.find('div', {'class': 'actdate'}).text)
            link = head['href']
            title = head.text
            description = i.find('div', {'class': 'acttext'}).text

            print(image)
            print(link)
            print(title)
            print(date)
            print(description)


p = SfeduParser('https://sfedu.ru/press-center/newspage/1')
