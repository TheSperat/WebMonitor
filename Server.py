from flask import render_template
import flask


class WebSiteOperator:
    def __init__(self, websites):
        self.websites = websites
        self.create_dictionary()
        self.app = flask.Flask('my app')

    def create_dictionary(self):
        self.items = {web: "UNKNOWN" for web in self.websites}

        print(self.items)

    def set_status(self, info):
        self.items = info

    def run_app(self):
        with self.app.app_context():
            rendered = render_template('index.html',
                                       title="My Generated Page",
                                       sites=self.items)



