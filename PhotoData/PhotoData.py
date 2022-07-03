import os, json
from PIL import Image, ExifTags

# r = raw string
photo_folder = r"C:\Work\_PythonSuli\pycore-220702\photos"

# check if folder exists
assert os.path.exists(photo_folder), f"Folder does not exist: {photo_folder}"

# check if photo_folder IS folder and not file
assert os.path.isdir(photo_folder), f"Path must be a folder: {photo_folder}"


# collect files into the photo_files with extension == .jpg or .jpeg
folder_content = os.listdir(photo_folder)
allowed_extensions = [".jpg", ".jpeg"]

photo_files = []
for item in folder_content:
    file_path = os.path.join(photo_folder, item)
    _, ext = os.path.splitext(file_path)

    if ext.lower() in allowed_extensions:
        photo_files.append(file_path)


# todo iterate on photo_files. Open photos and collect metadata
photo_data = {}
for photo in photo_files:
    img = Image.open(photo)

    # can be = None
    exif_data = img._getexif()

    if not exif_data:
        continue

    # todo store photo data into a dictionary
    photo_data[photo] = {
        "size": img.size,
        "camera_model": exif_data.get(0x0110),
        "date": exif_data.get(0x9003),
        "iso": exif_data.get(0x8827)
    }

# save dictionary to a file
with open("photo_data.json", "w") as f:
    json.dump(photo_data, f)