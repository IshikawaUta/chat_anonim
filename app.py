import os
from flask import Flask, render_template, request, jsonify, session
from google import genai
from google.genai import types
from dotenv import load_dotenv
import datetime
from typing import List, Dict

load_dotenv()

app = Flask(__name__)

app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'ganti_ini_dengan_kunci_sangat_rahasia_dan_acak_anda')

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("FATAL: GEMINI_API_KEY tidak ditemukan. Pastikan file .env sudah diisi.")
    client = None
else:
    try:
        client = genai.Client(api_key=api_key)
    except Exception as e:
        print(f"Error initializing Gemini client: {e}")
        client = None

MODEL_NAME = 'gemini-2.5-flash'
SYSTEM_INSTRUCTION_BASE = (
    "Anda adalah asisten chat anonim. Jawab semua pertanyaan dengan singkat dan membantu. "
    "Fokus pada topik yang dibahas. Jangan pernah menanyakan identitas pengguna atau informasi pribadi. "
    "Gunakan format Markdown jika perlu."
)

@app.route('/')
def index():
    """Halaman utama aplikasi chat."""
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """Endpoint untuk mengirim pesan dan mendapatkan balasan dari Gemini."""
    if not client:
        return jsonify({"error": "Layanan AI tidak dapat diinisialisasi."}), 500

    user_message = request.json.get('message')
    if not user_message:
        return jsonify({"error": "Pesan kosong."}), 400

    current_time_str = datetime.datetime.now().strftime(
        "Saat ini adalah: %A, %d %B %Y, pukul %H:%M WIB."
    )
    
    dynamic_system_instruction = (
        SYSTEM_INSTRUCTION_BASE + 
        f" **SELALU GUNAKAN WAKTU INI SEBAGAI WAKTU SAAT INI:** {current_time_str}"
    )

    if 'chat_id' not in session:
        session['chat_id'] = os.urandom(24).hex()
    
    history_dicts: List[Dict] = session.get('chat_history', [])
    try:
        history_objects = [types.Content.model_validate(h) for h in history_dicts]
    except Exception as e:
        print(f"Warning: Gagal memvalidasi riwayat. Memulai chat baru. Error: {e}")
        history_objects = []

    chat_session = client.chats.create(
        model=MODEL_NAME,
        history=history_objects,
        config=types.GenerateContentConfig(
            system_instruction=dynamic_system_instruction
        )
    )

    try:
        response = chat_session.send_message(user_message)
        ai_response = response.text

        current_history_objects = chat_session.get_history()
        new_history_dicts = [h.model_dump() for h in current_history_objects]
        
        session['chat_history'] = new_history_dicts
        
        return jsonify({"response": ai_response})

    except Exception as e:
        print(f"Gemini API Error: {e}")
        session.pop('chat_history', None) 
        return jsonify({"error": "Terjadi kesalahan pada layanan AI. Coba lagi."}), 500

@app.route('/clear', methods=['POST'])
def clear_chat():
    """Endpoint untuk menghapus riwayat chat anonim dari sesi."""
    session.pop('chat_history', None)
    session.pop('chat_id', None) 
    
    return jsonify({"status": "success", "message": "Riwayat chat telah dihapus."})

if __name__ == '__main__':
    app.run(debug=True)