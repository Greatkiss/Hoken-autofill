import openpyxl as xl

def fill_date(birth_l):
    birth = [""]*6
    l=""
    if(int(birth_l[1]) < 10):
        birth[0] = "0"
        birth[1] = birth_l[1][1]
    else:
        bl=birth_l[1]
        birth[0] = bl[0]
        birth[1] = bl[1]

    if(int(birth_l[2]) < 10):
        birth[2] = "0"
        birth[3] = birth_l[2][1]
    else:
        bl=birth_l[2]
        birth[2] = bl[0]
        birth[3] = bl[1]

    if(int(birth_l[3]) < 10):
        birth[4] = "0"
        birth[5] = birth_l[3][1]
    else:
        bl=birth_l[3]
        birth[4] = bl[0]
        birth[5] = bl[1]
    return birth
    
def fill_shaho(jygs, kysh):
    book = xl.load_workbook("shaho_temp.xlsx")
    sheet = book["Sheet1"]
    sheet['H7'] = jygs.seirinum[0]

    sheet['T7'] = jygs.seirinum[1]

    sheet['AJ7'] = jygs.shahonum
    
    sheet['J12'] = jygs.postnum[0]
    sheet['R12'] = jygs.postnum[1]
    sheet['H13'] = jygs.address
    sheet['H17'] = jygs.name
    sheet['M25'] = jygs.phone[0]
    sheet['Y25'] = jygs.phone[1]
    sheet['AK25'] = jygs.phone[2]

    sheet['AB28'] = kysh.name_kana[0]
    sheet['AW28'] = kysh.name_kana[1]
    sheet['AB30'] = kysh.name_kanji[0]
    sheet['AW30'] = kysh.name_kanji[1]
    birth = fill_date(kysh.birth)
    sheet['CB28'] = birth[0]
    sheet['CE28'] = birth[1]
    sheet['CH28'] = birth[2]
    sheet['CK28'] = birth[3]
    sheet['CN28'] = birth[4]
    sheet['CQ28'] = birth[5]

    sheet['H36'] = kysh.kojin[0]
    sheet['K36'] = kysh.kojin[1]
    sheet['N36'] = kysh.kojin[2]
    sheet['Q36'] = kysh.kojin[3]
    sheet['T36'] = kysh.kojin[4]
    sheet['W36'] = kysh.kojin[5]
    sheet['Z36'] = kysh.kojin[6]
    sheet['AC36'] = kysh.kojin[7]
    sheet['AF36'] = kysh.kojin[8]
    sheet['AI36'] = kysh.kojin[9]
    sheet['AL36'] = kysh.kojin[10]
    sheet['AO36'] = kysh.kojin[11]

    shutoku = fill_date(kysh.lostdate)
    sheet['AY36'] = shutoku[0]
    sheet['BB36'] = shutoku[1]
    sheet['BE36'] = shutoku[2]
    sheet['BH36'] = shutoku[3]
    sheet['BK36'] = shutoku[4]
    sheet['BN36'] = shutoku[5]
    #未実装
    lost = fill_date(kysh.lostdate)
    sheet['CE36'] = lost[0]
    sheet['CI36'] = lost[1]
    sheet['CM36'] = lost[2]

    book.save('取得届_{}.xlsx'.format(kysh.name_kanji[0]))