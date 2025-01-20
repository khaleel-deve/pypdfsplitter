# PDF Splitter

This Python script splits a multi-page PDF document into smaller PDFs based on specified page ranges and titles.

## Features

Splits a PDF into multiple PDFs based on page ranges.
Assigns user-defined titles to the output PDFs.
Handles errors gracefully, providing informative messages for invalid inputs or processing issues.
## Usage

Save the script as pdf_splitter.py
Open a terminal or command prompt and navigate to the directory containing the script.
Run the script using the following command,1 replacing the placeholders with your actual file paths and loan number:   
1.
github.com
github.com
python pdf_splitter.py --input_pdf_path /path/to/your/input.pdf --output_folder /path/to/output/folder --loan_number 12345 --page_info "(1, 1): 'asset', (2, 2): 'income', (3, 43): 'report'"
Explanation of arguments:

--input_pdf_path: Path to the PDF you want to split.
--output_folder: Path to the folder where you want to save the output PDFs.
--loan_number: A loan number or any other identifier to be included in the output filenames.
--page_info: A dictionary defining page ranges and titles for the output PDFs. The format is (start_page, end_page): 'title', separated by commas for multiple entries.
## Example

Let's say you have a 43-page PDF document containing loan application sections. You want to split it into three separate PDFs:

Pages 1 (cover page) titled "Asset"
Page 2 (income statement) titled "Income"
Pages 3-43 (loan report) titled "Report"
Here's the command you would use:

python pdf_splitter.py --input_pdf_path loan_application.pdf --output_folder output_pdfs --loan_number L12345 --page_info "(1, 1): 'Asset', (2, 2): 'Income', (3, 43): 'Report'"
This will create three PDFs in the output_pdfs folder named L12345_Asset_YYYYMMDD.pdf, L12345_Income_YYYYMMDD.pdf, and L12345_Report_YYYYMMDD.pdf (where YYYYMMDD is the current date).

## Additional Notes

The script assumes the PyPDF2 library is installed. You can install it using pip install PyPDF2.
Make sure you have permission to read the input PDF and write to the output folder.
