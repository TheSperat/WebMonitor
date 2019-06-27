from bs4 import BeautifulSoup
import urllib.request
from time import time
import logging
import http.server
import socketserver


class FindOperations:
    start = None
    end = None
    url = None
    logging.basicConfig(level=logging.INFO)
    log_operator = logging.getLogger(__name__)
    log_operator.setLevel(logging.INFO)
    handler = logging.FileHandler('hello.log')
    handler.setLevel(logging.INFO)
    log_operator.addHandler(handler)


    def load_site(self, url):
        print("Tu musi być info!!!!")
        FindOperations.url = url
        return urllib.request.urlopen(url).read()

    def parse_site(self, site):
        FindOperations.start = time()
        data = BeautifulSoup(site, 'html.parser')
        FindOperations.end = time()
        return data


    def find_element(self, tuple_data, info):
        element, el_type, key = tuple_data
        # print(info)

        print(element, key)
        if element == "text":
            return info.body.find_all(text=key)
        else:
            return info.body.find_all(element, {el_type: key})

    def check_condition(self, element):
        if not element:
            result = "Element NOT found!"
        else:
            result = "Element found"

        builder = "{} {} {}".format(FindOperations.url, result, FindOperations.end - FindOperations.start)
        FindOperations.log_operator.info(builder)

