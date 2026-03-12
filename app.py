import os
import whisper
from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50MB max

ALLOWED_EXTENSIONS = {'mp3', 'wav', 'ogg', 'm4a', 'flac', 'mp4', 'webm'}

os.makedirs('uploads', exist_ok=True)

model = whisper.load_model("tiny")

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transcribe', methods=['POST'])
def transcribe():
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file uploaded'}), 400

    file = request.files['audio']

    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    if not allowed_file(file.filename):
        return jsonify({'error': 'File type not supported. Use mp3, wav, ogg, m4a, flac'}), 400

    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    try:
        result = model.transcribe(filepath)
        transcript = result['text'].strip()
        language = result.get('language', 'unknown')

        os.remove(filepath)

        return jsonify({
            'success': True,
            'transcript': transcript,
            'language': language
        })

    except Exception as e:
        if os.path.exists(filepath):
            os.remove(filepath)
        return jsonify({'error': f'Transcription failed: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
