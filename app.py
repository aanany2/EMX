
# A very simple Flask Hello World app for you to get started with...
from flask import Flask, request

app = Flask(__name__)

ips = {}

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
        return "Github link"

    elif query_args == 'Status':
        return "H1B Visa"

    elif query_args == 'Resume':
        return "https://drive.google.com/file/d/15P-_tkf1zWkBGDUP_WDlJTiL-EaeUkM4/view?usp=sharing"

    elif query_args == 'Degree':
        return "Masters in Information Systems at UIC"

    elif query_args == 'Puzzle':
        return   " ABCD\nA=>>>\nB<=>>\nC<<=<\nD<<>=\n"
        # return (args,query_args,desc_args, requested_url)
        # print ("this is the all arguement", args)
        # print ("this is query arguemnts", query_args)
        # print ("this is the description arguement", desc_args)
        # print (requested_url)
        # return (requested_url)

if __name__ == '__main__':
    app.run(debug=True)

