import pandas as pd
from openpyxl import Workbook

# Constants for the spreadsheet columns based on the provided table
SPREADSHEET_COLUMNS = [
    'File Name', 'Name', 'Email', 'Phone', 'Location',
    'Role/Title', 'Education', 'Skills', 'Experience',
    'Work Authorization', 'LinkedIn URL'
]

def create_spreadsheet(spreadsheet_path='parsed_resumes.xlsx'):
    # Create a workbook and select the active worksheet
    wb = Workbook()
    ws = wb.active

    # Write the column headers
    ws.append(SPREADSHEET_COLUMNS)

    # Save the workbook to the specified path
    wb.save(spreadsheet_path)

def add_to_spreadsheet(parsed_data, spreadsheet_path='parsed_resumes.xlsx'):
    # Load the existing spreadsheet or create a new one if it doesn't exist
    try:
        df = pd.read_excel(spreadsheet_path)
    except FileNotFoundError:
        df = pd.DataFrame(columns=SPREADSHEET_COLUMNS)
        df.to_excel(spreadsheet_path, index=False)

    # Append the new data to the dataframe
    new_row = {col: parsed_data.get(col, '') for col in SPREADSHEET_COLUMNS}
    df = df.append(new_row, ignore_index=True)
    
    # Ensure the spreadsheet does not exceed 100,000 lines
    if len(df) > 100000:
        raise ValueError("The spreadsheet has exceeded the limit of 100,000 lines.")
    
    # Save the updated dataframe back to the spreadsheet
    df.to_excel(spreadsheet_path, index=False)

