from flask import *


def ecryption(text):
    cyfer = []
    for i in text:
        cyfer.append(chr(ord(i) + 46))
    cyfer.reverse()
    return "".join(cyfer)


def decryption(ecr):
    cyfer = []
    for i in ecr:
        cyfer.append(chr(ord(i) - 46))
    cyfer.reverse()
    return "".join(cyfer)


app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def Home():
    return render_template('index.html')


@app.route('/send', methods=["GET", "POST"])
def send():
    if request.method == 'POST':
        text = request.form['text_area']
        key = int(request.form['key'])
        ecr = ecryption(text)
        for i in range(key):
            ecr = ecryption(ecr)
    else:
        ecr = ""
    return render_template('send.html', params=ecr)


@app.route('/receive', methods=["GET", "POST"])
def receive():
    if request.method == 'POST':
        text = request.form['text_area']
        key = int(request.form['key'])
        dcr = decryption(text)
        for i in range(key):
            dcr = decryption(dcr)
    else:
        dcr = ""
    return render_template('receive.html', params=dcr)


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')