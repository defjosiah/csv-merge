csv-merge
==============

## Overview

csv-merge takes a markdown template (though technically you could use any text
based language e.g. LaTeX, plain text, etc), and merges an input spreadsheet 
with the template. 

Template: 

```
## <name>

####Roommate
> <roommate> 

####Room Number
> <room_number>

<div class="pagebreak"></div>
``` 

Spreadsheet:

| name          | roommate           | room_number |
| ------------- |:------------------:| -----------:|
| Bob           | right-aligned      |     3       |
| John          | centered           |     9       |
| Jackie        | are neat           |    11       |

And merges them together into a markdown file with a per row replacement for the 
column names wherever there is an angle bracket in the template. 

Generally, this output is run through "pandoc" with css in order to make it 
look pretty and output to a pdf. e.g. 

> $ python csv_merge.py | pandoc -c css/something.css -o combined.html

I'm sure something similar exists, but this is simple, and effective. 
