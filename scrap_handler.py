from bs4 import BeautifulSoup
from logger import Logger
import urllib.request
from time import time


"""
Class which is responsible for performing operations connected with site status management.
"""
class ScrapOperator(Logger):
    START = None
    END = None
    URL = None

    def __init__(self, sites):
        super().__init__()
        self.log_setup()
        self.site_status = {web: "UNKNOWN" for web in sites}

    # Returns loaded site HTML
    @staticmethod
    def load_site(url):
        ScrapOperator.URL = url
        ScrapOperator.START = time()
        data = urllib.request.urlopen(url).read()
        ScrapOperator.END = time()
        return data

    # Returns raw data
    @staticmethod
    def parse_site(site):
        ScrapOperator.START = time()
        data = BeautifulSoup(site, 'html.parser')
        ScrapOperator.END = time()
        return data

    # Returns list, if item wasn't found the list would be empty
    @staticmethod
    def find_element(tuple_data, info):
        element, el_type, key = tuple_data

        # Find by text
        if element == "text":
            return info.body.find_all(text=key)
        # Find by other parameters e.g. (p, class, text)
        else:
            return info.body.find_all(element, {el_type: key})

    # Checks if list was empty (it means element wasn't found) and creates proper info in log
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

    # Maps site url with its status
    def status_generator(self, status):
        self.site_status[ScrapOperator.URL] = status

    @staticmethod
    # Returns page load time
    def calculate_time(start, end):
        return end - start

    # Creates message inserted to log file
    def build_log_message(self, result, error=False):
        # Error means that there's a problem with web site so loading time is negligible
        if error:
            calculated_time = "Site error"
        # In other case calculate time
        else:
            calculated_time = self.calculate_time(ScrapOperator.START, ScrapOperator.END)

        # {site url} {result of checking operataion} {time}
        return "{} {} {}".format(
            ScrapOperator.URL,
            result,
            calculated_time)
