from flask import Flask, render_template, abort, request, redirect

app = Flask(__name__)
articles = [
    {
        'id': 1,
        'author': 'Taras Zagr',
        'title': 'Spring',
        'text': 'About quadro'
    },
    {
        'id': 2,
        'author': 'Juan Carlos',
        'title': 'Winner',
        'text': 'This is a development server. Do not use it in a production deployment. Use a production WSGI server instead'
    }
]


# users = [
#     {
#         'name': '',
#         'email': '',
#         'telephone': '',
#         'password': '',
#         'repit_password': '',
#         'avatar': ''
#
#     }]

@app.route('/')
def main_page():
    return render_template('index.html', title='KsuZag', articles=articles)


@app.route('/article/<int:id>')
def get_article(id):
    for article in articles:
        if article['id'] == id:
            return render_template('generic.html', article=article, title='KsuZag')
    abort(404)


@app.route('/create/article', methods=['GET', 'POST'])
def create_article():
    '''GET,POST,PUT,DELETE'''

    if request.method == 'GET':
        return render_template('create_article.html')
    elif request.method == 'POST':
        articles.append({
            'author': request.form['art_author'],
            'title': request.form['art_title'],
            'text': request.form['art_text'],
        })
        return redirect('/')
    else:
        return 'METHOD BAD'


@app.route('/about')
def about():
    return render_template('about.html', title='KsuZag')


@app.route('/elements')
def elements():
    return  render_template('elements.html', title='KsuZag')



# @app.route('/create/user')
# def create_user():
#     if request.method == 'GET':
#         return render_template('create_user.html')
#     elif request.method == 'POST':
#         for user in users:
#             user['name'] = request.form['user_name']
#             user['email'] = request.form['user_email']
#             user['telephone'] = request.form['user_tel']
#             user['password'] = request.form['user_password']
#             user['repit_password'] = request.form['user_rep_pass']
#             user['avatar'] = request.form['user_avatar']
#             return redirect('/')


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
