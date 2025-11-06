# 💬 Anonim Chat AI (Didukung Gemini)

[](https://www.google.com/search?q=LICENSE)

Aplikasi chat anonim berbasis web yang ditenagai oleh **Google Gemini AI**. Nikmati percakapan pribadi tanpa perlu login atau menyimpan data identitas Anda, memastikan riwayat obrolan tidak terkait dengan informasi pribadi Anda.

## 🚀 Fitur Utama

  * **Chat Anonim Penuh:** Tidak ada fitur login, ID sesi unik dibuat secara anonim untuk mempertahankan riwayat obrolan sementara.
  * **Didukung oleh Gemini:** Menggunakan model `gemini-2.5-flash` untuk respons yang cepat, membantu, dan ringkas.
  * **Riwayat Sesi:** Riwayat obrolan disimpan sementara di sesi peramban (menggunakan *session storage* Flask) dan dapat dihapus kapan saja.
  * **Instruksi Sistem Dinamis:** Memanfaatkan instruksi sistem yang dikonfigurasi untuk memastikan AI tetap membantu dan anonim.
  * **Deployment Mudah:** Dirancang untuk deployment mudah di platform *serverless* seperti Vercel.

## 🛠️ Persyaratan Sistem

  * Python 3.8+
  * Pip (Pengelola paket Python)
  * Akun **Google AI Studio** untuk mendapatkan **GEMINI\_API\_KEY**.
  * Akun **GitHub/GitLab/Bitbucket** (Opsional, diperlukan untuk *Continuous Deployment* ke Vercel).

## 🏗️ Struktur Proyek

Struktur proyek Anda mengikuti konvensi standar aplikasi Flask:

```
anonim-chat-ai/
├── .env                    # Variabel lingkungan (API Key, Secret Key)
├── app.py                  # Aplikasi Flask utama, routing, dan logika AI
├── requirements.txt        # Daftar semua dependensi Python
├── run.sh                  # Skrip untuk menjalankan aplikasi secara lokal
├── vercel.json             # Konfigurasi deployment untuk Vercel
├── LICENSE                 # Detail Lisensi (MIT)
├── templates/
│   └── index.html          # Template HTML utama untuk antarmuka chat
└── static/
    ├── favicon.ico         # Ikon situs web
    └── og-image.png        # Gambar untuk Open Graph (Preview saat dibagikan)
```

## 💻 Instalasi Lokal

Ikuti langkah-langkah di bawah ini untuk menjalankan proyek secara lokal.

### 1\. Klon Repositori

```bash
git clone https://github.com/IshikawaUta/chat_anonim.git
cd chat_anonim
```

### 2\. Konfigurasi Lingkungan

Buat *Virtual Environment* dan instal dependensi yang tercantum dalam `requirements.txt`.

```bash
# Buat Virtual Environment
python -m venv venv

# Aktifkan Virtual Environment
# Di macOS/Linux:
source venv/bin/activate
# Di Windows (PowerShell):
# .\venv\Scripts\Activate.ps1

# Instal dependensi
pip install -r requirements.txt
```

### 3\. Atur Kunci API dan Kunci Rahasia

Edit file `.env` dan masukkan kunci API Gemini serta kunci rahasia Flask Anda:

```bash
# File: .env
GEMINI_API_KEY="PASTE_API_KEY_ANDA_DI_SINI"
FLASK_SECRET_KEY="GANTI_DENGAN_KUNCI_RAHASIA_YANG_ACAK"
```

> **Peringatan Keamanan:** Jangan pernah melakukan *commit* file `.env` yang berisi kunci asli ke repositori publik.

### 4\. Jalankan Aplikasi

Gunakan skrip `run.sh` untuk menjalankan aplikasi di lingkungan debug.

```bash
bash run.sh
```

Aplikasi akan berjalan di `http://127.0.0.1:5000/`.

## ⚙️ Deployment ke Vercel

Proyek ini sudah dikonfigurasi untuk deployment ke Vercel berkat file `vercel.json` dan penggunaan Python Runtime Vercel.

### 1\. Siapkan Repositori Git

Pastikan semua kode Anda sudah di-*push* ke repositori Git (misalnya GitHub).

```bash
git add .
git commit -m "Initial commit and Vercel setup"
git push origin main
```

### 2\. Deployment Melalui Dashboard Vercel

1.  Buka **Vercel Dashboard** dan klik **"Add New"** \> **"Project"**.
2.  **Impor Git Repository** Anda.
3.  Pada tahap **"Configure Project"**:
      * **Build & Output Settings:** Vercel akan otomatis mendeteksi konfigurasi Python melalui `vercel.json`.
      * **Environment Variables:** Ini adalah langkah *kritis*. Tambahkan variabel lingkungan yang ada di file `.env` ke pengaturan proyek Vercel Anda:
          * `GEMINI_API_KEY`
          * `FLASK_SECRET_KEY`
4.  Klik **"Deploy"**. Vercel akan membangun dan men-deploy aplikasi Anda sebagai **Serverless Function**.

Vercel akan secara otomatis melakukan *redeployment* setiap kali Anda melakukan *push* perubahan ke cabang utama (Continuous Deployment).

## 📄 Lisensi

Proyek ini dilisensikan di bawah **Lisensi MIT**.