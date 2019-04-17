from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    temp = request.args.get("kleur")
    print(temp)
    tekst = '<body bgcolor="{}">Hello World</body>'.format(temp)
    return tekst

@app.route('/')
def  sqldemo


if __name__ == '__main__':
    app.run()
