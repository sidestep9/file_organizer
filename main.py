from pathlib import Path
import shutil, sys

file_types = {
    ".jpg": "IMAGES",
    ".png": "IMAGES",
    ".pdf": "PDFs",
    ".docx": "DOCUMENTS",
    ".mp3": "AUDIOS",
    ".wav": "AUDIOS",
    ".mp4": "VIDEOS"
} # Can always add more!

print("Enter target folder")

target_folder = Path(input("> "))
if not target_folder.exists():
    print("Couldn't find path!")
    sys.exit()

for file in target_folder.iterdir():
    for ext, folder in file_types.items():
        if str(file).endswith(ext):
            (target_folder / folder).mkdir(exist_ok=True)
            shutil.move(file, (target_folder / folder))
            print(f"Moving: {str(file.parts[-1])} to {(target_folder / folder)}")
            break