import cv2
import pytesseract

#OCR (Reconhecimento Óptico de Caracteres)

pytesseract.pytesseract.tesseract_cmd = r'G:/Códigos/Tesseract/tesseract.exe'

def extracao_texto(path_imagem):
    #carregar a imagem utilizando OpenCV
    imagem = cv2.imread(path_imagem)

    # Converter a imagem para escala de cinza, pois o tesseract funciona melhor em escala de cinza
    gray_image = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    # Realizar a binarização da imagem (opcional)
    _, binarized_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    # Extrair texto usando Tesseract OCR
    texto_extraido = pytesseract.image_to_string(binarized_image)
    
    return texto_extraido

if __name__ == "__main__":
    image_path = "Imagens/noticia.jpg" 
    texto_extraido = extracao_texto(image_path)
    print("Texto extraído:")
    print(texto_extraido)