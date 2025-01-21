import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()
PASSWORD_DB = os.getenv('PASSWORD_DB')
DB_NAME = os.getenv('DB_NAME')
USER_DB = os.getenv("USER_DB")


def koneksi():
    conn = mysql.connector.connect(
        host="localhost",      
        user=USER_DB,            
        password=PASSWORD_DB,
        database=DB_NAME  
    )
    cursor = conn.cursor()
    
    return conn, cursor

def create_db() :
    conn, cursor = koneksi()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS data_notes(
        id_note INT AUTO_INCREMENT PRIMARY KEY,
        judul VARCHAR(30),
        note VARCHAR(100),
        waktu DATETIME
    )
    """)
    
    conn.commit()
    cursor.close()
    conn.close()
    

    
def add_data(judul, notes, waktu):
    conn, cursor = koneksi()
    cursor.execute("""
    INSERT INTO data_notes (judul, note, waktu) VALUES (%s, %s, %s)
    """, (judul, notes, waktu))
    conn.commit()


# create_db()
# add_data("Halow", "Kaciww", "2024-01-31")

def read(id_note):
    conn, cursor = koneksi() 
    cursor.execute("SELECT id_note, note, waktu FROM data_notes WHERE id_note = %s", (id_note,))
    result = cursor.fetchall()    
    
    if result:
        return f"ID : {result[0][0]}\nNote: {result[0][1]}\nWaktu: {result[0][2]}"
    else:
        return "Note tidak ada"
    
def all():
    conn, cursor = koneksi() 
    cursor.execute("SELECT * FROM data_notes")
    result = cursor.fetchall()
    
    if not result:
        return "Anda tidak punya catatan"
    
    hasil = ""
    hitung = 0
    for row in result:
        hitung += 1
        id = row[0]
        judul = row[1]
        note = row[2]
        waktu = row[3]
        hasil += f""""       
Data ke-{hitung}:
=================
ID      : {id}
Judul   : {judul}
Note    : {note}
Waktu   : {waktu}
================="""
        
    return hasil

def dell(id_note):
    conn, cursor = koneksi() 
    cursor.execute("DELETE FROM data_notes WHERE id_note = %s", (id_note,))
    conn.commit()
    cursor.close()
    conn.close()
    
    return f"Note dengan id : {id_note} telah di hapus"

def edit(id_note, op, upD):
    conn, cursor = koneksi() 
    
    if op == "1":
        cursor.execute("UPDATE data_notes SET judul = %s WHERE id_note = %s",(upD, id_note))
    elif op == "2":    
        cursor.execute("UPDATE data_notes SET note = %s WHERE id_note = %s",(upD, id_note))
    elif op == "3":
        cursor.execute("UPDATE data_notes SET waktu = %s WHERE id_note = %s",(upD, id_note))
    else:
        return "Opsi hanya 1 sampai 3"
        
    conn.commit()
    cursor.close()
    conn.close()
    
    return f"Meng-update data dengan id {id_note}"

def delDBAll():
    conn, cursor = koneksi() 
    cursor.execute("DELETE FROM data_notes")
    
    conn.commit()
    cursor.close()
    conn.close()
    
    return "Berhasil menghapus semua data"

conn, cursor = koneksi() 
conn.close()
