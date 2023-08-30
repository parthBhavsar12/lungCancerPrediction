from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('login.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/logout')
def logout():
    return "Logout"


@app.route('/home')
def home():
    # return render_template('home.html')
    return "Home"


@app.route('/info')
def info():
    # return render_template('info.html')
    return "Info"


@app.route('/predict')
def predict():
    # return render_template('predict.html')
    return "Prediction"


@app.route('/about')
def about():
    # return render_template('about.html')
    return "About"


@app.route('/contact')
def contact():
    # return render_template('contact.html')
    return "Contact"


if __name__ == '__main__':
    app.run(debug=True)

