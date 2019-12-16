from file_reader import read_file, paragraphs_to_string
from text_classifier import classify
from text_replacer import replace
from file_creator import write_file
ext = '.docx'
file_name = 'OFICIOS PENAL REBELDIA PENAL'
file_path = './docs/'
input_file = file_path + file_name + ext
output_file = file_path + file_name + '-Anonimizado' + ext

text = paragraphs_to_string(read_file(input_file))
classifications = classify(text)
new_text = replace(text, classifications)
write_file(new_text, output_file)
