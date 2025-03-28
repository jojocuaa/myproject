# Library Management System

## Project Setup & Running Instructions

### Prerequisites
Pastikan Anda memiliki:
- Python (versi 3.8 atau lebih baru)
- Pip (Python package manager)
- Virtual environment (opsional tapi disarankan)

### 1. Clone Repository
Jika proyek ada di GitHub, clone dengan:
```bash
git clone https://github.com/jojocuaa/myproject.git
cd library-management
```

### 2. Buat Virtual Environment (Opsional)
```bash
python -m venv venv
source venv/bin/activate  # Untuk Mac/Linux
venv\Scripts\activate    # Untuk Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Konfigurasi Database
- Perbarui konfigurasi database di `src/config/database.py`.
- Jalankan migrasi jika ada:
```bash
python src/manage.py migrate
```

### 5. Menjalankan Aplikasi
```bash
python -m src.app
```

### 6. API Endpoints
| Method | Endpoint       | Description        |
|--------|--------------|-------------------|
| GET    | `/books`     | Mendapatkan daftar buku |
| POST   | `/books`     | Menambahkan buku baru |
| GET    | `/members`   | Mendapatkan daftar anggota |
| POST   | `/members`   | Menambahkan anggota baru |
| GET    | `/borrowings` | Mendapatkan daftar peminjaman |
| POST   | `/borrowings` | Membuat peminjaman baru |

### 7. Troubleshooting
Jika ada error `ModuleNotFoundError`, coba jalankan:
```bash
export PYTHONPATH=$(pwd)/src  # Untuk Mac/Linux
set PYTHONPATH=%CD%\src      # Untuk Windows
```
Lalu coba jalankan ulang aplikasi.

### 8. Stop Aplikasi
Jika ingin menghentikan aplikasi, tekan **CTRL+C** di terminal.

---

Sekarang aplikasi sudah siap digunakan! 🚀

