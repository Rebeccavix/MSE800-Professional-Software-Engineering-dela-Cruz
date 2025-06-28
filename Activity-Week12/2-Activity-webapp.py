# Activity W12-2: Develop a web App using Flask - Load image
# Develop a Flask web application that allows users to upload
# an image and display it on the browser. Share your GitHub link and screenshot of your result.

from flask import Flask, request, send_from_directory
import os

app = Flask(__name__)

# Get the absolute path to the directory this script is in
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'upload')

# Create upload folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    result = '''
        <form method="post" enctype="multipart/form-data">
            <input type="file" name="file">
            <input type="submit" value="Upload">
        </form>
    '''
    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename:
            filename = file.filename
            save_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(save_path)
            result += f'<img src="/upload/{filename}" style="max-width:300px;">'
    return result


@app.route('/upload/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)


if __name__ == '__main__':
    app.run(debug=True)
