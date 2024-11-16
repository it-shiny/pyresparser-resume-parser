# Resume Parsing Utility

This utility parses individual resumes and extracts important information such as name, contact details, skills, experience, and education.

## Prerequisites

Before you run the parser, ensure you have the following installed:

- Python 3.7
- pip (Python package installer)
- Virtual Environment (recommended)

## Installation

To set up the project and install the required dependencies, follow these steps:


1. **Create a virtual environment** (recommended) to isolate the project dependencies:

    ```
    python -m venv venv
    ```

2. **Activate the virtual environment**:

- On Windows:

  ```
  venv\Scripts\activate
  ```

- On MacOS/Linux:

  ```
  source venv/bin/activate
  ```


3. **Install the required packages**:

    ```
    pip install -r requirements.txt
    ```

## Post-installation Setup

After installing the required packages, you need to perform a one-time download of the `stopwords` dataset from `nltk`:

1. Open a Python interpreter by typing `python` in your terminal or command prompt.

2. Run the following commands within the Python interpreter:

   ```python
   import nltk
   nltk.download('stopwords')

## Patching Libraries

Due to some version conflicts with the `pdfminer` package, you may need to modify a line in the package's `__init__.py` file.

Follow these steps:

1. Navigate to your virtual environment's site-packages directory:

    ```
    cd path_to_your_virtualenv\Lib\site-packages\pdfminer
    ```

2. Open the `__init__.py` file in a text editor.

3. Locate the following line:

    ```python
    from importlib.metadata import version, PackageNotFoundError
    ```

4. Replace it with:

    ```python
    try:
        from importlib.metadata import version, PackageNotFoundError
    except ImportError:
        from importlib_metadata import version, PackageNotFoundError
    ```

5. Save the file

Advise users to revert any manual changes if they update the `pdfminer` package later, as the updated package might already contain the fix for the version conflict.



## Usage

To run the resume parser, navigate to the `src` directory and execute `main.py` with the required arguments.

python main.py <input_folder>

- `<input_folder>` is the path to the folder containing the resumes you want to parse.


### Example:

python main.py ../data/

This command will parse all resumes in the `../data/` directory and output as JSON.


## Output

The parsed resume data will be saved in an Excel spreadsheet with the following columns:

- File Name
- Name
- Email
- Phone
- Location
- Role/Title
- Education
- Skills
- Experience
- Work Authorization
- LinkedIn URL

Each row in the spreadsheet corresponds to a single resume.

## Troubleshooting

If you encounter any issues while running the utility, ensure that:

- You're in the correct directory.
- The virtual environment is activated.
- The input folder exists and contains resume files.
- You have write permissions for the output file path.



