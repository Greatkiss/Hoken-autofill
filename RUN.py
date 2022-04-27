import jygs_input
import kysh_input
from fill_koho import fill_koho_class as koho
from fill_shaho import fill_shaho

jygs = jygs_input.jygs()
jygs.load_info()

print("被保険者の人数を入力(kysh_info.xlxsを参照)")
n = int(input())
kysh = kysh_input.kysh()
for i in range(n):
    kysh.load_info(i+2)
    koho.fill_koho(kysh,jygs)
    fill_shaho(jygs, kysh)
