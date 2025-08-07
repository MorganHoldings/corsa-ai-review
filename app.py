
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '🚗 Hello from Corsa AI Review!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
from flask import Flask, render_template, request
from PIL import Image
import pytesseract
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files.get("image")
    if not file or file.filename == "":
        return "No file uploaded", 400
    os.makedirs("uploads", exist_ok=True)
    filepath = os.path.join("uploads", file.filename)
    file.save(filepath)
    text = pytesseract.image_to_string(Image.open(filepath), lang="eng+kor")
    return render_template("result.html", text=text)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
