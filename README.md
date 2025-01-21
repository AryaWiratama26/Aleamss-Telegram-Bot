# Aleamss-Telegram-Bot

## Deskripsi
Aleams Bot adalah sebuah bot telegram yang melakukan create, update, remove data menggunakan `python` dan `mysql` yang dilengkapi dengan asistem AI menggunakan model `llama`

---


## Perintah dan penjelasan

| Perintah | Deskripsi |
|----------|-------------|
| `/hello` | Menyapa bot |
| `/tanya <pertanyaan>` | Bertanya ke AI |
| `/note "Judul" "Isi" "Tanggal"` | Menyimpan atau menambah catatan ke database |
| `/read <ID>` | Membaca catatan berdasarkan ID |
| `/list` | Menampilkan semua catatan |
| `/del <ID>` | Menghapus catatan berdasarkan ID |
| `/edit "ID" "Opsi" "Perubahan"` | Mengedit catatan berdasarkan ID (Opsi 1 : Judul, Opsi 2 : Note, Opsi 3 : Perubahan) |
| `/rm` | Menghapus semua catatan |
| `/help` | Menampilkan daftar perintah |

---

## Contoh

### 1. Menambah Catatan
```bash
/note "Hari Pahlawan" "Mengingat hari pahlawan dengan melaksanakan upacara bendera" "2024-11-10"
```
### 2. Membaca Catatan
```bash
/read 1 (Dengan ID = 1)
```
### 3. Menghapus Catatan
```bash
/del 1 (Dengan ID = 2)
```
### 4. Mengedit Catatan
```bash
/edit "1" "2" "Isi Baru"
```
_(Opsi: 1=Judul, 2=Isi, 3=Waktu)_

### 5. Menghapus Semua Catatan
```bash
/rm
```

---

## Teknologi yang dipakai dalam project ini
- Python
- Telegram Bot API
- Groq AI API
- MySQL

---

## Kontak
[aryawiratama2401@gmail.com](aryawiratama2401@gmail.com).

