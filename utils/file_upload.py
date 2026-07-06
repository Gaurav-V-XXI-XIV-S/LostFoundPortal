import os
import uuid

from flask import current_app
from werkzeug.utils import secure_filename


def allowed_image(filename):
    if "." not in filename:
        return False
    extension = filename.rsplit(".", 1)[1].lower()
    return extension in current_app.config["ALLOWED_IMAGE_EXTENSIONS"]


def save_upload(file_storage, folder_key):
    if not file_storage or not file_storage.filename:
        return None
    if not allowed_image(file_storage.filename):
        raise ValueError("Only PNG, JPG, JPEG, and WEBP images are allowed.")

    folder = current_app.config[folder_key]
    os.makedirs(folder, exist_ok=True)
    original = secure_filename(file_storage.filename)
    extension = original.rsplit(".", 1)[1].lower()
    filename = f"{uuid.uuid4().hex}.{extension}"
    path = os.path.join(folder, filename)
    file_storage.save(path)

    relative = os.path.relpath(path, current_app.static_folder).replace("\\", "/")
    return f"uploads/{relative.split('uploads/', 1)[1]}"
