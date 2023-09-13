# Game Locker 🎮
#### Tautan aplikasi: https://game-locker.adaptable.app/main/
<hr>

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
    - Buka berkas `settings.py` di dalam direktori proyek `game_locker`.
    - Temukan variabel `INSTALLED_APPS`.
    - Daftarkan `main` ke dalam daftar aplikasi yang ada:
        ```
        INSTALLED_APPS = [
            ...,
            'main',
            ...
        ]
        ```

### Checklist 3: Melakukan *routing* pada proyek agar dapat menjalankan aplikasi `main`
#### * Dilakukan nanti bersamaan dengan *routing* pada `urls.py` aplikasi `main`.
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

### Checklist 4: Membuat model pada aplikasi `main` dengan nama *Item* dan memiliki atribut wajib *name*, *amount*, *description*
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

### Checklist 5: Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu
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
![Bagan Django](./images/bagan_django.png)
### Penjelasan
1. *User* mengirimkan HTTP *Request* ke aplikasi Django.
2. Oleh `urls.py`, *request* tersebut akan diteruskan ke `views.py` yang sesuai.
3. `views.py` akan menggunakan `models.py` jika perlu mengakses data dari *database*.
4. Setelah selesai memproses *request*, `views.py` akan me-*render* HTML *template*.
5. HTML yang sudah ter-*render* kemudian akan dikembalikan ke *user* sebagai HTTP *response*.

## Jelaskan mengapa kita menggunakan ***virtual environment***? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan ***virtual environment***?
*Virtual environment* dibutuhkan dalam pembuatan aplikasi web berbasis Django untuk mengisolasi Python dan *dependencies* yang diperlukan. Dengan menggunakan *virtual environment*, Python dan *dependencies* yang kita perlukan tidak tercampur dengan Python dan *packages* dari *base environment*. Kita sebenarnya bisa saja membuat aplikasi web Django tanpa menggunakan *virtual environment*. Akan tetapi, agar lebih mudah mengelola Python dan *dependencies*-nya, lebih baik tetap menggunakan *virtual environment*.

## Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
### Penjelasan
1. MVC atau *Model*-*View*-*Controller*:

    - ***Model***</br>
        Komponen *Model* berfungsi untuk membuat logika data aplikasi dan mengelola datanya. 
    - ***View***</br>
        Komponen *View* berisikan logika dan struktur tampilan data yang akan dilihat.
    - ***Controller***</br>
        Komponen *Controller* berfungsi untuk menangani *request* dan memberikan *response*. *Controller* bertindak sebagai penghubung antara *Model* dan *View*. Menentukan View apa yang akan di-*render*.

1. MVT atau *Model*-*View*-*Template*:

    - ***Model***</br>
        Komponen *Model* berfungsi untuk membuat logika data aplikasi dan mengelola datanya.
    - ***View***</br>
        Komponen *View* berfungsi untuk menangani *request* dan memberikan *response*.
    - ***Template***</br>
        Komponen *Template* mendefinisikan struktur HTML yang nantinya akan di-*render*.

1. MVVM atau *Model*-*View*-*ViewModel*:

    - ***Model***</br>
        Komponen *Model* berfungsi untuk membuat logika data aplikasi dan mengelola datanya.
    - ***View***</br>
        Komponen *View* berkaitan dengan struktur dan tampilan data yang akan dilihat. *View* berinteraksi dengan *ViewModel* melalui *data binding*.
    - ***ViewModel***</br>
        Komponen *ViewModel* bertindak sebagai penghubung antara *Model* dan *View*. *ViewModel* berisikan logika utama bisnis.

### Perbedaan
- Perbedaan utama antara MVC dan MVT adalah pada MVC kita harus membuat semua kode untuk kontrol. Pada MVT, bagian *controller* sudah ditangani oleh *framework*.
- Perbedaan utama antara MVC dan MVVM adalah pada MVVM, *View* dapat berinteraksi langsung dengan propertinya di *ViewModel* menggunakan *data binding*.