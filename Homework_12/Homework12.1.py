from bs4 import BeautifulSoup


import codecs


def delete_html_tags(html_file , result_file):
      with codecs.open(html_file, 'r', 'utf-8') as file:
           html = file.read()
      soup = BeautifulSoup(html,'lxml')
      extracted_text = soup.get_text()
      with open(result_file, 'w', encoding='utf-8') as txt_file:
          txt_file.write(extracted_text)


delete_html_tags('draft.html', 'cleaned.txt')
