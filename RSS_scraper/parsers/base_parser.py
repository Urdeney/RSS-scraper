from abc import ABC, abstractmethod
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
