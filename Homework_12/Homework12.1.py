from bs4 import BeautifulSoup


import codecs


def delete_html_tags(html_file , result_file):
      with codecs.open(html_file, 'r', 'utf-8') as file:
           html = file.read()
      soup = BeautifulSoup(html,'lxml')
      extracted_text = soup.get_text()
      cleaned_text = '\n'.join([line.strip() for line in extracted_text.splitlines() if line.strip()])
      with open(result_file, 'w', encoding='utf-8') as txt_file:
          txt_file.write(cleaned_text)


delete_html_tags('draft.html', 'cleaned.txt')
