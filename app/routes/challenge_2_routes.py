#!/usr/bin/env python

from flask_restful import Resource
from flask import request
from controllers.challenge_2_resize_image_controller import resize_image
from controllers.challenge_2_get_frames_for_min_max_depth_controller import (
    get_frames_for_min_max_depth,
)


class resize_image_route(Resource):
    def post(self):
        return resize_image()


class get_frames_for_min_max_depth_route(Resource):
    def get(self):
        min_depth = request.args.get("min_depth", type=float)
        max_depth = request.args.get("max_depth", type=float)
        print(f"------------------------")
        print(f"min_depth: {min_depth}, max_depth: {max_depth}")
        print(f"------------------------")
        return get_frames_for_min_max_depth(min_depth, max_depth)
