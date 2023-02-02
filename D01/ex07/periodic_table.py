def clean_info(temp_info):
    temp3 = temp_info.split(":")
    temp4 = temp3[1]
    information = temp4.strip()
    return(information)

def infos_chem(temp):
    temp2 = temp.split(",")
    temp_collumn = temp2[0]
    collumn = clean_info(temp_collumn)
    temp_num = temp2[1]
    temp2_num = clean_info(temp_num)
    num = "No " + temp2_num
    temp_small = temp2[2]
    small = clean_info(temp_small)
    temp_mol = temp2[3]
    mol = clean_info(temp_mol)
    temp_ele = temp2[4]
    temp2_ele = clean_info(temp_ele)
    ele = temp2_ele + " electron"
    info_list = [collumn, num, small, mol, ele]
    return(info_list)

def test():
    file_html = open("demo.html", "w")
    file_txt = open("periodic_table.txt", "r")
    # Reading the txt
    text_chem = file_txt.read().split("\n")
    text_chem.remove('')
    #creating dict
    dict_chem = {}
    for line in text_chem:
        temp1 = line.split("=")
        temp_element = temp1[0]
        list_info = infos_chem(temp1[1])
        element = temp_element.strip()
        dict_chem[element] = list_info
    print(dict_chem)
    # Adding the input data to the HTML file
    file_html.write('''<html>
    <head>
    <title>HTML File</title>
    </head> 
    <body>
    <h1>Welcome Finxters</h1>           
    <p>Example demonstrating How to generate HTML Files in Python</p> 
    </body>
    </html>''')
    # Saving the data into the HTML file
    file_html.close()

if __name__ == '__main__':
    test()