import requests
import mojimoji

class fill_koho_class:
    @staticmethod
    def fill_koho(kysh, jygs):
        session = requests.session()
        url_login = "https://hoken.hellowork.mhlw.go.jp/assist/001000.do?screenId=001000&action=koyohohiSoshitsuLink"
        res = session.get(url_login)
        res.raise_for_status()
        response_cookie = res.cookies
        #check box
        info = {
            "chkDoi": "1",
            "inputPrintButton": "内容を入力して印刷",
            "reportTypeHidden": "KOYOHOHISOSHITSU",
            "inputHidden": "1",
            "screenId": "001010",
            "maba_vrbs": "commonDownload,inputPrintButton",
        }
        login_url = "https://hoken.hellowork.mhlw.go.jp/assist/001010.do"
        response = session.post(login_url, data=info, cookies=response_cookie)
        response.raise_for_status()
        #data input
        info_send={
            "txtHhksNo1": mojimoji.zen_to_han(kysh.hiho[0]),
            "txtHhksNo2": mojimoji.zen_to_han(kysh.hiho[1]),
            "txtHhksNo3": mojimoji.zen_to_han(kysh.hiho[2]),
            "txtJgshNo1": (mojimoji.zen_to_han(jygs.kohonum[0])),
            "txtJgshNo2": (mojimoji.zen_to_han(jygs.kohonum[1])),
            "txtJgshNo3": (mojimoji.zen_to_han(jygs.kohonum[2])),
            "skkuStkYmdGG": (mojimoji.zen_to_han(kysh.getdate[0])),
            "skkuStkYmdYY": (mojimoji.zen_to_han(kysh.getdate[1])),
            "skkuStkYmdMM": (mojimoji.zen_to_han(kysh.getdate[2])),
            "skkuStkYmdDD": (mojimoji.zen_to_han(kysh.getdate[3])),
            "riskYmdGG": (mojimoji.zen_to_han(kysh.lostdate[3])),
            "riskYmdYY": (mojimoji.zen_to_han(kysh.lostdate[3])),
            "riskYmdMM": (mojimoji.zen_to_han(kysh.lostdate[3])),
            "riskYmdDD": (mojimoji.zen_to_han(kysh.lostdate[3])),
            "rdoSoshitsuGenin": "2",
            "rdoRiskHyoKofuKibo": "1",
            "txt1ShuukanNoShoteiRodoJnJn": "40",
            "txt1ShuukanNoShoteiRodoJnFun": "00",
            "rdoHojuSaiyoYoteiNoUmu": "",
            "txtFuriganaKatakana": "",
            "txtNewNameKnj": "",
            "txtHhksNameRomaji":"", 
            "txtZairyuCardNo": "",
            "bikoZairyuKikanYY": "",
            "bikoZairyuKikanMM": "",
            "bikoZairyuKikanDD": "",
            "cmbHakenUkeoiShuroukbn":"", 
            "txtBikoKokuseki": "",
            "txtBikoZairyuSkku": "",
            "txtHhksNameKana": "",
            "txtHhksNameKnj": "",
            "rdoSeibetsu": (mojimoji.zen_to_han(kysh.sex)),
            "seinenGG": (mojimoji.zen_to_han(kysh.birth[0])),
            "seinenYY": (mojimoji.zen_to_han(kysh.birth[1])),
            "seinenMM": (mojimoji.zen_to_han(kysh.birth[2])),
            "seinenDD": (mojimoji.zen_to_han(kysh.birth[3])),
            "txtHhksYubinNo1": "",
            "txtHhksYubinNo2": "",
            "txtHhksJusho": (mojimoji.han_to_zen(kysh.address)),
            "txtJgshMeisho": (mojimoji.han_to_zen(jygs.name)),
            "nameChangeYmdGG": "5",
            "nameChangeYmdYY": "",
            "nameChangeYmdMM": "",
            "nameChangeYmdDD": "",
            "txtHhksChangeCause": "自己都合",
            "txtJgysYubinNo1": "",
            "txtJgysYubinNo2": "",
            "txtJgysJusho": (mojimoji.han_to_zen(jygs.address)),
            "txtJgysName": (mojimoji.han_to_zen(jygs.name)),
            "txtJgysTel1": (mojimoji.zen_to_han(jygs.phone[0])),
            "txtJgysTel2": (mojimoji.zen_to_han(jygs.phone[1])),
            "txtJgysTel3": (mojimoji.zen_to_han(jygs.phone[2])),
            "todokedeYmdYY": "",
            "todokedeYmdMM": "",
            "todokedeYmdDD": "",
            "txtShinseiSaki": "新宿",
            "shakaiRomushiSkseYmdGG": "5",
            "shakaiRomushiSkseYmdYY": "",
            "shakaiRomushiSkseYmdMM": "",
            "shakaiRomushiSkseYmdDD": "",
            "txtShakaiRomushiDairiSha": "",
            "txtShakaiRomushiName": "",
            "txtShakaiRomushiTel1": "",
            "txtShakaiRomushiTel2": "",
            "txtShakaiRomushiTel3": "",
            "commonDownload": "帳票作成",
            "screenId": "001100",
            "action": "",
            "codeAssistType": "",
            "codeAssistKind": "",
            "codeAssistCode": "",
            "codeAssistItemCode": "",
            "codeAssistItemName": "",
            "codeAssistDivide": "",
            "maba_vrbs": "continueMakeButton,commonDownload",
            "preCheckFlg": "false"
        }
        #print(info_send)
        make_pdf_url = "https://hoken.hellowork.mhlw.go.jp/assist/001050.do"
        response_cookie = response.cookies
        res_file = session.post(make_pdf_url, data=info_send, cookies=response_cookie)
        res_file.raise_for_status()
        #contentType = res_file.headers['Content-Type']
        print(res_file.headers)
        contentDisposition = res_file.headers['Content-Disposition']
        with open("雇用保険_{}.pdf".format(kysh.name_kanji[0]), 'wb') as saveFile:
                saveFile.write(res_file.content)
        session.close()

#import jygs_input
#import kysh_input
#jygs = jygs_input.jygs()
#jygs.load_info()
#print("被保険者の列数を入力(kysh_info.xlxsを参照)")
#n = int(input())
#kysh = kysh_input.kysh()
#kysh.load_info(n)
#fill_koho_class.fill_koho(kysh,jygs)