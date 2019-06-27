from CONFIG import inforamtion, refresh_rate
from FindOperations import FindOperations
import sys
import time


x = FindOperations()
while True:
    try:
        site = x.load_site("https://photricity.com/flw/ajax/")
        parse = x.parse_site(site)
        find = x.find_element(inforamtion["https://photricity.com/flw/ajax/"], parse)
        x.check_condition(find)
    except:
        x.log_operator.info("{} {}".format(x.url + " ", sys.exc_info()[0]))

    time.sleep(refresh_rate)