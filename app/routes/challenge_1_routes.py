#!/usr/bin/env python

from flask_restful import Resource
from flask import Flask, jsonify, request
from controllers.challenge_1_file_uploader_controller import upload_file
from controllers.challenge_1_list_circular_objects_controller import (
    list_circular_objects,
)
from controllers.challenge_1_list_circle_details_controller import list_circle_details


class file_handler_route(Resource):
    def post(self):
        image = request.files.getlist("media")[0]
        return upload_file(image)


class list_circular_objects_route(Resource):
    def get(self, image_id):
        return list_circular_objects(image_id)


class list_circle_details_route(Resource):
    def get(self, circle_id):
        return list_circle_details(circle_id)
