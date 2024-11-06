import albumentations as A
import cv2
import os
import numpy as np
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

input_dir = "C:/Users/danie/git/ImageAugmentation/images" 
output_dir = 'C:/Users/danie/git/ImageAugmentation/augmented_images'
os.makedirs(output_dir, exist_ok=True)

def process_image(img_name, transform, input_dir, output_dir):
    img_path = os.path.join(input_dir, img_name)
    image = cv2.imread(img_path)

    if image is None:
        print(f"Errore nel caricare l'immagine {img_name}. Saltata.")
        return None
    
    augmented = transform(image=image)
    augmented_image = augmented["image"]

    output_path = os.path.join(output_dir, img_name)
    cv2.imwrite(output_path, augmented_image)
    return img_name  

def augmentDir_par(input_dir, output_dir, num_processes=os.cpu_count(), transform = A.Compose([
                                                                            A.GridDistortion(num_steps=5, distort_limit=0.3, p=0.5),
                                                                            A.HorizontalFlip(p=0.5),
                                                                            A.RandomBrightnessContrast(p=0.2),
                                                                            A.Rotate(limit=40, p=0.5)
                                                                        ])):
    image_list = os.listdir(input_dir)

    with ThreadPoolExecutor(max_workers=num_processes) as executor:
        futures = [executor.submit(process_image, img_name, transform, input_dir, output_dir) for img_name in image_list]
        
        for future in tqdm(as_completed(futures), total=len(futures)):
            img_name = future.result()

    print("Processo di augmentazione parallela completato!")