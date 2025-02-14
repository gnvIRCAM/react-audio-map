import soundfile as sf

from flask import Flask, request
from flask_cors import CORS
from pydub import AudioSegment
import pydub.playback

app = Flask(__name__)
app.secret_key = "super secret key"
CORS(app, expose_headers='Authorization')

@app.route('/play', methods=['POST'])
def play():
    try:
        data = request.get_json()
        # playsound(data['filename'])
        sound = AudioSegment.from_file(data['filename'])
        pydub.playback.play(sound)
        return 'Things went well'
    except:
        return 'Things didnt go well' 

if __name__ == '__main__':
    app.run(debug=True)