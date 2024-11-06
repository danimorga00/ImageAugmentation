import csv
import time
import albumentations as A
import cv2
import os
import numpy as np
from tqdm import tqdm 
from augmentation_par import augmentDir_par  

input_dir = 'C:/Users/danie/Pictures/imagenette' 
output_dir = 'C:/Users/danie/git/ImageAugmentation/augmented_images'

os.makedirs(output_dir, exist_ok=True)

ITERATIONS = 25
transform = A.Compose([
                        A.ElasticTransform(alpha=1, sigma=50, alpha_affine=50, p=1),
                        A.GridDistortion(num_steps=5, distort_limit=0.3, p=1),
                        A.HorizontalFlip(p=1),
                        A.RandomBrightnessContrast(p=1),
                        A.Rotate(limit=40, p=1)
                    ])

report = []

for i in range(ITERATIONS):
    result = []
    result.append(i+1)
    start = time.time()
    print(f"num workers: {i+1}")
    augmentDir_par(input_dir, output_dir, i+1, transform)
    result.append(time.time() - start)
    report.append(result)

with open("results", mode='w', newline='', encoding='utf-8') as file_csv:
    scrittore = csv.writer(file_csv)
    scrittore.writerows(report)