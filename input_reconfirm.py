def jygs_num_input(kind: str):
    print("type the first digits of {0}".format(kind))
    num0 = input()
    print("type the second digits of {0}".format(kind))
    num1 = input()
    print("type the last digits of {}".format(kind))
    num2 = input()
    return num0, num1, num2

def jygs_name_input(kind: str):
    print("type the {0} ".format(kind))
    hoge = input()
    return hoge

def reconfirm(kind: str, hoge):
    print("the {0} is {1}? (y/n)".format(kind, hoge))
    ans = input()
    while(ans != 'y'):
        hoge =jygs_name_input(kind)
        print("the {0} is {1}? (y/n)".format(kind, hoge))
        ans = input()
    return hoge

def reconfirm_num(kind: str, hoge0, hoge1, hoge2):
    print("the {0} is {1}-{2}-{3}? (y/n)".format(kind, hoge0, hoge1, hoge2))
    ans = input()
    while(ans != 'y'):
        hoge0, hoge1, hoge2=jygs_num_input(kind)
        print("the {0} is {1}-{2}-{3}? (y/n)".format(kind, hoge0, hoge1, hoge2))
        ans = input()
    return hoge0, hoge1, hoge2

def kysh_name_input(kind: str):
    print("type the {0} of the hi-koyou-sha".format(kind))
    hoge = input()
    hoge_l = hoge.split()
    return hoge_l

def reconfirm_name(kind: str, hoge_l):
    print("the {0} is {1} {2}? (y/n)".format(kind, hoge_l[0], hoge_l[1]))
    ans = input()
    while(ans != 'y'):
        hoge_l=kysh_name_input(kind)
        print("the {0}  is {1} {2}? (y/n)".format(kind, hoge_l[0], hoge_l[1]))
        ans = input()
    return hoge_l

def kysh_num_input(kind: str):
    print("type the first digits of {0}".format(kind))
    num0 = input()
    print("type the second digits of {0}".format(kind))
    num1 = input()
    print("type the third digits of {}".format(kind))
    num2 = input()
    print("type the last digits of {}".format(kind))
    num3 = input()
    return num0, num1, num2, num3

def kysh_reconfirm_num(kind: str, hoge0, hoge1, hoge2, hoge3):
    print("the {0} is {1}-{2}-{3}-{4}? (y/n)".format(kind, hoge0, hoge1, hoge2, hoge3))
    ans = input()
    while(ans != 'y'):
        hoge0, hoge1, hoge2, hoge3=jygs_num_input(kind)
        print("the {0} is {1}-{2}-{3}-{4}? (y/n)".format(kind, hoge0, hoge1, hoge2, hoge3))
        ans = input()
    return hoge0, hoge1, hoge2, hoge3