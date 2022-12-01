from flask import Flask

app = Flask(__name__)


# Decorators for various repeated stuff
def make_bold(bold):
    def wrapper_function():
        return f"<b>{bold()}</b>"

    return wrapper_function


def make_emphasis(emphasis):
    def wrapper_function():
        return f"<em>{emphasis()}</em>"

    return wrapper_function


def make_underline(underline):
    def wrapper_function():
        return f"<u>{underline()}</u>"

    return wrapper_function


@app.route('/')
@make_bold
@make_underline
@make_emphasis
def hello():
    return "<h1>Hello There how are you?</h1>"


if __name__ == "__main__":
    app.run(port=5001, debug=True)
