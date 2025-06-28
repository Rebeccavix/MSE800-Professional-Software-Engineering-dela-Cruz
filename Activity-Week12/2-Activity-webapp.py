# Activity W12-2: Develop a web App using Flask - Load image
# Develop a Flask web application that allows users to upload
# an image and display it on the browser. Share your GitHub link and screenshot of your result.

from flask import Flask, request
import os

app = Flask(__name__)

# Create upload folder
if not os.path.exists('Activity-Week12/upload'):
    os.makedirs('Activity-Week12/upload')


@app.route('Activity-Week12/', methods=['GET', 'POST'])
def upload_file():
    result = '''
        <form method="post" enctype="multipart/form-data">
            <input type="file" name="file">
            <input type="submit" value="Upload">
        </form>
    '''

    if request.method == 'POST':
        file = request.files['file']
        file.save(f'Activity-Week12/upload/{file.filename}')
        result += f'<img src="/Activity-Week12/upload/{file.filename}">'

    return result


# Run the app
app.run(debug=True)
