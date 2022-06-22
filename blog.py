from flask import Flask, render_template

app = Flask(__name__)


posts = [
    {
        'author': 'solo dolo',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'June 20, 2022'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'June 21, 2022'
    }
]


@app.route('/')
@app.route('/Home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='Abouts')

if __name__=="__main__":
    app.run(debug=True)