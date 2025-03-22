import os
from datetime import datetime
from PyPDF2 import PdfReader, PdfWriter

def get_unique_filename(output_folder, loan_number, title, current_date):
    """
    Generates a unique filename by adding _1, _2, etc., if needed.
    """
    base_filename = f"{loan_number}_{title}_{current_date}"
    output_path = os.path.join(output_folder, f"{base_filename}.pdf")
    counter = 1

    # Check if file exists and append counter if needed
    while os.path.exists(output_path):
        output_path = os.path.join(output_folder, f"{base_filename}_{counter}.pdf")
        counter += 1

    return output_path


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

        # Construct the output file name with duplicate handling
        output_path = get_unique_filename(output_folder, loan_number, title, current_date)

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
        (3, 3): "report",
        (4, 4): "income",
        (5, 20): "income"
    }

    # Split the PDF based on the provided information
    split_pdf(input_pdf_path, output_folder, page_info, loan_number)

