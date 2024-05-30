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
import blosc
import pymongo
import pickle


def resize_image():
    object_id = ObjectId()
    img_df = pd.read_csv("data/Challenge2_1.csv")
    img_df = img_df.drop(["depth"], axis=1)
    image = img_df.head().to_numpy()
    image = np.asarray(image)
    resized_img = cv2.resize(
        image, (200, img_df.shape[0]), interpolation=cv2.INTER_NEAREST
    )
    compressed_img = blosc.pack_array(resized_img)
    db_result = aiq_db["images"].insert_one({"image": compressed_img})
    return jsonify("Successfully inserted resized image into images col")
