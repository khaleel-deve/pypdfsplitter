import os
from datetime import datetime
from PyPDF2 import PdfReader, PdfWriter

def split_pdf(input_pdf_path, output_folder, page_info, loan_number):
    """
    Splits a PDF into smaller PDFs based on specified page ranges and titles.

    Parameters:
        input_pdf_path (str): Path to the input PDF.
        output_folder (str): Folder where the output PDFs will be saved.
        page_info (dict): Dictionary where keys are tuples representing page ranges (1-based),
                          and values are document titles.
        loan_number (str): Loan number provided by the user.

    Returns:
        None
    """
    # Read the input PDF
    try:
        pdf_reader = PdfReader(input_pdf_path)
        total_pages = len(pdf_reader.pages)
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Get the current date in mmddyyyy format
    current_date = datetime.now().strftime("%m%d%Y")

    # Process each page range based on the dictionary
    for page_range, title in page_info.items():
        start, end = page_range
        if start < 1 or end > total_pages or start > end:
            print(f"Skipping invalid page range: {page_range}")
            continue

        # Extract the specified page range and write to a new PDF
        pdf_writer = PdfWriter()
        for page_num in range(start - 1, end):  # Convert to 0-based index
            pdf_writer.add_page(pdf_reader.pages[page_num])

        # Construct the output file name
        output_filename = f"{loan_number}_{title}_{current_date}.pdf"
        output_path = os.path.join(output_folder, output_filename)

        try:
            with open(output_path, "wb") as output_file:
                pdf_writer.write(output_file)
            print(f"Saved: {output_path}")
        except Exception as e:
            print(f"Error saving PDF {output_path}: {e}")

if __name__ == "__main__":
    # Input PDF path
    input_pdf_path = input("Enter the path to the input PDF: ").strip()

    # Output folder
    output_folder = input("Enter the folder path to save the output PDFs: ").strip()

    # Loan number
    loan_number = input("Enter the loan number: ").strip()

    # Dictionary of page ranges and titles
    # Example: (1, 1) -> "asset", (2, 2) -> "income", (3, 43) -> "report"
    page_info = {
        (1, 1): "asset",
        (2, 2): "income",
        (3, 43): "report"
    }

    # Split the PDF based on the provided information
    split_pdf(input_pdf_path, output_folder, page_info, loan_number)
