import os

folder_path = 'F:/Mikayla Campinos'  # Update with your folder path
prefix = 'MikaylaCampinos_'  # Update with your desired prefix

counter = 1

for filename in os.listdir(folder_path):
    if os.path.isfile(os.path.join(folder_path, filename)):
        file_extension = os.path.splitext(filename)[1]
        new_filename = f"{prefix}_{counter}{file_extension}"
        os.rename(
            os.path.join(folder_path, filename),
            os.path.join(folder_path, new_filename)
        )
        counter += 1