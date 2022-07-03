import os

# r = raw string
photo_folder = r"C:\Work\_PythonSuli\pycore-220702\photos"

# check if folder exists
assert os.path.exists(photo_folder), f"Folder does not exist: {photo_folder}"

# check if photo_folder IS folder and not file
assert os.path.isdir(photo_folder), f"Path must be a folder: {photo_folder}"


# todo collect files into a list with extension == .jpg or .jpeg
folder_content = os.listdir(photo_folder)
allowed_extensions = [".jpg", ".jpeg"]

for item in folder_content:
    file_path = os.path.join(photo_folder, item)
    _, ext = os.path.splitext(file_path)

    if ext.lower() in allowed_extensions:
        print(file_path)


# todo iterate on a photo list. Open photos and collect metadata
# todo store photo data into a dictionary
# todo save dictionary to a file