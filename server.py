import sentry_sdk
import os
from bottle import Bottle, request, template, run
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(
    dsn="https://f4380e0754ae41efad6a7d6fa49a39a3@sentry.io/5052116",
    integrations=[BottleIntegration()]
)

app = Bottle()

@app.route('/')
def index():
    return template('index')


@app.route('/success')
def success():
      return '<h1>You have SUCCESS</h1>'

@app.route('/fail')
def fail():
    raise RuntimeError("There is an error!")
    return '<h1>You hve FAIL</h1>'


if os.environ.get("APP_LOCATION") == "heroku":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=3,
    )
else:
    app.run(host="localhost", port=8080, debug=True)