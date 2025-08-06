import os
# config.py
SCENE_NAME = "kitchen"  #to train on different scene jsut change this

BASE_DIR = f"mipnerf360/{SCENE_NAME}/"
#BASE_DIR = f"nerf_sythetic/{SCENE_NAME}/"
POINTS3D_PATH = BASE_DIR + "sparse/0/points3D.txt"
IMAGES_TXT_PATH = BASE_DIR + "sparse/0/images.txt"
DEPTH_FILE_PATH = BASE_DIR + "depth/f.npy"
GP_DIR = BASE_DIR + "gp/"
TEST_VAR = GP_DIR + f"{SCENE_NAME}test_var.npy"
PREDICT_MEAN = GP_DIR + f"{SCENE_NAME}mean.npy"

# For densified results - handle both pixel-to-point and pixle-to-point (typo)
# Check both root and /0/ subdirectory structures
pixel_to_point_base_correct = f"{BASE_DIR}pixel-to-point-{SCENE_NAME}"
pixel_to_point_base_typo = f"{BASE_DIR}pixle-to-point-{SCENE_NAME}"

# Determine which directory exists and whether it has a /0/ subdirectory
if os.path.exists(pixel_to_point_base_correct):
    pixel_to_point_base = pixel_to_point_base_correct
elif os.path.exists(pixel_to_point_base_typo):
    pixel_to_point_base = pixel_to_point_base_typo
else:
    raise FileNotFoundError(f"Neither {pixel_to_point_base_correct} nor {pixel_to_point_base_typo} exists")

# Check if /0/ subdirectory exists
if os.path.exists(pixel_to_point_base + "/0/"):
    PIXEL_TO_POINT_DIR = pixel_to_point_base + "/0/"
else:
    PIXEL_TO_POINT_DIR = pixel_to_point_base + "/"

PIXEL_TO_POINT_IMAGES = PIXEL_TO_POINT_DIR + "images.txt"
PIXEL_TO_POINT_POINTS3D = PIXEL_TO_POINT_DIR + "points3D.txt"