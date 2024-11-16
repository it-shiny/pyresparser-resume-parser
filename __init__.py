import argparse
import os
import shutil
from datetime import datetime
import pandas as pd
from pdfminer import high_level
import docx

# Function to extract text from a docx file
def extract_text_from_docx(docx_path):
    doc = docx.Document(docx_path)
    return " ".join([para.text for para in doc.paragraphs])

# Function to extract text from a pdf file
def extract_text_from_pdf(pdf_path):
    return high_level.extract_text(pdf_path)

# Function to process a resume and extract information
def parse_resume(file_path):
    # Determine the file extension and call the appropriate function
    file_ext = os.path.splitext(file_path)[1].lower()
    text = ""
    if file_ext == '.docx':
        text = extract_text_from_docx(file_path)
    elif file_ext == '.pdf':
        text = extract_text_from_pdf(file_path)
    # Here, you would add your parsing logic or an external API call
    return {
        'Name': 'Extracted Name',  # Replace with actual extraction logic
        'Email': 'Extracted Email',  # Replace with actual extraction logic
        # ... other fields ...
    }

# Function to update the spreadsheet
def update_spreadsheet(resume_data, spreadsheet_path='resume_data.xlsx'):
    # Load existing data or initialize new DataFrame
    if os.path.exists(spreadsheet_path):
        df = pd.read_excel(spreadsheet_path)
    else:
        df = pd.DataFrame(columns=resume_data.keys())
    # Append new data and save
    df = df.append(resume_data, ignore_index=True)
    df.to_excel(spreadsheet_path, index=False)

# Function to archive processed documents
def archive_document(file_path):
    archive_folder = 'archive'
    if not os.path.exists(archive_folder):
        os.makedirs(archive_folder, exist_ok=True)
    # Generate today's archive subfolder
    today_folder = datetime.now().strftime('%Y-%m-%d')
    today_path = os.path.join(archive_folder, today_folder)
    if not os.path.exists(today_path):
        os.makedirs(today_path, exist_ok=True)
    # Move file to today's archive folder
    shutil.move(file_path, os.path.join(today_path, os.path.basename(file_path)))

# Main function that ties everything together
def main(input_folder):
    for file in os.listdir(input_folder):
        if file.lower().endswith(('.docx', '.pdf')):
            print(f'Processing file: {file}')
            file_path = os.path.join(input_folder, file)
            resume_data = parse_resume(file_path)
            update_spreadsheet(resume_data)
            archive_document(file_path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Resume Parsing Utility')
    parser.add_argument('input_folder', type=str, help='Input folder containing resumes')
    args = parser.parse_args()
    main(args.input_folder)
