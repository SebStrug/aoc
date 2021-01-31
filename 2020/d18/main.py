import re

ex = '2 * 3 + (4 * 5)'


def eval_expr(ex: str):
    while ' ' in ex:
        expr = re.match(r'\S+\s\S+\s\S+', ex).group()
        print(f'ex: {ex}, part: {expr}')
        ex = ex.replace(expr, str(eval(expr)))
    return ex


def eval_line(ex: str):
    for paren in re.findall(r'\(.+\)', ex):
        ex = ex.replace(paren, str(eval_expr(paren.strip('()'))))
    # print(ex)
    ex = eval_expr(ex)
    return ex

# need to account for nested parentheses!
