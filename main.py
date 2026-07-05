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
    if not file.is_file():
        continue

    folder = file_types.get(file.suffix.lower())
    if folder is None:
        continue

    (target_folder / folder).mkdir(exist_ok=True)
    numbering = 0
    destination = (target_folder / folder / file.parts[-1])

    while True:
        if destination.exists():
            numbering += 1
            destination = (target_folder / folder / (file.stem + "(" + str(numbering) + ")" +"".join(file.suffixes)))
        else:
            shutil.move(file, destination)
            print(f"Moving: {str(file.parts[-1])} to {(target_folder / folder)}")
            break