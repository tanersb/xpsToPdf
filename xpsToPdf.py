import fitz  # PyMuPDF
import os


xps_dir = "."
output_dir = "."


xps_files = [f for f in os.listdir(xps_dir) if f.endswith(".xps")]

for xps_file in xps_files:

    xps_file_path = os.path.join(xps_dir, xps_file)


    pdf_file = os.path.splitext(xps_file)[0] + ".pdf"
    pdf_file_path = os.path.join(output_dir, pdf_file)

    doc = fitz.open(xps_file_path)
    pdf_bytes = doc.convert_to_pdf()

    with open(pdf_file_path, "wb") as pdf_out:
        pdf_out.write(pdf_bytes)

    print(f"{xps_file} dosyası {pdf_file} dosyasına dönüştürüldü.")
