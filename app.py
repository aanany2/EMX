
# A very simple Flask Hello World app for you to get started with...
from flask import Flask, request

app = Flask(__name__)

ips = {}

int_to_char_index = {0:'A', 1:'B', 2:'C', 3:'D'}
char_to_int_index = {'A':0, 'B':1, 'C':2, 'D':3}

def translate(condition):
    for index, i in enumerate(condition[1:]):
        if i == '<':
            return condition[0] + '<' + int_to_char_index[index]
        elif i == '>': # Convert
            return int_to_char_index[index] + '<' + condition[0]

def solver(translated):
    list_translated = list(translated)

    board = {'A':0, 'B':0, 'C':0, 'D':0}

    for item in list_translated:
        board[item[0]] = board[item[0]] - 1
        board[item[2]] = board[item[2]] + 1

    first = ''
    last = ''
    middles = []

    for k, v in board.items():
        if v == -1:
            first = k
        elif v == 1:
            last = k
        else:
            middles.append(k)

    # mid_check = first + ', '.join(translated)

    middle = ""

    for item in list_translated:
        if (middles[0] in item) and (middles[1] in item):
            middle = item
            break

    result = first + '<' + middle + '<' + last

    return result

def print_result(one_line_statement):
    board = {'A':"", 'B':"", 'C':"", 'D':""}

    for i in range(0, 7, 2):
        score = ""
        if i == 0:
            score = list("<<<<")
            score[char_to_int_index[one_line_statement[i]]] = '='
        elif i == 2:
            score = list("<<<<")
            score[char_to_int_index[one_line_statement[i]]] = '='
            score[char_to_int_index[one_line_statement[0]]] = '>'
        elif i == 4:
            score = list("<<<<")
            score[char_to_int_index[one_line_statement[i]]] = '='
            score[char_to_int_index[one_line_statement[0]]] = '>'
            score[char_to_int_index[one_line_statement[2]]] = '>'
        elif i == 6:
            score = list(">>>>")
            score[char_to_int_index[one_line_statement[i]]] = '='

        board[one_line_statement[i]] = "".join(score)

    result = " ABCD\n"

    for k, v in board.items():
        result = result + k + v + "\n"

    return result

@app.route('/')
def get_args():
    requested_url = request.url
    args = request.args
    query_args = args.get('q')
    desc_args = args.get('d')

    if query_args == 'Ping':
        return "OK"

    elif query_args == 'Name':
        return "Ananya Kumar"

    elif query_args == 'Years':
        return "4"

    elif query_args == 'Email Address':
        return "ananya10588@gmail.com"

    elif query_args == 'Position':
        return "Software Engineer"

    elif query_args == 'Referrer':
        return "LinkedIn"

    elif query_args == 'Degree':
        return "Masters in Information Systems at UIC"

    elif query_args == 'Phone':
        return "3127990999"

    elif query_args == 'Source':
        return "https://github.com/aanany2/EMX/blob/master/app.py"

    elif query_args == 'Status':
        return "H1B Visa"

    elif query_args == 'Resume':
        return "https://drive.google.com/file/d/15P-_tkf1zWkBGDUP_WDlJTiL-EaeUkM4/view?usp=sharing"

    elif query_args == 'Degree':
        return "Masters in Information Systems at UIC"

    elif query_args == 'Puzzle':
        conditions = desc_args.split(" ")[-1].splitlines()
        for_A = conditions[-4]
        translated_A = translate(for_A)
        for_B = conditions[-3]
        translated_B = translate(for_B)
        for_C = conditions[-2]
        translated_C = translate(for_C)
        for_D = conditions[-1]
        translated_D = translate(for_D)

        translated = set([translated_A, translated_B, translated_C, translated_D])

        one_line_statement = solver(translated)

        real_result = print_result(one_line_statement)
        # result = translated_A + " , " + translated_B + " , " + translated_C + " , " + translated_D
        return (real_result)

if __name__ == '__main__':
    app.run(debug=True)

