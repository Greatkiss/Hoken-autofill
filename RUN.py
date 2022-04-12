import jygs_input
import kysh_input
import fill_koho 
import fill_shaho

jygs = jygs_input.jygs()
jygs.type_info()

kysh = kysh_input.kysh()
kysh.type_info()

fill_shaho.fill_shaho(jygs, kysh)
fill_koho.fill_koho(jygs, kysh)
