# -*- coding: utf-8 -*-
# @Time    : 2022/6/17 00:38
# @Author  : Peilin Zhou
# @FileName: preprocess.py
# @Software: PyCharm
# @E-mail  : zhoupl@pku.edu.cn
import re
import emoji

def remove_urls(text):
    pattern = "http\S+"
    return re.sub(pattern,' ',text)
def add_spaces_to_emojis(text):
    # pattern = ":\w+:"
    pattern = ":[A-Za-z0-9-_]+:"
    return re.sub(pattern,' \g<0> ', text)
def add_spaces_for_punc(text,pos = 'all'):
    puncts = ['.','!','?','\'s',',',')','\'',"\"",'“','”','(','‘','/',':','…',';','’s','~','=','*','（','-','—']
    for punct in puncts:
        old_str = '{}'.format(punct)
        if pos == 'all':
            new_str = ' {} '.format(punct)
        elif pos == 'left':
            new_str = ' {}'.format(punct)
        elif pos == 'right':
            new_str = '{} '.format(punct)
        text = text.replace(old_str,new_str)
    return text
def remove_html_tags(text):
    pattern = r"""(?x)                              # Turn on free-spacing
      <[^>]+>                                       # Remove <html> tags
      | &([a-z0-9]+|\#[0-9]{1,6}|\#x[0-9a-f]{1,6}); # Remove &nbsp;
      """
    return re.sub(pattern,' ',text)
def preprocess(text):
    ## 移除url
    text = remove_urls(text)
    text = remove_html_tags(text)
    text = add_spaces_for_punc(text,pos = 'all')
    text = emoji.demojize(text)
    text = add_spaces_to_emojis(text)
    text = ' '.join(text.split())
    return text