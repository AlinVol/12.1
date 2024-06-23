import re


def clean_html(input_file, output_file="cleaned_text.txt"):
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    cleaned_content = re.sub(r'<[^>]+>', '', content)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(cleaned_content)


input_file = r'C:\Users\user\Downloads\draft.html'
output_file = r'C:\Users\user\Downloads\cleaned_text.txt'

clean_html(input_file, output_file)

with open(output_file, 'r', encoding='utf-8') as file:
    cleaned_text = file.read()

cleaned_text
