import pytesseract
from PIL import Image
from pdf2image import convert_from_path
import os

# Configurar o caminho do executável do Tesseract e o TESSDATA_PREFIX
pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"
os.environ["TESSDATA_PREFIX"] = "/usr/share/tesseract-ocr/5/"

def extract_text_from_image(image_path):
    """Extrai texto de uma imagem usando Tesseract OCR."""
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image, lang='por')  # 'por' para português
    return text

def extract_text_from_pdf(pdf_path, output_folder="output_images"):
    """Converte um PDF em imagens e extrai texto de cada página."""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Converter PDF para imagens
    pages = convert_from_path(pdf_path)
    text = ""

    for i, page in enumerate(pages):
        image_path = os.path.join(output_folder, f"page_{i + 1}.jpg")
        page.save(image_path, "JPEG")
        
        text += extract_text_from_image(image_path) + "\n\n"

    return text

if __name__ == "__main__":
    pdf_path = "arquivo.pdf"
    output_folder = "imagens_extraidas"

    print("Extraindo texto do PDF...")
    texto_extraido = extract_text_from_pdf(pdf_path, output_folder)

    with open("texto_extraido.txt", "w", encoding="utf-8") as f:
        f.write(texto_extraido)

    print("Texto extraído e salvo em 'texto_extraido.txt'.")
