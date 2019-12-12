from file_reader import read_file
from text_classifier import classify
from text_replacer import replace

file_name = "/home/natalia/Desktop/programacion/justlab/git/juslab/VISU CONTRAVENCIONAL TESTADO.docx"

text = read_file(file_name)
final = '\n'.join(text)

classification = classify(final)

print(classification)