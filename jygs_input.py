import pandas as pd
from input_reconfirm import jygs_name_input, jygs_num_input, reconfirm, reconfirm_num

class jygs:
    def __init__(self):
        self.name = ""
        self.num = [""]*3
        self.address = ""
        self.simei = self.name
        self.phone = [""]*3
    def type_info(self):

        name =jygs_name_input("name")
        name = reconfirm("name", name)
        self.name = name

        num0, num1, num2=jygs_num_input("jigyo-sho bango-")
        num0, num1, num2=reconfirm_num("jigyo-sho bango-", num0, num1, num2)
        self.num[0] = num0
        self.num[1] = num1
        self.num[2] = num2

        adrs =jygs_name_input("address")
        adrs = reconfirm("name", adrs)
        self.address = adrs

        num0, num1, num2=jygs_num_input("phone number")
        num0, num1, num2=reconfirm_num("phone number", num0, num1, num2)
        self.phone[0] = num0
        self.phone[1] = num1
        self.phone[2] = num2

        self.simei = self.name