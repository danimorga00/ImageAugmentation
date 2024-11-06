import os
import shutil

# Specifica la cartella di origine e quella di destinazione
destination_folder = 'C:/Users/danie/Pictures/imagenette'
source_folder = 'C:/Users/danie/Downloads/imagenette2/imagenette2/train'

# Crea la cartella di destinazione se non esiste
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Lista delle estensioni di file immagine comuni
image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp']

# Scansione ricorsiva della cartella di origine
for root, dirs, files in os.walk(source_folder):
    for file in files:
        # Verifica che il file sia un'immagine
        if any(file.lower().endswith(ext) for ext in image_extensions):
            # Percorso completo del file da spostare
            source_path = os.path.join(root, file)
            destination_path = os.path.join(destination_folder, file)
            
            # In caso di file con lo stesso nome, rinomina aggiungendo un suffisso numerico
            base_name, extension = os.path.splitext(file)
            counter = 1
            while os.path.exists(destination_path):
                new_name = f"{base_name}_{counter}{extension}"
                destination_path = os.path.join(destination_folder, new_name)
                counter += 1
            
            # Sposta il file nella cartella di destinazione
            shutil.move(source_path, destination_path)
            print(f"Spostato: {source_path} -> {destination_path}")

print("Tutte le foto sono state spostate nella cartella di destinazione.")
