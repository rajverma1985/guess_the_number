import random

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


def logging_decorator(function):
    def wrapper(*args, **kwargs):
        return f"{function.__name__}{args} function called"

    return wrapper


@app.route('/')
@make_bold
def guess():
    return f"<h1>Guess a number between 0 and 9</h1><img " \
           f"src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"


# todo see if you can add too high, too low or right!
@app.route('/<int:num>')
def num_generator(num):
    gen = random.randint(0, 9)
    if num == gen:
        return f"<h1>Yup you guessed it right!</h1>" \
               f"<img src='https://media.giphy.com/media/QuTOdlwvMl5lHKbpRC/" \
               f"giphy.gif?cid=ecf05e47opd543a292l85ik5f2pghpz8bwrbcca1kyx2d94z&rid=giphy.gif&ct=g'>"
    else:
        return f"<h1>Nope try again!</h1><img src='https://media.giphy.com/media/wV2LWS2IPouNWSj1on/" \
               f"giphy.gif?cid=ecf05e47tb8kmuqk3c8idrqgua3v9lrxbfsj5z2nxih4tnzz&rid=giphy.gif&ct=g'>"


if __name__ == "__main__":
    app.run(port=5001, debug=True)
