import re
"""
link: https://www.codewars.com/kata/59c2e2a36bddd2707e000079

kata's name: Solvwe For X

"""


def solve_for_x(equation):
    return equation
    # print(solve_for_x('x - 5 = 20'), 25)
# print(solve_for_x('20 = 5 * x - 5'), 5)


def eq(es):
    dat1 = re.findall(r"[0-9x()+-/*=]", es)
    es1 = re.findall(r"\d+|\D", "".join(dat1))

    print(es1)
    if es1.index("=") == 1:
        es2 = " ".join(es1[2:]) + " - " + es1[0] + " = 0"
        print(es2)


    elif es1.index("=") == len(es1) - 2:
        print(-2)
        print('oh yeahy')




print(eq('20 =  x+   23  - 5 +   5'))

def calc(stri1):
    dat1 = re.findall(r"[0-9()+-/*=]", stri1)
    expr = re.findall(r"\d+|\D", "".join(dat1))

    for i in range(len(expr)):
        if expr[i].isdigit():
            expr[i] = float(expr[i])
    while len(expr) > 1:
        if "*" in expr:
            first = expr[expr.index("*") - 1]
            second = expr[expr.index("*") + 1]
            for_paste = first * second
            expr[expr.index("*") - 1: expr.index("*") + 2] = [for_paste]

        elif "/" in expr:
            first = expr[expr.index("/") - 1]
            second = expr[expr.index("/") + 1]
            for_paste = first / second
            expr[expr.index("/") - 1: expr.index("/") + 2] = [for_paste]

        elif "+" in expr:
            first = expr[expr.index("+") - 1]
            second = expr[expr.index("+") + 1]
            for_paste = first + second
            expr[expr.index("+") - 1: expr.index("+") + 2] = [for_paste]

        elif "-" in expr:
            first = expr[expr.index("-") - 1]
            second = expr[expr.index("-") + 1]
            for_paste = first - second
            expr[expr.index("-") - 1: expr.index("-") + 2] = [for_paste]

    return expr[0]


# print(calc(input(":  ")))




s = "5 * x - 5 = 20"