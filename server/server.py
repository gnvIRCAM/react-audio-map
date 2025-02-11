import soundfile as sf
from playsound import playsound

from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = "super secret key"
CORS(app, expose_headers='Authorization')

@app.route('/play', methods=['POST'])
def play():
    try:
        data = request.get_json()
        playsound(data['filename'])
        return 'Things went well'
    except:
        return 'Things didnt go well' 

if __name__ == '__main__':
    app.run(debug=True)