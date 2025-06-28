from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/profile")
def profile():
    return render_template("profile.html")


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static')


@app.route('/static', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file:
        filename = file.filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        # url_for('static', filename=filename) will generate the correct URL for the static file
        image_url = url_for('static', filename=filename)
        return render_template('profile.html', image_url=image_url)
    return redirect(request.url)


if __name__ == "__main__":
    app.run(debug=True)
