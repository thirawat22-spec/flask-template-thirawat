from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    title = 'Home Page'
    return render_template('index.html', title=title)

@app.route('/about')
def about():
    title = 'About Page'
    name = 'thirawat khantamala'
    email = 'std.68122420104@ubru.ac.th'
    mobile = '061-049-7689'
    age = 21

    return render_template('about.html',title=title, name=name, email=email, mobile=mobile, age=age)

@app.route('/favorite/foods')
def favorite_foods():
    title = 'Favorite Foods Page'
    foods = ['ไข่เจียว','ซาลาเปา','หม่าล่า','สุกี้','แมวย่าง']
    return render_template('favorite_foods.html',title=title,foods=foods)

@app.route('/favorite/sports')
def favorite_sports():
    title = 'Favorite Sports Page'
    sports = ['Esport','มวยอิสระ','กรีฑา','ยิงธนู','แข่งรถ']
    return render_template('favorite_sports.html',title=title,sports=sports)

@app.route('/favorite/movies')
def favorite_movies():
    title = 'Favorite Movies Page'
    movies = ['Green Book','Inception','Interstellar','Now You See Me','The Conjuring']
    return render_template('favorite_movies.html',title=title,movies=movies)