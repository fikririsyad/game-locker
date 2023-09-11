# Game Locker 🎮
## [Link to App](https://game-locker.adaptable.app/main/)
##  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
### Checklist 1: Membuat sebuah proyek Django baru
1. Membuat direktori baru untuk proyek ini dengan nama `game_locker`.
1. Membuka terminal dan pindah ke direktori tersebut.
1. Membuat berkas `requirements.txt` yang berisikan beberapa *dependencies* sebagai berikut.
    ```
    django
    gunicorn
    whitenoise
    psycopg2-binary
    requests
    urllib3
    ```
1. Membuat *virtual environment* dengan menjalankan perintah `python -m venv env`
1. Mengaktifkan *virtual environment* dengan perintah `source env/bin/activate`
1. Menginstalasi *dependencies* di atas dengan perintah `pip install -r requirements.txt`
1. Membuat projek Django baru dengan nama `game_locker` melalui perintah `django-admin startproject game_locker .`
1. Menambahkan `*` pada `ALLOWED_HOSTS` di `settings.py` untuk keperluan deployment.
    ```
    ...
    ALLOWED_HOSTS = ["*"]
    ...
    ```
1. Tambahkan juga berkas `.gitignore` sebelum melakukn *add*, *commit*, dan *push*. Untuk berkas `.gitignore` yang digunakan dalam proyek ini mengikuti template [berikut](https://pbp-fasilkom-ui.github.io/ganjil-2024/docs/tutorial-0#tutorial-unggah-proyek-ke-repositori-github).

### Checklist 2: Membuat aplikasi `main` pada proyek tersebut
1. Menjalankan perintah ini untuk membuat aplikasi baru bernama main `main`:
    ```
    python manage.py startapp main
    ```
1. Tambahkan aplikasi main ke dalam proyek:
    - Buka berkas `settings.py` di dalam direktori proyek `game_locker`
    - Temukan variabel `INSTALLED_APPS`
    - Daftarkan `main` ke dalam daftar aplikasi yang ada:
        ```
        INSTALLED_APPS = [
            ...,
            'main',
            ...
        ]
        ```

### Checklist 3: Melakukan *routing* pada proyek agar dapat menjalankan aplikasi `main`.
#### * Dilakukan nanti bersamaan dengan *routing* pada `urls.py` di direktori `main`
1. Bukalah berkas `urls.py` di dalam direktori `game_locker` dan isi berkas dengan kode berikut.
    ```
    ...
    from django.urls import path, include

    urlpatterns = [
        ...
        path('main/', include('main.urls')),
        ...
    ]
    ```

### Checklist 4: Membuat model pada aplikasi `main` dengan nama *Item* dan memiliki atribut wajib *name*, *amount*, *description*.
1. Membuka berkas `models.py` di dalam direktori `main`.
1. Mengisi `models.py` dengan kode berikut.
    ```
    from django.db import models

    class Item(models.Model):
        name = models.CharField(max_length=255) 
        amount = models.IntegerField()
        description = models.TextField()
        price = models.IntegerField()
        genre = models.CharField(max_length=30)
        date_added = models.DateField(auto_now_add=True)
    ```
1. Menjalankan perintah `python manage.py makemigrations` untuk membuat migrasi model. Berkas migrasi yang berisi perubahan model belum diaplikasikan ke dalam basis data.
1. Menjalankan perintah `python manage.py migrate` untuk menerapkan migrasi ke dalam basis data lokal.

### Checklist 5: Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
1. Membuat direktori bernama `templates` di dalam direktori `main`
1. Membuat berkas `main.html` di dalam direktori `templates` dan diisi dengan teks berikut.
    ```
    <h1>Game Locker</h1>
    <p>Name: {{ name }}</p>
    <p>Class: {{ class }}</p>
    ```
1. Membuka berkas `views.py` di dalam direktori `main` dan isi dengan kode berikut.
    ```
    from django.shortcuts import render

    def show_main(request):
        context = {
            'name': 'Fikri Risyad Indratno',
            'class': 'PBP C'
        }
    
        return render(request, "main.html", context)
    ```

### Checklist 6: Membuat sebuah *routing* pada `urls.py` aplikasi `main` untuk memetakan fungsi yang telah dibuat pada `views.py`.
1. Membuat berkas `urls.py` di dalam direktori `main`.
2. Mengisi `urls.py` dengan kode berikut.
    ```
    from django.urls import path
    from main.views import show_main

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
    ]
    ```
### Checklist 7: Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat
1. *Login* ke Adaptable menggunakan akun GitHub.
1. Klik `New App` dan pilih *Connect an Existing Repository*.
1. Klik repositori proyek ini, yaitu `fikririsyad/game-locker` dan pilih *branch* main.
1. Pilih `Python App Template` sebagai *deploy template*.
1. Pilih `PostgreSQL` sebagai *Database Type*.
1. Pilih versi Python yang dipakai dalam proyek ini, yaitu `3.11` dan masukkan `python manage.py migrate && gunicorn game_locker.wsgi` pada bagian `Start Command`.
1. Masukkan nama aplikasi.
1. Centang bagian `HTTP Listener on PORT` dan klik `Deploy App` untuk memulai proses `deployment` aplikasi.

## Buatlah bagan yang berisi *request client* ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas `html`.

