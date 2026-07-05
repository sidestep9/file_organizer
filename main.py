from pathlib import Path
import shutil

file_types = {
    ".jpg": "IMAGES",
    ".png": "IMAGES",
    ".pdf": "PDFs",
    ".docx": "DOCUMENTS",
    ".mp3": "AUDIOS",
    ".wav": "AUDIOS",
    ".mp4": "VIDEOS"
}

target_folder = Path("D:/Ghani/Project")
for file in target_folder.iterdir():
    for ext, folder in file_types.items():
        if str(file).endswith(ext):
            (target_folder / folder).mkdir(exist_ok=True)
            shutil.move(file, (target_folder / folder))
            print(f"Moving: {str(file.parts[-1])} to {(target_folder / folder)}")
            break