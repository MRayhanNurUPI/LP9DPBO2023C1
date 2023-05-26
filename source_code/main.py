# Import Class dan Library yang Digunakan
import tkinter as tkinter
from apartemen import Apartemen
from rumah import Rumah
from indekos import Indekos
from tkinter import *
from PIL import ImageTk, Image

# List Data Hunian
hunians = []
hunians.append(Apartemen("Nelly Joy", 3, 3, "Melati", "apart1.jpg"))
hunians.append(Rumah("Sekar MK", 5, 2, 36, "rumah36-1.jpg"))
hunians.append(Indekos("Bp. Romi", "Cahya", "3A", "indekos1.jpg"))
hunians.append(Rumah("Satria", 1, 4, 60, "rumah60-1.jpg"))

# List objek ImageTk untuk ganti-ganti foto
images = []

# Window Detail
def details(index):
    top = Toplevel()
    top.geometry(f"{450}x{400}+{x}+{y-100}")
    top.title("Detail " + hunians[index].get_jenis() + " Page - LP9 - Muhammad Rayhan Nur")

    d_frame = LabelFrame(top, text="Data Residen", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)

    d_summary = Label(d_frame, font="Helvetica 9", text="== Data Lengkap Hunian ==\n" + hunians[index].get_detail() + "\n" + hunians[index].get_summary() + "\n" + hunians[index].get_dokumen(), anchor="w", justify=LEFT).grid(row=1, column=1, sticky="w")

    img = Image.open("assets/images/" + hunians[index].get_foto())
    img = img.resize((150, 150))  
    photo_img = ImageTk.PhotoImage(img)
    images.append(photo_img)
    img_label = Label(d_frame, image=photo_img, borderwidth=1, relief="solid")
    
    img_label.grid(row=0, column=1)


    btn = LabelFrame(top, padx=0, pady=0)
    btn.pack(padx=10, pady=10)
    b_close = Button(btn, text="Tutup", command=top.destroy)
    b_close.grid(row=0, column=0)

# Window Page List Data
def showData():
    window.destroy()
    root = Tk()
    root.title("Show Data Page - LP9 - Muhammad Rayhan Nur")
    root.geometry(f"{600}x{300}+{x-50}+{y+50}")
    root.configure(bg="green")

    frame = LabelFrame(root, text="Data Seluruh Residen", padx=10, pady=10, font="Montserrat 10 bold")
    frame.pack(padx=10, pady=10)

    opts = LabelFrame(root, padx=10, pady=10)
    opts.pack(padx=10, pady=10)

    # b_add = Button(opts, text="Tambah Data", state="disabled")
    # b_add.grid(row=0, column=0)

    # Button Exit dari Data Page (sekaligus menutup program)
    b_exit = Button(opts, text="Keluar", activebackground="#f54242", activeforeground="#fff", command=root.destroy, bg="#f78181")
    b_exit.grid(row=0, column=1)

    # Header Tabel
    idx = Label(frame, text="No", width=5, borderwidth=1, relief="solid", font='Helvetica 8 bold')
    idx.grid(row=0, column=0)

    type = Label(frame, text="Jenis Hunian", width=15, borderwidth=1, relief="solid", font='Helvetica 8 bold')
    type.grid(row=0, column=1)

    name = Label(frame, text=" Nama Penghuni/Pemilik", width=40, borderwidth=1, relief="solid", font='Helvetica 8 bold')
    name.grid(row=0, column=2)

    aksi = Label(frame, text="Aksi", width=10, borderwidth=1, relief="solid", font='Helvetica 8 bold')
    aksi.grid(row=0, column=3)

    # Perulangan untuk mengisi data tabel hunian
    for index, h in enumerate(hunians):
        idx = Label(frame, text=str(index+1), width=5, borderwidth=1, relief="solid")
        idx.grid(row=index+1, column=0)

        type = Label(frame, text=h.get_jenis(), width=15, borderwidth=1, relief="solid")
        type.grid(row=index+1, column=1)

        if h.get_jenis() != "Indekos": 
            name = Label(frame, text=" " + h.get_nama_pemilik(), width=40, borderwidth=1, relief="solid", anchor="w")
            name.grid(row=index+1, column=2)
        else:
            name = Label(frame, text=" " + h.get_nama_penghuni(), width=40, borderwidth=1, relief="solid", anchor="w")
            name.grid(row=index+1, column=2)

        b_detail = Button(frame, text="Lihat Detail", command=lambda index=index: details(index), bg="#fff67d")
        b_detail.grid(row=index+1, column=3)

    root.mainloop()

# Window Landing Page
window = Tk()
window.title("Landing Page - LP9 - Muhammad Rayhan Nur")

# Set Ukuran Window
lebar = 500
tinggi = 400

# Set letak Window saat Start
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()
x = int(screenWidth/2 - lebar/2)
y = int(screenHeight/2 - tinggi/2)
window.geometry(f"{lebar}x{tinggi}+{x}+{y}")

# Set Background Window
window.configure(bg="green")

# Set Window Landing Page Tidak Bisa di-Resize
window.resizable(False, False)

# Set Grid Window (2 Baris, 3 Kolom) -> Baris 1 untuk Label dan Foto, Baris 2 untuk Tombol Opsi
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)

# Buat Frame untuk Tempat Foto pada Window Landing Page dan Letaknya
frame = Frame(window, width=600, height=400)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.4)

# Buat objek tkinter ImageTk
img = Image.open("assets/images/building.jpg")
img = img.resize((300,200))
imgTk = ImageTk.PhotoImage(img)
images.append(imgTk)

# Buat widget label untuk tempat menampilkan gambar hunian
labelImg = Label(frame, image = imgTk)
labelImg.pack()

# Buat widget Label untuk kalimat sapaan dalam Landing Page dan Letaknya
labelTitle = Label(text="Selamat Datang di LP9-nya Rayhan!", font="Poppins 12", bg="green", fg="white")
labelTitle.pack()
labelTitle.place(anchor='center', relx=0.5, rely=0.1)

# Buat widget Label untuk Copyright dalam Landing Page dan Letaknya
labelCopyright = Label(text="Latihan Praktikum 9 DPBO | 2100192 | Muhammad Rayhan Nur | Ilmu Komputer C1", font="Poppins 8", bg="green", fg="white")
labelCopyright.pack()
labelCopyright.place(anchor='center', relx=0.5, rely=0.95)

# Button di Landing Page yang apabila di-klik akan membuka Window yang berisi List Data Hunian
btn_toData = Button(text="Lihat Data", activebackground="#98f542", activeforeground="#000", command=showData, bg="#26C281")
btn_toData.grid(row=1, column=0, sticky="we", padx=50)

# Button di Landing Page yang apabila di-klik akan menutup window landing page sekaligus mengakhiri program
btn_toClose = Button(text="Keluar", activebackground="#f54242", activeforeground="#fff", command=window.destroy, bg="#f78181")
btn_toClose.grid(row=1, column=2, sticky="we", padx=50)

# Menjalankan Looping untuk Window Landing Page sebagai Window pertama yang dijalankan
window.mainloop()