from flask import Flask, render_template
import os


app = Flask(__name__)
picFolder = os.path.join('static', 'pics')

app.config['UPLOAD_FOLDER'] = picFolder

@app.route("/")
def index():
    logo=os.path.join(app.config['UPLOAD_FOLDER'], 'logo.png')
    pic1=os.path.join(app.config['UPLOAD_FOLDER'], 'pic1.jpeg')
    pic2=os.path.join(app.config['UPLOAD_FOLDER'], 'pic2.jpeg')
    pic3=os.path.join(app.config['UPLOAD_FOLDER'], 'pic3.mp4')
    return render_template ('index.html', user_image=logo, user_image1=pic1, user_image2=pic2, user_image3=pic3)

if __name__== "__main__":
    app.run(debug=True)