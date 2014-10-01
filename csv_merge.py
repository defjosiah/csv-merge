#Markdown Replacement
#Josiah Grace 

"""
Given a markdown template and a spreadsheet, for each row of the spreadsheet
replace the markdown template column names "<Column Name>" with that row's 
information. Then run these through pandoc with any specified CSS, convert 
to pdf and save in one document. 

HTML markdown with specific css:
    pandoc -c avenir-white.css test.md -o test.pdf

Regex for string replacement: 
    re = <\w+>
"""

import os
import sys
import re

def parse_csv(input_form):
    """
    Turn an input csv into two lists, header and info, which contains the 
    rest of the rows. 
    """
    info = []
    with open(input_form, 'rb') as csvfile:
        for index, row in enumerate(csvfile):
            if index == 0:
                header = row.rstrip().split(",")
            else:
                info.append(row.rstrip().split(","))
    return (header, info) 
            
def replace_template(template_file, info_tuple):
    header = info_tuple[0]
    info = info_tuple[1]
    output_string = ""

    #echo the template file, with "<Name>" replaced
    with open(template_file, 'r') as temp_file:
        text = temp_file.read()
    
    for row in info:
        output = text
        for index, entry in enumerate(header): 
            output = re.sub(r"<{0}>".format(entry), row[index], output)
        print output

def main():
    template = sys.argv[1]
    data_file = sys.argv[2]
    replace_template(template, parse_csv(data_file))


if __name__ == '__main__':
    main()
