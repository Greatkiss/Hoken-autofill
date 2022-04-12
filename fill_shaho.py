import openpyxl as xl

def fill_shaho(jygs, kysh):
    book = xl.load_workbook("shaho_temp.xlsx")
    sheet = book["Sheet1"]
    sheet['T8'] = jygs.seirinum[0][0]
    sheet['W8'] = jygs.seirinum[0][1]

    l = jygs.seirinum[1]
    sheet['AB8'] = l[0]
    sheet['AE8'] = l[1]
    sheet['AH8'] = l[2]
    #sheet['AK8'] = l[3]

    sheet['AV8'] = jygs.shahonum[0]
    sheet['AZ8'] = jygs.shahonum[1]
    sheet['BD8'] = jygs.shahonum[2]
    sheet['BH8'] = jygs.shahonum[3]
    sheet['BL8'] = jygs.shahonum[4]
     
    sheet['R17'] = jygs.postnum[0]
    sheet['AA17'] = jygs.postnum[1]
    sheet['N20'] = jygs.address
    sheet['N31'] = jygs.name
    sheet['V49'] = jygs.phone[0]
    sheet['AH49'] = jygs.phone[1]
    sheet['AX49'] = jygs.phone[2]

    sheet['AB55'] = kysh.name_kana[0]
    sheet['AZ55'] = kysh.name_kana[1]
    sheet['AB58'] = kysh.name_kanji[0]
    sheet['AZ58'] = kysh.name_kanji[1]
    birth = fill_date(kysh.birth)
    sheet['CJ55'] = birth[0]
    sheet['CM55'] = birth[1]
    sheet['CP55'] = birth[2]
    sheet['CS55'] = birth[3]
    sheet['CV55'] = birth[4]
    sheet['CY55'] = birth[5]

    sheet['AB65'] = kysh.kojin[0]
    sheet['AF65'] = kysh.kojin[1]
    sheet['AJ65'] = kysh.kojin[2]
    sheet['AN65'] = kysh.kojin[3]
    sheet['AR65'] = kysh.kojin[4]
    sheet['AV65'] = kysh.kojin[5]
    sheet['AZ65'] = kysh.kojin[6]
    sheet['BD65'] = kysh.kojin[7]
    sheet['BH65'] = kysh.kojin[8]
    sheet['BL65'] = kysh.kojin[9]
    sheet['BP65'] = kysh.kojin[10]
    sheet['BT65'] = kysh.kojin[11]

    shutoku = fill_date(kysh.getdate)
    sheet['CJ65'] = shutoku[0]
    sheet['CM65'] = shutoku[1]
    sheet['CP65'] = shutoku[2]
    sheet['CS65'] = shutoku[3]
    sheet['CV65'] = shutoku[4]
    sheet['CY65'] = shutoku[5]

    gekyu = int(kysh.tin[0])
    sheet['S74'] = gekyu*1000

    book.save('shaho_filled.xlsx')

def fill_date(birth_l):
    birth = [""]*6
    l=""
    if(int(birth_l[1]) < 10):
        birth[0] = "0"
        birth[1] = birth_l[1]
    else:
        bl=birth_l[1]
        birth[0] = bl[0]
        birth[1] = bl[1]

    if(int(birth_l[2]) < 10):
        birth[2] = "0"
        birth[3] = birth_l[2]
    else:
        bl=birth_l[2]
        birth[2] = bl[0]
        birth[3] = bl[1]

    if(int(birth_l[3]) < 10):
        birth[4] = "0"
        birth[5] = birth_l[3]
    else:
        bl=birth_l[3]
        birth[4] = bl[0]
        birth[5] = bl[1]
    return birth