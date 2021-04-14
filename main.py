from flask import Flask, render_template, abort, request, redirect
import random
import string
import os

app = Flask(__name__)
BASE_IMG_PATH = 'static/images/pic01.jpg'
articles = [
    {
        'id': 1,
        'views_count': 0,
        'author': 'Taras Zagr',
        'title': 'Spring',
        'text': 'About quadro',
        'img': BASE_IMG_PATH
    },
    {
        'id': 2,
        'views_count': 0,
        'author': 'Juan Carlos',
        'title': 'Winner',
        'text': 'This is a development server. Do not use it in a production deployment. Use a production WSGI server instead',
        'img': BASE_IMG_PATH
    }

]

users = [
    {
        'name': '',
        'email': '',
        'telephone': '',
        'password': '',
        'repit_password': '',
        'img': BASE_IMG_PATH

    }]


@app.route('/')
def main_page():
    return render_template('index.html', title='KsuZag', articles=articles)


@app.route('/article/<int:id>')
def get_article(id):
    for article in articles:
        if article['id'] == id:
            article['views_count'] += 1
            return render_template('generic.html', article=article, title='KsuZag')
    abort(404)


@app.route('/create/article', methods=['GET', 'POST'],)
def create_article():
    '''GET,POST,PUT,DELETE'''

    if request.method == 'GET':
        return render_template('create_article.html', title='KsuZag')
    elif request.method == 'POST':
        image = request.files['article_image']
        random_name = ''.join([random.choice(string.digits + string.ascii_letters) for x in range(8)])
        img_path = f'static/images/{random_name}.jpg'
        image.save(img_path)
        articles.append({
            'id': len(articles) + 1,
            'views_count': 0,
            'author': request.form['art_author'],
            'title': request.form['art_title'],
            'text': request.form['art_text'],
            'img': img_path
        })
        return redirect('/')
    else:
        return 'METHOD BAD'


@app.route('/update/article/<int:id>', methods=['GET', 'POST'])
def update_article(id):
    if request.method == 'GET':
        for article in articles:
            if article['id'] == id:
                return render_template('update_article.html', article=article)
        abort(404)
    elif request.method == 'POST':
        image = request.files['article_image']
        for article in articles:
            if article['id'] == id:
                article['title'] = request.form['art_title']
                article['author'] = request.form['art_author']
                article['text'] = request.form['art_text']
                if image.filename:
                    random_name = ''.join([random.choice(string.digits + string.ascii_letters) for x in range(8)])
                    img_path = f'static/images/{random_name}.jpg'
                    image.save(img_path)
                else:
                    img_path = BASE_IMG_PATH
                if article['img'] != BASE_IMG_PATH:
                    os.remove(article['img'])

                article['img'] = img_path
                return redirect(f'/article/{article["id"]}')


@app.route('/elements')
def elements():
    return render_template('elements.html', title='KsuZag')


@app.route('/about')
def about():
    return render_template('about.html', title='KsuZag')


@app.route('/create/user')
def create_user():
    if request.method == 'GET':
        return render_template('create_user.html')
    elif request.method == 'POST':
        for user in users:
            user['name'] = request.form['user_name']
            user['email'] = request.form['user_email']
            user['telephone'] = request.form['user_tel']
            user['password'] = request.form['user_password']
            user['repit_password'] = request.form['user_rep_pass']
            user['avatar'] = request.form['user_avatar']
            return redirect('/')


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
