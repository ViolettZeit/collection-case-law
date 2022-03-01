from flask import Flask
from collect import selenium_driver

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    selenium_driver.do_collect();
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
