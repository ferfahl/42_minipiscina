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

def write_html_key(key, value, file_html):
    file_html.write('''
        
        <td style="border: 1px solid black; padding:10px">
        <h4>{}</h4> 
        <ul>
            <li>{}</li>
            <li>{}</li>
            <li>{}</li>
            <li>{}</li>
        </ul>
        </td>
        '''.format(key,
                        value[1],
                        value[2],
                        value[3],
                        value[4])) 

def periodic_table():
    file_html = open("periodic_table.html", "w")
    file_txt = open("periodic_table.txt", "r")
    # Reading the txt
    text_chem = file_txt.read().split("\n")
    text_chem.remove('')
    # Creating dict
    dict_chem = {}
    for line in text_chem:
        temp1 = line.split("=")
        temp_key = temp1[0]
        list_info = infos_chem(temp1[1])
        key = temp_key.strip()
        dict_chem[key] = list_info
    # Adding the input data to the HTML file
    file_html.write('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Periodic Table</title>
</head>
    <body>
    <h1>The Periodic Table of keys!</h1>  
    <table>
    <tr>
    ''')
    collumn_place = 0
    for key, value in dict_chem.items():
        if collumn_place == 18:
            collumn_place = 0
            file_html.write('''</tr>

            <tr>
            ''')
        while collumn_place < 18:
            temp_holder = int(value[0])
            if collumn_place == temp_holder:
                write_html_key(key, value, file_html)
                # file_html.write('''<td>key found! key:{} collumn{}</td>
                # '''.format(value[0], collumn_place))
                break
            else:
                # file_html.write('''<td>No key key:{} collumn{}</td>
                # '''.format(value[0], collumn_place))
                file_html.write('''
                <td></td>
            ''')
            collumn_place = collumn_place + 1
        collumn_place = collumn_place + 1
    file_html.write('''
    </table>
    </body>
    </html>''')
    # Saving the data into the HTML file
    file_html.close()

if __name__ == '__main__':
    periodic_table()
