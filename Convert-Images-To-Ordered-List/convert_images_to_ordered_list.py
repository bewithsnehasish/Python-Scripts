import os

from PIL import Image

def rename_images(folder_path):
    image_files = [f for f in os.listdir(folder_path) if f.endswith(('.jpg', '.jpeg', '.png', '.gif'))]
    image_files.sort()
    count = 1
    
    for image_file in image_files:
        _, ext = os.path.splitext(image_file)
        new_filename = str(count) + ext
        
        old_image_path = os.path.join(folder_path, image_file)
        new_image_path = os.path.join(folder_path, new_filename)
        
        os.rename(old_image_path, new_image_path)
        count += 1

if __name__ == "__main__":
    folder_path = "path/to/your/folder"
    rename_images(folder_path)
