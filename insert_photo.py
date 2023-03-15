from docxtpl import DocxTemplate, InlineImage
from docx.shared import Mm
import os

document = DocxTemplate('.\\PLANTILLAS\\plantilla.docx')

imagen_cif = InlineImage(document, image_descriptor='.\\CLIENTES\\A\\12345A\\cif.jpg', \
    width=Mm(150), height=Mm(100))

context = {'cif': imagen_cif}

document.render(context)

# Save the document
document.save(".\\TEMP\\output.docx")