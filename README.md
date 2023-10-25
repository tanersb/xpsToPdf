
# XPS to PDF Converter

This Python script is designed to convert XPS files into PDF format using the [PyMuPDF](https://pypi.org/project/PyMuPDF/) library. It retrieves XPS files from a specified directory, processes each file, and saves the resulting PDF files in an output directory.

## Usage

1. Before running this script, you need to install the [PyMuPDF](https://pypi.org/project/PyMuPDF/) library. You can install the library with the following command: pip install PyMuPDF

2. To execute the script, use the following command:
python xpsToPdf.py

By default, the script processes all .xps files in the current directory and saves the resulting .pdf files in the same directory. You can modify the input and output directories by editing the `xps_dir` and `output_dir` variables within the script.

## Example

Here's an example of how to use this script to convert an XPS file to PDF:

```bash
python xpsToPdf.py

Requirements

    The PyMuPDF library must be installed.

Contribution

If you wish to contribute to this project, please submit pull requests or report any issues.

