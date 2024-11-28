import argparse
import os
import glob
import fitz # PyMuPDF
from PIL import Image
import re

Image.MAX_IMAGE_PIXELS = None


def convert_tiffs_to_pdf(input_dir, output_dir, pdf_mode, dpi, width, height):
    os.makedirs(output_dir, exist_ok=True)
    all_tifs = glob.glob(os.path.join(input_dir, '*.tif*'))

    tiffs = [f for f in all_tifs if re.match(r'.*\.tif(f)?$', f)]

    if not tiffs:
        print(f"No TIFF files found in the directory: {input_dir}")
        return

    if pdf_mode == 'unique':
        output_pdf = os.path.join(output_dir, "output.pdf")
        pdf_document = fitz.open()
        print(f"Generating single PDF at: {output_pdf}")

        for tiff in tiffs:
            process_tiff(tiff, pdf_document, dpi, width, height)
        pdf_document.save(output_pdf, deflate=False)
        pdf_document.close()
        print(f"Single PDF generated successfully: {output_pdf}")
    else:
        for tiff in tiffs:
            base_name = os.path.splitext(os.path.basename(tiff))[0]
            output_pdf = os.path.join(output_dir, f"{base_name}.pdf")
            pdf_document = fitz.open()
            print(f"Generating PDF for: {tiff}")
            process_tiff(tiff, pdf_document, dpi, width, height)
            pdf_document.save(output_pdf, deflate=False)
            pdf_document.close()
            print(f"PDF generated: {output_pdf}"
                  "\n----------"
                  )


def process_tiff(tiff, pdf_document, dpi, width, height):
    try:
        img = Image.open(tiff)
        page_index = 0

        while True:
            try:
                img.seek(page_index)
                page_index += 1

                rgb_image = img.convert("RGB")

                img_width, img_height = rgb_image.size
                page_width = width if width else img_width
                page_height = height if height else img_height
                rect = fitz.Rect(0, 0, page_width, page_height)

                temp_path = f"temp_page_{page_index}.png"
                rgb_image.save(temp_path, dpi=(dpi, dpi))
                page = pdf_document.new_page(width=rect.width, height=rect.height)
                page.insert_image(rect, filename=temp_path)
                os.remove(temp_path)
            except EOFError:
                break
    except Exception as e:
        print(f"Error processing {tiff}: {e}")


def main():
    parser = argparse.ArgumentParser(description="TIFF to PDF converter with configurable options.")
    parser.add_argument("-i", "--input", type=str, default=os.getcwd(), help="Input directory containing TIFF files.")
    parser.add_argument("-o", "--output", type=str, default=os.path.join(os.getcwd(), "output"), help="Output directory for generated PDFs.")
    parser.add_argument("-p", "--pdf", type=str, choices=["multiple", "unique"], default="multiple", help="PDF generation mode: 'multiple' for separate PDFs, 'unique' for a single PDF.")
    parser.add_argument("-d", "--dpi", type=int, default=300, help="Resolution (DPI) for images in the PDF.")
    parser.add_argument("-w", "--width", type=int, help="Page width in pixels.")
    parser.add_argument("-H", "--height", type=int, help="Page height in pixels.")

    args = parser.parse_args()

    print(f"Configured parameters:\n"
          f"Input directory: {args.input}\n"
          f"Output directory: {args.output}\n"
          f"PDF mode: {args.pdf}\n"
          f"DPI: {args.dpi}\n"
          f"Width: {args.width}\n"
          f"Height: {args.height}\n"
		  "----------")

    convert_tiffs_to_pdf(args.input, args.output, args.pdf, args.dpi, args.width, args.height)


if __name__ == "__main__":
    main()
