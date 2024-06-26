from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
import os

page = """
<!DOCTYPE html>
<html>
<body>

<h2>Upload File</h2>
<form action="/upload" method="POST" enctype="multipart/form-data">
   <input type="file" name="file" />
   <input type="submit"/>
</form>

</body>
</html>
"""


def runReciver(portNum=5000):
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = '.'

    @app.route('/upload', methods=['GET', 'POST'])
    def upload_file():
        if request.method == 'POST':
            file = request.files['file']
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return 'File uploaded and saved.'
        return page
    
    app.run(port=portNum)

def runUploader(filePath, portNum=5000):
    app = Flask(__name__)

    @app.route('/download')
    def uploader():
        return send_file(path_or_file=filePath)
    
    app.run(port=portNum)

if __name__ == '__main__':
    runReciver()