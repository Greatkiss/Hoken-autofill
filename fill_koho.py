from bs4 import BeautifulSoup
import requests
import mojimoji

class fill_koho_class:
    @staticmethod
    def fill_koho(kysh, jygs):
        session = requests.session()
        url_login = "https://hoken.hellowork.mhlw.go.jp/assist/001000.do?screenId=001000&action=koyohohiLicenceLink"
        res = session.get(url_login)
        res.raise_for_status()
        response_cookie = res.cookies
        #check box
        info = {
            "chkDoi": "1",
            "inputPrintButton": "内容を入力して印刷",
            "reportTypeHidden": "KOYOHOHILICENCE",
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
            "cmbStk": kysh.kubun,
            "txtFuriganaKatakana1": (mojimoji.zen_to_han(kysh.name_kana[0]) + ' ' + mojimoji.zen_to_han(kysh.name_kana[1])),
            "txtHhksNameKnj": (mojimoji.han_to_zen(kysh.name_kanji[0]) + '　' + mojimoji.han_to_zen(kysh.name_kanji[1])),
            "txtFuriganaKatakana2": "",
            "txtHkgoNoNameKnj": "",
            "cmbSeibetsu": kysh.sex,
            "seinengappiGG": (mojimoji.zen_to_han(kysh.birth[0])),
            "seinengappiYY": (mojimoji.zen_to_han(kysh.birth[1])),
            "seinengappiMM": (mojimoji.zen_to_han(kysh.birth[2])),
            "seinengappiDD": (mojimoji.zen_to_han(kysh.birth[3])),
            "txtJgshNo1": (mojimoji.zen_to_han(jygs.kohonum[0])),
            "txtJgshNo2": (mojimoji.zen_to_han(jygs.kohonum[1])),
            "txtJgshNo3": (mojimoji.zen_to_han(jygs.kohonum[2])),
            "cmbHhksToNattakotoNoGenin": "4",
            "cmbChgnShiharaiNoTaiyo": "1",
            "txtChgnChgnGetsugaku": str(int(kysh.tin)),
            "skkuStkYmdGG": (mojimoji.zen_to_han(kysh.getdate[0])),
            "skkuStkYmdYY": (mojimoji.zen_to_han(kysh.getdate[1])),
            "skkuStkYmdMM": (mojimoji.zen_to_han(kysh.getdate[2])),
            "skkuStkYmdDD": (mojimoji.zen_to_han(kysh.getdate[3])),
            "cmbKoyoKeitai": "7",
            "cmbSksu": "05",
            "cmbShusyokuKeiro": "4",
            "txt1ShuukanNoShoteiRodoJnJn": "40",
            "txt1ShuukanNoShoteiRodoJnFun": "00",
            "keiyakuKikanNoSdamStaGG": "",
            "keiyakuKikanNoSdamStaYY": "",
            "keiyakuKikanNoSdamStaMM": "",
            "keiyakuKikanNoSdamStaDD": "",
            "keiyakuKikanNoSdamEndGG": "",
            "keiyakuKikanNoSdamEndYY": "",
            "keiyakuKikanNoSdamEndMM": "",
            "keiyakuKikanNoSdamEndDD": "",
            "rdoKeiyakuKikanNoSdamJokoUmu": "",
            "rdoKeiyakuKikanNoSdam": "2",
            "txtJgshMei": (mojimoji.han_to_zen(jygs.name)),
            "txtBiko": (mojimoji.han_to_zen(kysh.bikou)),
            "txtHhksNameRomaji": "",
            "txtZairyuCardNo": "",
            "bikoZairyuKikanYY": "",
            "bikoZairyuKikanMM": "",
            "bikoZairyuKikanDD": "",
            "rdoBikoSkkuGaiKyokaUmu": "",
            "cmbHakenUkeoiShuroukbn": "",
            "txtBikoKokuseki": "",
            "txtBikoZairyuSkku": "",
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
            "screenId": "001050",
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