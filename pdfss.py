import PyPDF2
import os

merger = PyPDF2.PdfMerger()

pdf_directory = "C:/Users/agust/.vscode/pdfs"  # Ruta de la carpeta que contiene los archivos PDF

for file in os.listdir(pdf_directory):
    if file.endswith(".pdf"):
        file_path = os.path.join(pdf_directory, file)  # Combina la ruta del directorio con el nombre de archivo
        merger.append(file_path)  # Agrega el archivo al objeto merger para combinarlos

output_file = os.path.join(pdf_directory, "nuevo.pdf") 
merger.write(output_file)
merger.close()

print("Nuevo PDF:", output_file)


# IMPORTANTE los PDF que se quieran combinar, deben de estar en la misma carpeta que este codigo