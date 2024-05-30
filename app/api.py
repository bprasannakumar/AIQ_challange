#!/usr/bin/env python
from flask import Flask, render_template
from flask_restful import Api
import os
from dotenv import load_dotenv

from routes.challenge_1_routes import (
    file_handler_route,
    list_circular_objects_route,
    list_circle_details_route,
)
from routes.challenge_2_routes import (
    resize_image_route,
    get_frames_for_min_max_depth_route,
)


CODE_VERSION = "v1.0.0"

env_path = os.path.dirname(os.getcwd()) + "/app"
load_dotenv(os.path.join(env_path, ".env"))

app = Flask(__name__)
app.config["DEBUG"] = True
app.json.sort_keys = False

## app.register_blueprint(error_blueprint)
api = Api(app)
base_route = "/aiq"
print(f"AIQ Code Version: {CODE_VERSION}")


@app.route("/", methods=["GET"])
def home():
    return "<h1> Welcome to AIQ </h1>"


@app.route("/api/docs", methods=["GET"])
def get_docs():
    return render_template("swaggerui.html")


@app.route("/aiq/version", methods=["GET"])
def check_version():
    print("getting the code version")
    return {"version": CODE_VERSION}


api.add_resource(file_handler_route, "/aiq/image/upload")
api.add_resource(list_circular_objects_route, "/aiq/images/<string:image_id>")
api.add_resource(list_circle_details_route, "/aiq/circles/<string:circle_id>")

api.add_resource(resize_image_route, "/aiq/image/resize")
api.add_resource(
    get_frames_for_min_max_depth_route,
    "/aiq/image/fetch_frames",
)


app.run(host="0.0.0.0", port=os.getenv("PORT_NUMBER"))
