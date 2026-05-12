# Automated File Organizer

## Overview
The **Automated File Organizer** is a robust Python utility designed to declutter your workspace by automatically categorizing and moving files into dedicated folders based on their extensions. Developed as part of the InternSpark internship (Task 1), this tool helps maintain a clean and organized directory structure with minimal effort.

## Key Features
- **Smart Categorization**: Automatically identifies and groups files into categories:
  - 🖼️ **Images**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`
  - 📄 **Documents**: `.pdf`, `.doc`, `.docx`, `.txt`, `.ppt`, `.xls`, etc.
  - 🎵 **Audio**: `.mp3`, `.wav`, `.aac`
  - 🎥 **Videos**: `.mp4`, `.mkv`, `.avi`, `.mov`
  - 📦 **Archives**: `.zip`, `.rar`, `.7z`
  - 📁 **Others**: Any other file types.
- **Conflict Resolution**: Smartly renames files if a duplicate exists in the destination folder (e.g., `report.pdf` becomes `report_1.pdf`).
- **Activity Logging**: Maintains a detailed `file_organizer.log` to track all file movements and errors.
- **Safe Execution**: Skips directories and its own log file to prevent recursive loops or accidental moves.

## Prerequisites
- **Python 3.x**
- No external libraries required (uses standard `os`, `shutil`, and `logging` modules).

## How to Use
1. **Clone/Download** the repository.
2. **Run the script**:
   ```bash
   python Task1.py
   ```
3. **Provide the Path**: Enter the absolute path of the folder you wish to organize when prompted.
   - Example: `C:\Users\Name\Downloads\UnorganizedFolder`
4. **Relax**: The script will instantly create category folders and move your files.

## Screenshots
Refer to the `Screenshots/` folder for visual demonstrations of the script in action:
- `code_screenshot.png`: The implementation of the script.
- `input_screenshot.png`: Providing the folder path to organize.
- `before_execution.png`: The state of the folder before organization.
- `after_execution.png`: The organized folder structure.
- `output_screenshot.png`: Terminal output showing success.

## Project Structure
- `Screenshots/`: Folder containing project demonstrations.
- `Task1.py`: The core automation script.
- `Task_1.pdf`: Task requirements and documentation.
- `file_organizer.log`: Log file generated during execution.
- `README.md`: This documentation.

## Logging & Debugging
The application generates a `file_organizer.log` in the same directory. It records:
- Timestamp of operations.
- Successful file moves.
- Errors (e.g., permission issues, invalid paths).

## License
This project is for educational purposes as part of the InternSpark internship program.
