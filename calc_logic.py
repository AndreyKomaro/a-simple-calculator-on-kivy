import math

import calc_gui

"""Логика программы"""

value_1 = ''
value_2 = ''
tk = 0
znak = ''
ZERO = 'На ноль делить нельзя!'


def logic(char):
    """Логика программы"""
    global value_1
    global value_2
    global tk
    global znak
    win = calc_gui.win

    match char.text:
        case '+' | '-' | 'x' | '/' | '%' | '=' as z:
            if (value_2 != '' or value_1 != '') and value_2 != '-' and value_1 != ZERO:
                if value_2:
                    if 'e' in value_2:
                        value_2 = value_2[:-2] if value_2[-2] == 'e' else value_2
                    if '.' in value_2:
                        value_2 = value_2[:-1] if value_2[-1] == '.' else value_2
                    value_2 = not_float(value_2)
                if value_1 and value_2 and znak:
                    value_1 = not_float(calculate(value_1, znak, value_2))
                    win.text = unary(value_1) + ('' if z == '=' else z)
                    value_2 = ''
                elif z != '=':
                    win.text = (unary(value_1) if value_1 else unary(value_2)) + z
                    if not value_1:
                        value_1 = value_2
                        value_2 = ''
                znak = z if z != '=' else ''
                tk = 0
        case 'C':
            win.text = value_2 = ''
            value_1 = ''
            znak = ''
            tk = 0
        case '<':
            if znak != '=':
                if len(value_2) > 1 and value_2[-2] == 'e':
                    value_2 = value_2[:-2]
                else:
                    value_2 = value_2[:-1] if len(value_2) > 1 else ''
                win_text()
                if not ('.' in value_2) and not ('e' in value_2):
                    tk = 0
        case '√':
            if value_2 != '' and value_2[0] != '-':
                value_2 = not_float(str(math.sqrt(float(value_2))))
                win_text()
            elif value_1 and znak == '':
                value_1 = not_float(str(math.sqrt(float(value_1))))
                win_text()
        case '+/-':
            if znak != '' if value_1 else znak == '':
                value_2 = (value_2[1:] if value_2[0] == '-' else '-' + value_2) if len(value_2) else '-'
                win_text()
        case 'e+' | 'e-' as e:
            if value_2 and value_2[-1] != '.' and 'e' not in value_2:
                value_2 = exponent_change(value_2, e)
                tk = 1
                win_text()
        case val:
            if (znak != '' if value_1 else znak == '') and value_1 != ZERO and len(value_2) < 23:
                match val:
                    case '.':
                        if tk == 0:
                            value_2 = (value_2 + '0' + val if value_2 == '-' or value_2 == ''
                                       else value_2 + val)
                            tk = 1
                    case v:
                        value_2 = '-' if value_2 == '-0' else value_2
                        value_2 = '' if value_2 == '0' else value_2
                        value_2 = value_2 + v
                win_text()


def calculate(a, z, b):
    a = float(a) if '.' or 'e' in a else int(a)
    b = float(b) if '.' or 'e' in b else int(b)
    v = 'error'
    match z:
        case '+':
            v = a + b
        case '-':
            v = a - b
        case 'x':
            v = a * b
        case '/':
            if b == 0: return ZERO
            v = a / b
        case '%':
            if b == 0: return ZERO
            v = a % b
    return str(v)


def unary(val):  # Добавление унарного минуса
    return f'({val})' if len(val) and val[0] == '-' else val


def not_float(val_2):  # Отсечение лишних нулей после точки
    if val_2 != ZERO:
        f = float(val_2)
        f = int(f) if f % 1 == 0 else f
        val_2 = format(f, 'e') if len(str(f)) > 23 else str(f)  # В экспоненту
    return val_2


def exponent_change(val_3, e):  # Добавление экспоненты
    if len(val_3) > 1 and val_3[0] == '-' or len(val_3) > 0 and val_3[0] != '-':
        val_3 += 'e+' if e == 'e+' else 'e-'
    return val_3


def win_text():
    win = calc_gui.win
    win.text = unary(value_1) + znak + unary(value_2)
