import pandas as pd
from input_reconfirm import jygs_name_input, jygs_num_input, reconfirm, reconfirm_num, kysh_name_input, reconfirm_name, kysh_num_input, kysh_reconfirm_num
import os
import openpyxl as xl

class kysh:
    def __init__(self):
        self.hiho = [""]*3
        self.kubun = ""
        self.name_kana = [""]*2
        self.name_kanji = [""]*2
        self.sex = ""
        self.birth = [""]*4
        self.getdate = [""]*4
        self.tin = ""
        self.carfare = ""
        self.bikou = ""
        self.kojin = ""

    def type_info(self):
        kubun =jygs_name_input("取得区分（1:新規、2:再取得）")
        kubun = reconfirm("取得区分（1:新規、2:再取得）", kubun)
        self.kubun = kubun
        if(kubun == "2"):
            num0, num1, num2=jygs_num_input("被保険者番号")
            num0, num1, num2=reconfirm_num("被保険者番号", num0, num1, num2)
            if(len(num0)+len(num1)+len(num2) == 0):
                bikou = jygs_name_input("備考-前職")
                bikou = reconfirm("備考-前職",bikou)
                self.bikou = bikou
            else:
                self.hiho[0] = num0
                self.hiho[1] = num1
                self.hiho[2] = num2
        kojin = jygs_name_input("個人番号")
        kojin = reconfirm("個人番号", kojin)
        self.kojin = kojin

        kana=kysh_name_input("ﾐｮｳｼﾞ ﾅﾏｴ")
        kana=reconfirm_name("ﾐｮｳｼﾞ ﾅﾏｴ", kana)
        self.name_kana = kana

        kanji=kysh_name_input("苗字　名前")
        kanji=reconfirm_name("苗字　名前", kanji)
        self.name_kanji = kanji

        sex =jygs_name_input("性別（1:男，2:女）")
        sex = reconfirm("性別（1:男，2:女）", sex)
        self.sex = sex

        num0, num1, num2, num3=kysh_num_input("生年月日（2:大正，3:昭和，4:平成，5:令和）")
        num0, num1, num2, num3=kysh_reconfirm_num("生年月日（gg-yy-mm-dd）", num0, num1, num2, num3)
        self.birth[0] = num0
        self.birth[1] = num1
        self.birth[2] = num2
        self.birth[3] = num3

        num0, num1, num2, num3=kysh_num_input("資格取得日（4:平成，5:令和）")
        num0, num1, num2, num3=kysh_reconfirm_num("資格取得日（gg-yy-mm-dd）", num0, num1, num2, num3)
        self.getdate[0] = num0
        self.getdate[1] = num1
        self.getdate[2] = num2
        self.getdate[3] = num3

        tingin=kysh_name_input("月給 space 交通費(千円)")
        tingin=reconfirm_name("月給 space 交通費(千円)", tingin)
        self.tin = tingin
    def load_info(self):
        print("被保険者の列数を入力(kysh_info.xlxsを参照)")
        n = int(input())
        book = xl.load_workbook("kysh_info.xlsx")
        sheet = book["Sheet1"]
        self.hiho = cell_to_list(sheet.cell(row=n,column=3).value)
        self.kojin = str(sheet.cell(row=n,column=4).value)
        self.kubun = str(sheet.cell(row=n,column=5).value)
        self.sex = str(sheet.cell(row=n,column=6).value)
        self.birth = cell_to_list(str(sheet.cell(row=n,column=7).value))
        self.getdate = cell_to_list(str(sheet.cell(row=n,column=8).value))
        self.tin = str(sheet.cell(row=n,column=9).value)
        self.carfare = str(sheet.cell(row=n,column=10).value)
        self.bikou = str(sheet.cell(row=n,column=11).value)
        self.name_kana = cell_to_name(str(sheet.cell(row=n,column=2).value))
        self.name_kanji = cell_to_name(str(sheet.cell(row=n,column=1).value))


def cell_to_list(cell_data):
    if(str(cell_data).find('-')):
        l = str(cell_data).split('-')
    elif(cell_data.find(' ')):
        l = str(cell_data).split(' ')
    return l


def cell_to_name(cell_data):
    print(cell_data)
    if(str(cell_data).find('-')>0):
        l = str(cell_data).split('-')
    elif(str(cell_data).find(' ')>0):
        l = str(cell_data).split(' ')
    elif(str(cell_data).find('　')>0):
        l = str(cell_data).split('　')
    else:
        print("error")
        return -1
    
    if(len(l) < 3):
        return l
    else:
        l_foreign = [""]*2
        l_foreign[0] = l[0]
        l.pop(0)
        l_foreign[1] = ' '.join(l)
        return l_foreign