import sys
import os

def check_args():
    if (len(sys.argv) != 2):
        sys.exit("Error: Wrong Number of Arguments, the program needs a '(name).template'")
    file_template = sys.argv[1]
    file_name = os.path.splitext(file_template)
    if (not file_template.endswith(".template")):
        sys.exit("Error: Invalid Extension")
    if not (os.path.isfile(file_template)):
        sys.exit("Error: File Not Found")
    return(file_name)

def render():
    try:
        file_name = check_args()
        file_html = open(file_name[0] + ".html", "w")
        file_template = open(sys.argv[1], "r")
        file_info = open("./settings.py", "r")
        # Reading info
        text_info = file_info.read().strip().split("\n")
        # Creating dict
        dict_info = {}
        for item in text_info:
            dict_info[item.split('=')[0].strip()] = item.split('=')[1].strip(' "')
        # Reading template
        template = file_template.read()
        # Adding the input data to the HTML file
        file_html.write('''<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Curricullum vitae</title>
        <style>
        table, th, td {
            border-color: #071381;
            border-style: solid;
            border-collapse: collapse;}
        </style>
    </head>
        <body>
        ''')
        file_html.write(template.format(**dict_info))
        file_html.write('''
        </body>
        </html>''')
        # Saving the data into the HTML file
        file_html.close()
    except KeyError:
            sys.exit("The template requires more information than provided")

if __name__ == '__main__':
    render()
