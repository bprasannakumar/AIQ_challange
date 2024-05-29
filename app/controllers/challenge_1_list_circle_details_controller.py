from flask import jsonify, request
from werkzeug.utils import secure_filename
from utils.upload_utils import is_allowed_file, UPLOAD_FOLDER
from utils.image_processor import process_image
from utils.db_connection import aiq_db
import os
from bson.objectid import ObjectId


def list_circle_details(circle_id):
    response = {}
    doc = aiq_db["circles"].find_one({"_id": ObjectId(circle_id)})
    if doc:
        response = {
            "id": str(doc.get("_id")),
            "x-cord": doc.get("xCord"),
            "y-cord": doc.get("yCord"),
            "height": doc.get("height"),
            "width": doc.get("width"),
            "centroid": doc.get("centroid"),
            "radius": doc.get("radius"),
        }
    return jsonify(response)
