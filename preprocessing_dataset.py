from PIL import Image
import os

input_dir = "raw_images"
output_dir = "anime_faces_256"
os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(input_dir):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        img = Image.open(os.path.join(input_dir, filename)).convert("RGB")
        img = img.resize((256, 256), Image.ANTIALIAS)
        img.save(os.path.join(output_dir, filename))
