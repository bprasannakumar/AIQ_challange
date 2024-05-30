from flask import jsonify
from werkzeug.utils import secure_filename
from utils.upload_utils import is_allowed_file
from utils.image_processor import process_image
from utils.db_connection import aiq_db
import os
from bson.objectid import ObjectId
import numpy as np
import pandas as pd
import cv2
import io
import pymongo
import pickle


def resize_image():
    object_id = ObjectId()
    img_df = pd.read_csv("data/Challenge2_1.csv")
    img_df = img_df.drop(["depth"], axis=1)
    image_data = img_df.head().to_numpy()
    image = np.array(image_data)
    resized_img = cv2.resize(
        image, (200, img_df.shape[0]), interpolation=cv2.INTER_NEAREST
    )
    byte_stream = io.BytesIO()
    np.savez(byte_stream, resized_img)

    db_result = aiq_db["images"].insert_one({"_id": object_id, "image": byte_stream})
    return jsonify(
        {
            f"Successfully inserted resized image into images col with id {str(object_id)}"
        }
    )
