import os
import shutil
from pathlib import Path

DOCUMENTS_PATH = os.path.join(os.path.expanduser("~"), "Documents")
TEXT_FILE_PATH = os.path.join(DOCUMENTS_PATH, "prank.txt")

def create_text_file():
    with open(TEXT_FILE_PATH, "w") as file:
        file.write("You've been pranked")


def create_quick_cmd():
#     launcher_code = """
# import os
# os.system('start cmd /c exit')
# """ # Code within the created file
#     with open(os.path.join(DOCUMENTS_PATH, "quick_cmd.py"), "w") as file:
#         file.write(launcher_code)
    os.system(f"python -m PyInstaller --onefile \"{os.path.join(DOCUMENTS_PATH, "quick_cmd.py")}\"") # Turns the created Python file into an executable
    # Moves the file to the documents folder
    dist_executable = Path("dist") / "quick_cmd.exe"
    destination = os.path.join(DOCUMENTS_PATH, "quick_cmd.exe")
    if dist_executable.exists():
        shutil.move(str(dist_executable), str(destination))
    else:
        pass
    # Remove created folders and files to keep things clean
    for folder in ["dist", "build"]:
        if Path(folder).exists():
            shutil.rmtree(folder)
    spec_file = Path("quick_cmd.spec")
    if spec_file.exists():
        spec_file.unlink()


if __name__ == "__main__":
    # create_text_file()
    create_quick_cmd()