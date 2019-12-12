from docx import Document

def read_file(path_file, format = 'docx'):
  f = open(path_file, 'r')
  fullText = []
  if format == 'docx':
    document = Document(path_file)
    for para in document.paragraphs:
        fullText.append(para.text)
  else:
    fullText = [f.read()]
  f.close()
  return fullText