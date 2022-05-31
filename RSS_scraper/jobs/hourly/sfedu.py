from django_extensions.management.jobs import HourlyJob
from ...parsers import SfeduParser

class Job(HourlyJob):
    help = 'sfedu.ru news parser'
    link = 'https://sfedu.ru/press-center/newspage/1'

    def execute(self):
        SfeduParser(Job.link)