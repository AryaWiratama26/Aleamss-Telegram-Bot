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

def read(judul):
    conn, cursor = koneksi() 
    cursor.execute("SELECT note, waktu FROM data_notes WHERE judul = %s", (judul,))
    result = cursor.fetchall()    
    
    if result:
        return f"Note: {result[0][0]}\nWaktu: {result[0][1]}"
    else:
        return "Note tidak ada"
    
def all():
    conn, cursor = koneksi() 
    cursor.execute("SELECT * FROM data_notes")
    result = cursor.fetchall()
    
    hasil = ""
    hitung = 0
    for row in result:
        hitung += 1
        judul = row[1]
        note = row[2]
        waktu = row[3]
        hasil += f""""       
Data ke-{hitung}:
=================
Judul   : {judul}
Note    : {note}
Waktu   : {waktu}
================="""
        
    return hasil
        

conn, cursor = koneksi() 
conn.close()
