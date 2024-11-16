import os
import argparse
from resume_parser import parse_resume
from spreadsheet_manager import add_to_spreadsheet

def main():
    parser = argparse.ArgumentParser(description='Resume Parser using pyresparser')
    parser.add_argument('input_folder', type=str, help='Folder containing resumes')
    # parser.add_argument('spreadsheet_path', type=str, help='Path to the spreadsheet', default='parsed_resumes.xlsx')

    args = parser.parse_args()

    # Ensure the input is a directory
    if not os.path.isdir(args.input_folder):
        print("The specified input is not a directory.")
        return

    # Iterate over files in the directory
    for filename in os.listdir(args.input_folder):
        file_path = os.path.join(args.input_folder, filename)
        
        # Ensure it's a file
        if os.path.isfile(file_path):
            print(f"Parsing {filename}...")
            try:
                resume_data = parse_resume(file_path)
                print(resume_data)
            except Exception as e:
                print(f"Error parsing {filename}: {e}")


if __name__ == '__main__':
    main()
