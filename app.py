from flask import Flask, render_template
import time
import sys
import _thread
from components.CONFIG import CONTENT_REQUIREMENTS, REFRESH_RATE
from components.scrap_handler import ScrapOperator


scrap_operator = ScrapOperator(CONTENT_REQUIREMENTS.keys())

'''
A function which is responsible of looping through all sites saved in CONFIG file
and checking if elements specified in this file are met
'''
def thread_function():
    while True:
        for key, value in CONTENT_REQUIREMENTS.items():

            try:
                site = scrap_operator.load_site(key)
                parse = scrap_operator.parse_site(site)
                find = scrap_operator.find_element(value, parse)
                scrap_operator.check_condition(find)
            except:
                message = scrap_operator.build_log_message(sys.exc_info()[0], error=True)
                scrap_operator.log_operator.info(message)
                scrap_operator.status_generator("ERROR")

        time.sleep(REFRESH_RATE)


app = Flask(__name__)

'''
Basic flask implementation
'''
@app.route("/")
def index():

    return render_template('index.html',
                           title="Sites statuses",
                           sites=scrap_operator.site_status)


if __name__ == "__main__":
    _thread.start_new_thread(thread_function, ())
    app.run(debug=False)
