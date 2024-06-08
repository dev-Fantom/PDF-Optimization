import argparse
import subprocess

output_pdf_path = "outputs/compress.pdf"


def compress_pdf(input_pdf_path, quality):
    quality_settings = {
        'screen': '72',
        'ebook': '150',
        'printer': '300',
        'prepress': '300',
        'default': '300'
    }

    if quality not in quality_settings:
        quality = 'default'

    ghostscript_command = [
        'gs', '-sDEVICE=pdfwrite', '-dCompatibilityLevel=1.4',
        '-dPDFSETTINGS=/{}/'.format(quality), '-dNOPAUSE', '-dQUIET',
        '-dBATCH', '-sOutputFile={}'.format(output_pdf_path),
        input_pdf_path
    ]

    subprocess.run(ghostscript_command)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Compress a PDF using Ghostscript')
    parser.add_argument('input_pdf_path', help='Path to the input PDF')
    parser.add_argument('quality', help='Quality of the PDF compression (screen, ebook, printer, prepress, default)')

    args = parser.parse_args()

    compress_pdf(args.input_pdf_path, args.quality)
