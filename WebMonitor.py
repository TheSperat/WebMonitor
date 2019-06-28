from CONFIG import inforamtion, refresh_rate
from FindOperations import FindOperations
from Server import WebSiteOperator
import sys
import time


x = FindOperations()
f = WebSiteOperator(inforamtion.keys())
site_statuses = {}

while True:
    f.run_app()
    for key, value in inforamtion.items():

        try:
            site = x.load_site(key)
            parse = x.parse_site(site)
            find = x.find_element(value, parse)
            x.check_condition(find)
            print("no exception")
        except:
            message = x.build_log_message(sys.exc_info()[0], True)
            x.log_operator.info(message)
            x.status_generator("ERROR")

    print(x.site_status)
    f.set_status(x.site_status)
    time.sleep(refresh_rate)