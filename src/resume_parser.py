# This is resume_parser.py
from pyresparser import ResumeParser
import os

def parse_resume(resume_path):
    if not os.path.exists(resume_path):
        raise FileNotFoundError(f"The resume file at {resume_path} was not found.")
    
    # Parse the resume file using pyresparser
    resume_data = ResumeParser(resume_path).get_extracted_data()
    return resume_data
