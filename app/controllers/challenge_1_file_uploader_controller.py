from flask import jsonify
from werkzeug.utils import secure_filename
from utils.upload_utils import is_allowed_file
from utils.image_processor import process_image
from utils.db_connection import aiq_db
import os
from bson.objectid import ObjectId
import numpy as np


def upload_file(image):
    object_id = ObjectId()
    filename = ""
    filename = secure_filename(image.filename)
    print(is_allowed_file(filename))
    if is_allowed_file(filename):
        file_bytes = np.fromfile(image, np.uint8)
        # get co-ordinates of the image
        coin_details = process_image(file_bytes)

        # we can store image into any database of our choice, preferable to S3 bucket
        # but I am stoing to mongodb now
        file_data = image.stream.read()
        db_result = aiq_db["images"].insert_one({"_id": object_id, "image": file_data})
        print(db_result.acknowledged)
        coin_records = []

        for coin_detail in coin_details:
            coin_records.append(
                {
                    "xCord": coin_detail.get("xCord"),
                    "yCord": coin_detail.get("yCord"),
                    "height": coin_detail.get("height"),
                    "width": coin_detail.get("width"),
                    "centroid": coin_detail.get("centroid"),
                    "radius": coin_detail.get("radius"),
                    "imageId": object_id,
                }
            )
        aiq_db["circles"].insert_many(coin_records)
    else:
        return jsonify({"message": "File type not allowed"}), 400
    return jsonify({"name": filename, "status": "success"})
