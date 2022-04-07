from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome import service as fs
import jygs_input
import kysh_input

ChDr = "/Users/kk/chromedriver"
chrome_service = fs.Service(executable_path = ChDr)
driver = webdriver.Chrome(service=chrome_service)
driver.get('https://hoken.hellowork.mhlw.go.jp/assist/001000.do?screenId=001000&action=koyohohiLicenceLink')
term = driver.find_element_by_xpath('//*[@id="ID_form_1"]/table/tbody/tr')  #Check box
term.click()
terms = driver.find_element_by_xpath('//*[@id="ID_inputPrintButton"]')   #Open the input form
terms.click()

jygs = jygs_input.jygs()
jygs.type_info()

kysh = kysh_input.kysh()
kysh.type_info()

form_2_1 = driver.find_element_by_xpath('//*[@id="ID_txtHhksNo1"]')
form_2_2 = driver.find_element_by_xpath('//*[@id="ID_txtHhksNo2"]')
form_2_3 = driver.find_element_by_xpath('//*[@id="ID_txtHhksNo3"]')
form_2_1.send_keys(kysh.hiho[0])
form_2_2.send_keys(kysh.hiho[1])
form_2_3.send_keys(kysh.hiho[2])

form_3 = driver.find_element_by_xpath('//*[@id="ID_cmbStk"]')
form_3.send_keys(kysh.kubun)

form_4_1 = driver.find_element_by_xpath('//*[@id="ID_txtFuriganaKatakana1"]')
form_4_2 = driver.find_element_by_xpath('//*[@id="ID_txtHhksNameKnj"]')
form_4_1.send_keys(kysh.name_kana[0] + ' ' + kysh.name_kana[1])
form_4_2.send_keys(kysh.name_kanji[0] + '　' + kysh.name_kanji[1])

form_6 = driver.find_element_by_xpath('//*[@id="ID_cmbSeibetsu"]')
form_6.send_keys(kysh.sex)

form_7_1 = driver.find_element_by_xpath('//*[@id="ID_seinengappiGG"]')
form_7_2 = driver.find_element_by_xpath('//*[@id="ID_seinengappiYY"]')
form_7_3 = driver.find_element_by_xpath('//*[@id="ID_seinengappiMM"]')
form_7_4 = driver.find_element_by_xpath('//*[@id="ID_seinengappiDD"]')
form_7_1.send_keys(kysh.birth[0])
form_7_2.send_keys(kysh.birth[1])
form_7_3.send_keys(kysh.birth[2])
form_7_4.send_keys(kysh.birth[3])

form_8_1 = driver.find_element_by_xpath('//*[@id="ID_txtJgshNo1"]')
form_8_2 = driver.find_element_by_xpath('//*[@id="ID_txtJgshNo2"]')
form_8_3 = driver.find_element_by_xpath('//*[@id="ID_txtJgshNo3"]')
form_8_1.send_keys(jygs.num[0])
form_8_2.send_keys(jygs.num[1])
form_8_3.send_keys(jygs.num[2])

form_9 = driver.find_element_by_xpath('//*[@id="ID_cmbHhksToNattakotoNoGenin"]')
form_6.send_keys('2')

form_10_1 = driver.find_element_by_xpath('//*[@id="ID_cmbChgnShiharaiNoTaiyo"]')
form_10_2 = driver.find_element_by_xpath('//*[@id="ID_txtChgnChgnGetsugaku"]')
form_10_1.send_keys(kysh.tin[0])
form_10_2.send_keys(kysh.tin[1])

form_11_1 = driver.find_element_by_xpath('//*[@id="ID_skkuStkYmdGG"]')
form_11_2 = driver.find_element_by_xpath('//*[@id="ID_skkuStkYmdYY"]')
form_11_3 = driver.find_element_by_xpath('//*[@id="ID_skkuStkYmdMM"]')
form_11_4 = driver.find_element_by_xpath('//*[@id="ID_skkuStkYmdDD"]')
form_11_1.send_keys(kysh.getdate[0])
form_11_2.send_keys(kysh.getdate[1])
form_11_3.send_keys(kysh.getdate[2])
form_11_4.send_keys(kysh.getdate[3])

form_12 = driver.find_element_by_xpath('//*[@id="ID_cmbKoyoKeitai"]')
form_12.send_keys('7')

form_13 = driver.find_element_by_xpath('//*[@id="ID_cmbKoyoKeitai"]')
form_13.send_keys('7')

form_14 = driver.find_element_by_xpath('//*[@id="ID_cmbShusyokuKeiro"]')
form_14.send_keys('4')

form_15_1 = driver.find_element_by_xpath('//*[@id="ID_txt1ShuukanNoShoteiRodoJnJn"]')
form_15_2 = driver.find_element_by_xpath('//*[@id="ID_txt1ShuukanNoShoteiRodoJnFun"]')
form_15_1.send_keys('40')
form_15_2.send_keys('00')

form_16_2 = driver.find_element_by_xpath('//*[@id="ID_LrdoKeiyakuKikanNoSdam2"]')
form_16_2.click()

form_jimusho = driver.find_element_by_xpath('//*[@id="ID_txtJgshMei"]')
form_jimusho.send_keys(jygs.name)

form_bikou = driver.find_element_by_xpath('//*[@id="ID_txtBiko"]')
form_bikou.send_keys(kysh.bikou)

form_jgys_jusho = driver.find_element_by_xpath('//*[@id="ID_txtJgysJusho"]')
form_jgys_jusho.send_keys(jygs.address)

form_jigyosho_simei = driver.find_element_by_xpath('//*[@id="ID_txtJgysName"]')
form_jigyosho_simei.send_keys(jygs.simei)

form_jigyosho_phone_1 = driver.find_element_by_xpath('//*[@id="ID_txtJgysTel1"]')
form_jigyosho_phone_2 = driver.find_element_by_xpath('//*[@id="ID_txtJgysTel2"]')
form_jigyosho_phone_3 = driver.find_element_by_xpath('//*[@id="ID_txtJgysTel3"]')
form_jigyosho_phone_1.send_keys(jygs.phone[0])
form_jigyosho_phone_2.send_keys(jygs.phone[1])
form_jigyosho_phone_3.send_keys(jygs.phone[2])

form_sinseisaki= driver.find_element_by_xpath('//*[@id="ID_txtShinseiSaki"]')
form_sinseisaki.send_keys('新宿')