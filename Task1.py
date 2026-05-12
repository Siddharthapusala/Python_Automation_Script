import os
import shutil
import logging

logging.basicConfig(
    filename='file_organizer.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
FILE_TYPES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.ppt', '.pptx', '.xls', '.xlsx'],
    'Audio': ['.mp3', '.wav', '.aac'],
    'Videos': ['.mp4', '.mkv', '.avi', '.mov'],
    'Archives': ['.zip', '.rar', '.7z'],
    'Others': []
}
def get_category(filename):
    """
    Returns the category based on file extension.
    """
    _, ext = os.path.splitext(filename)
    ext = ext.lower()
    for category, extensions in FILE_TYPES.items():
        if ext in extensions:
            return category
    return 'Others'
def get_unique_destination(destination):
    """
    If a file with the same name already exists,
    create a new unique name like file_1.txt, file_2.txt.
    """
    if not os.path.exists(destination):
        return destination
    base, ext = os.path.splitext(destination)
    counter = 1
    while True:
        new_destination = f"{base}_{counter}{ext}"
        if not os.path.exists(new_destination):
            return new_destination
        counter += 1
def organize_files(folder_path):
    """
    Organizes files into category folders.
    """
    try:
        if not os.path.exists(folder_path):
            print("Error: Folder does not exist.")
            return
        if not os.path.isdir(folder_path):
            print("Error: The path is not a folder.")
            return
        print(f"\nOrganizing files in: {folder_path}")
        logging.info(f"Started organizing folder: {folder_path}")
        for item in os.listdir(folder_path):

            item_path = os.path.join(folder_path, item)
            if os.path.isdir(item_path) or item == 'file_organizer.log':
                continue
            category = get_category(item)
            category_folder = os.path.join(folder_path, category)
            os.makedirs(category_folder, exist_ok=True)
            destination = os.path.join(category_folder, item)
            destination = get_unique_destination(destination)
            shutil.move(item_path, destination)
            print(f"Moved: {item} -> {category}")
            logging.info(f"Moved {item} to {category}")
        print("\nOrganization completed successfully!")
        print("Log file created: file_organizer.log")
        logging.info("Organization completed successfully.")
    except PermissionError:
        print("Permission denied. Please run with proper access rights.")
        logging.exception("PermissionError occurred.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        logging.exception("Unexpected error occurred.")

def main():
    folder_path = input("Enter the folder path to organize: ").strip()
    if folder_path:
        organize_files(folder_path)
    else:
        print("No folder path entered.")
if __name__ == "__main__":
    main()