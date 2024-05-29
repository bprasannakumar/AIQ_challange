import cv2
import numpy as np


def process_image(file_bytes):
    coin_details = []
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    gray = cv2.imdecode(file_bytes, cv2.IMREAD_GRAYSCALE)

    blur = cv2.GaussianBlur(gray, (11, 11), 0)
    canny = cv2.Canny(blur, 30, 145, 3)
    dilated = cv2.dilate(canny, (1, 1), iterations=2)
    (contours, heirarchy) = cv2.findContours(
        dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE
    )
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    cv2.drawContours(rgb, contours, -1, (0, 255, 0), 2)
    for contour in contours:
        print(f"contour: {contour}")
        x_cord, y_cord, width, height = cv2.boundingRect(contour)
        print(f"x_cord: {x_cord}, y_cord: {y_cord}")
        (x, y), radius = cv2.minEnclosingCircle(contour)
        centroid = (int(x), int(y))
        radius = int(radius)
        coin_details.append(
            {
                "xCord": x_cord,
                "yCord": y_cord,
                "height": height,
                "width": width,
                "centroid": centroid,
                "radius": radius,
            }
        )
    return coin_details
