from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    param = {}
    param['title'] = 'Заготовка'
    param['headline'] = "Миссия Колонизация Марса"
    param['text'] = "И на Марсе будут яблони цвести!"
    return render_template('base.html', **param)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
