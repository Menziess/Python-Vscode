from flask import Flask
from redis import Redis, RedisError
from .cli.command_line_fib import fib
import os
import socket

# Connect to Redis
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)
app = Flask(__name__)


@app.route("/")
def hello():
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "<i>cannot connect to Redis, counter disabled</i>"

    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Visits:</b> {visits}"
    return html.format(
        name=os.getenv("NAME", "world"),
        hostname=socket.gethostname(),
        visits=visits)


@app.route("/fib/<int:n>")
def calc_fib(n):
    return f"Fibonacci of {n} is {fib(n)}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
