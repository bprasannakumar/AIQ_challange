ALLOWED_EXTENSIONS = ["png", "jpeg", "jpg"]
UPLOAD_FOLDER = "./images"
MAX_CONTENT_LENGTH = 500 * 1000 * 1000  # 500 MB


def is_allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
