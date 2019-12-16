from docx import Document

def write_file(text, path_file):
  f = open(path_file, 'a')
  f.write(text)
  f.close()

# path_file = '/home/igzo/Documents/repositorios/investigacion/juslab/PROYECTO PANCHO/CONTRAVENCIONAL AUDIENCIA CONDENA 114 PENA EN SUSPENSO Proyecto.docx'
# fullText = read_file(path_file)
# final = '\n'.join(fullText)
# print(final)
