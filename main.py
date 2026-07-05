from pathlib import Path

file_types = {
    ".jpg": "IMAGES",
    ".png": "IMAGES"
}

target_folder = Path("D:/Ghani/Project")
for file in target_folder.iterdir():
    for ext, folder in file_types.items():
        if str(file).endswith(ext):
            (target_folder / folder).mkdir(exist_ok=True)
            break