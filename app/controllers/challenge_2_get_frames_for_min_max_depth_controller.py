from flask import jsonify
import pandas as pd


def get_frames_for_min_max_depth(min_depth, max_depth):
    img_df = pd.read_csv("data/Challenge2_1.csv")
    filtered_df = img_df[
        (img_df["depth"] >= min_depth) & (img_df["depth"] <= max_depth)
    ]
    result_df = filtered_df.drop(["depth"], axis=1)
    response = result_df.to_json()
    return jsonify(response)
