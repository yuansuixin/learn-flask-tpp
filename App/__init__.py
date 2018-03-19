
from flask import Flask

from App.Apis import init_api
from App.ext import init_ext
from App.settings import envs


def create_app(env):
    app = Flask(__name__)
    app.config.from_object(envs.get(env))
    init_ext(app)
    init_api(app)

    return app

















