# Activity W12-2: Develop a web App using Flask - Load image
# Develop a Flask web application that allows users to upload
# an image and display it on the browser. Share your GitHub link and screenshot of your result.

from flask import Flask, request
import os

app = Flask(__name__)

# Create static folder
if not os.path.exists('static'):
    os.makedirs('static')


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
        file.save(f'static/{file.filename}')
        result += f'<img src="/static/{file.filename}">'

    return result


# Run the app
app.run(debug=True)
