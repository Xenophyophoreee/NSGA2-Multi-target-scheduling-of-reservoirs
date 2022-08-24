# 9个水电站的主要函数表


def h1v1_w1(hx):
    vx = round(3.33257987E-06 * float(hx)**4 - 3.40473719E-03 * float(hx)**3 + 1.30798512E+00 * float(hx)**2 - 2.23769818E+02 * float(hx) + 1.43757521E+04, 5)
    return vx


def v1h1_w1(vx):
    hx = -1.8741E-02 * float(vx)**4 + 3.5765E-01 * float(vx)**3 - 2.7713E+00 * float(vx)**2 + 1.3795E+01 * float(vx) + 2.3637E+02
    return hx


def qh2_w1(qx):
    h2x = -1.4364E-17 * float(qx)**6 + 7.5688E-14 * float(qx)**5 - 1.5723E-10 * float(qx)**4 + 1.6373E-07 * float(qx)**3 - 9.0046E-05 * float(qx)**2 + 2.6043E-02 * float(qx) + 2.0833E+02
    return h2x


def qh2_w2(qx):
    h2x = -1.0596E-20 * float(qx)**6 + 1.5326E-16 * float(qx)**5 - 8.7713E-13 * float(qx)**4 + 2.5807E-09 * float(qx)**3 - 4.3865E-06 * float(qx)**2 + 6.0464E-03 * float(qx) + 1.9697E+02
    return h2x


def qh2_w3(qx):
    h2x = -4.0414E-14 * float(qx)**4 + 3.7227E-10 * float(qx)**3 - 1.2276E-06 * float(qx)**2 + 3.1791E-03 * float(qx) + 1.8569E+02
    return h2x


def qh2_w4(qx):
    h2x = -1.7856E-14 * float(qx)**4 + 2.1008E-10 * float(qx)**3 - 9.6793E-07 * float(qx)**2 + 3.3905E-03 * float(qx) + 1.7534E+02
    return h2x


def qh2_w5(qx):
    h2x = 9.8796E-18 * float(qx)**5 - 1.3859E-13 * float(qx)**4 + 7.6360E-10 * float(qx)**3 - 2.1600E-06 * float(qx)**2 + 4.2446E-03 * float(qx) + 1.6067E+02
    return h2x


def qh2_w6(qx):
    h2x = -4.5507E-21 * float(qx)**6 + 7.6477E-17 * float(qx)**5 - 5.1900E-13 * float(qx)**4 + 1.8109E-09 * float(qx)**3 - 3.4518E-06 * float(qx)**2 + 4.6714E-03 * float(qx) + 1.4780E+02
    return h2x


def qh2_w7(qx):
    h2x = -5.0360E-21 * float(qx)**6 + 8.5296E-17 * float(qx)**5 - 5.7766E-13 * float(qx)**4 + 2.0097E-09 * float(qx)**3 - 3.8819E-06 * float(qx)**2 + 5.2616E-03 * float(qx) + 1.3389E+02
    return h2x


def qh2_w8(qx):
    h2x = -5.1103E-21 * float(qx)**6 + 8.1461E-17 * float(qx)**5 - 5.3076E-13 * float(qx)**4 + 1.8394E-09 * float(qx)**3 - 3.7359E-06 * float(qx)**2 + 5.8813E-03 * float(qx) + 1.2257E+02
    return h2x


def qh2_w9(qx):
    h2x = -2.7608E-20 * float(qx)**6 + 4.0393E-16 * float(qx)**5 - 2.3067E-12 * float(qx)**4 + 6.5289E-09 * float(qx)**3 - 9.7864E-06 * float(qx)**2 + 9.3708E-03 * float(qx) + 1.1346E+02
    return h2x


print(h1v1_w1(275) - h1v1_w1(245))
print(v1h1_w1(h1v1_w1(275)))
print(v1h1_w1(10))
# print("---------------------------")
# print(qh2_w1(50))
# print(qh2_w1(500))
# print("---------------------------")
# print(qh2_w2(50))
# print(qh2_w2(500))
# print("---------------------------")
# print(qh2_w3(50))
# print(qh2_w3(500))
# print("---------------------------")
# print(qh2_w4(50))
# print(qh2_w4(500))
# print("---------------------------")
# print(qh2_w5(50))
# print(qh2_w5(500))
# print("---------------------------")
# print(qh2_w6(50))
# print(qh2_w6(500))
# print("---------------------------")
# print(qh2_w7(50))
# print(qh2_w7(500))
# print("---------------------------")
# print(qh2_w8(50))
# print(qh2_w8(500))
# print("---------------------------")
# print(qh2_w9(50))
# print(qh2_w9(500))

