from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello world</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return 'Hello ' + name


@app.route('/<celsius>')
def show_celsius(celsius=""):
    try:
        string = 'Original value: ' + celsius + '<br />'
        string += 'Converted value: ' + str(convert_to_fahrenheit(int(celsius)))
    except ValueError:
        string = 'The value entered was not a number'
    return string


def convert_to_fahrenheit(celsius):
    """Convert a value from Celsius to Fahrenheit"""
    return celsius * 9.0 / 5 + 32


if __name__ == '__main__':
    app.run()
