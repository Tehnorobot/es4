from flask import Flask, render_template, redirect
from loginform import LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title, n=0)


@app.route('/training/<prof>')
def training(prof):
    return render_template('base.html', prof=prof, n=1)


@app.route('/list_prof/<list>')
def list_prof(list):
    return render_template('base.html', list=list, n=2)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    lis = {
        'Название': 'Анкета',
        'Фамилия': 'Бобик',
        'Имя': 'Андрей',
        'Образование': 'Не имеется',
        'Пол': 'male',
        'Мотивация': 'Всегда хотел быть подальше от людей',
        'Готовы остаться на Марсе?': True
    }
    return render_template('auto_answer.html', lis=lis)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Аварийный доступ', form=form, n=3)


@app.route('/distribution')
def distribution():
    astronaut_list = ['Ридли Скотт',
                      'Энди Уир',
                      'Марк Уотни',
                      'Венката Капур',
                      'Тедди Сандерс',
                      'Шон Бин']
    return render_template('list.html', list=astronaut_list, n=4)


@app.route('/table/<sex>/<int:age>')
def table(sex, age):
    return render_template('table.html', sex=sex, age=age, n=5)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
