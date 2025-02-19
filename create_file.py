import os

def create_file():
    documents_path = os.path.join(os.path.expanduser("~"), "Documents")
    file_path = os.path.join(documents_path, "prank.txt")
    with open(file_path, "w") as file:
        file.write("You've been pranked")
    print(file_path)

if __name__ == "__main__":
    create_file()