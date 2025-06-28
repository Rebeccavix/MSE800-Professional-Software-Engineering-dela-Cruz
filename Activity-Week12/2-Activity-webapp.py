# Activity W12-2: Develop a web App using Flask - Load image
# Develop a Flask web application that allows users to upload
# an image and display it on the browser. Share your GitHub link and screenshot of your result.

from flask import Flask, request
import os

app = Flask(__name__)

# Create upload folder
UPLOAD_FOLDER = '/upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        image_url = url_for(filename='uploads/' + file.filename)
        return render_template('profile.html', image_url=image_url)


if __name__ == "__main__":
    app.run(debug=True)
