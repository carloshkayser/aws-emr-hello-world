from loremipsum import get_paragraphs, get_sentences, get_sentence

import sys
import re

# https://stackoverflow.com/questions/50133478/byte-prefix-in-python-string
def fix_loremipsum(loremipsum_string):
    loremipsum_string = re.sub("B'(.*?)'", lambda x: x.group(1).title(), loremipsum_string)
    loremipsum_string = re.sub("b'(.*?)'", lambda x: x.group(1), loremipsum_string)
    return loremipsum_string

if __name__ == "__main__":
    
    paragraphs = int(sys.argv[1])
    
    print('Generating dataset of {0}'.format(paragraphs))

    paragraphs_list = get_paragraphs(paragraphs)

    len(paragraphs_list)

    with open(sys.argv[2], 'w') as f:
        for paragraph in paragraphs_list:
            paragraph = fix_loremipsum(paragraph)
            f.write("%s\n" % paragraph)
            
# python lorem-ipsim-generator.py <number-of-paragraphs> <output-file-name>