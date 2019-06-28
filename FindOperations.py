from bs4 import BeautifulSoup
from logger import Logger
import urllib.request
from time import time


class FindOperations(Logger):
    START = None
    END = None
    URL = None

    def __init__(self):
        super().__init__()
        self.log_setup()
        self.site_status = {}


    def calculate_time(self, start, end):
        return end - start

    def build_log_message(self, result, error=False):
        if error:
            calculated_time = "Site error"
        else:
            calculated_time = self.calculate_time(FindOperations.START, FindOperations.END)

        return "{} {} {}".format(
            FindOperations.URL,
            result,
            calculated_time)

    def load_site(self, url):
        FindOperations.URL = url
        return urllib.request.urlopen(url).read()

    def parse_site(self, site):
        FindOperations.START = time()
        data = BeautifulSoup(site, 'html.parser')
        FindOperations.END = time()
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
            status = "ERROR"
        else:
            result = "Element found"
            status = "OK"

        self.status_generator(status)
        message = self.build_log_message(result)
        self.log_operator.info(message)


    def status_generator(self, status):
        self.site_status[FindOperations.URL] = status


