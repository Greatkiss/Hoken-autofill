import pandas as pd
from input_reconfirm import jygs_name_input, jygs_num_input, reconfirm, reconfirm_num, kysh_name_input, reconfirm_name, kysh_num_input, kysh_reconfirm_num

class kysh:
    def __init__(self):
        self.hiho = [""]*3
        self.kubun = ""
        self.name_kana = [""]*2
        self.name_kanji = [""]*2
        self.sex = ""
        self.birth = [""]*4
        self.getdate = [""]*4
        self.tin = [""]*2
        self.bikou = ""

    def type_info(self):
        num0, num1, num2=jygs_num_input("被保険者番号")
        num0, num1, num2=reconfirm_num("被保険者番号", num0, num1, num2)
        self.hiho[0] = num0
        self.hiho[1] = num1
        self.hiho[2] = num2

        kubun =jygs_name_input("取得区分（1:新規、2:継続）")
        kubun = reconfirm("取得区分（1:新規、2:継続）", kubun)
        self.kubun = kubun

        kana=kysh_name_input("ﾐｮｳｼﾞ ﾅﾏｴ")
        kana=reconfirm_name("ﾐｮｳｼﾞ ﾅﾏｴ", kana)
        self.name_kana = kana

        kanji=kysh_name_input("苗字　名前")
        kanji=reconfirm_name("苗字　名前", kana)
        self.name_kanji = kanji

        sex =jygs_name_input("性別")
        sex = reconfirm("s性別", sex)
        self.sex = sex

        num0, num1, num2, num3=kysh_num_input("生年月日")
        num0, num1, num2, num3=kysh_reconfirm_num("生年月日", num0, num1, num2, num3)
        self.birth[0] = num0
        self.birth[1] = num1
        self.birth[2] = num2
        self.birth[3] = num3

        num0, num1, num2, num3=kysh_num_input("資格取得日")
        num0, num1, num2, num3=kysh_reconfirm_num("資格取得日", num0, num1, num2, num3)
        self.getdate[0] = num0
        self.getdate[1] = num1
        self.getdate[2] = num2
        self.getdate[3] = num3

        tingin=kysh_name_input("1 space 賃金（千円）")
        tingin=reconfirm_name("1 space 賃金（千円）", tingin)
        self.tin = tingin
