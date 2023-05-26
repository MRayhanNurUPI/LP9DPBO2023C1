 # Buat Frame untuk Tempat Foto pada Window Landing Page dan Letaknya
    frame = Frame(top, width=100, height=100)
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.4)

    # Buat objek tkinter ImageTk
    img = Image.open("assets/images/" + hunians[index].get_foto())
    img = img.resize((300,200))
    imgTk = ImageTk.PhotoImage(img)

    # Buat widget label untuk tempat menampilkan gambar landing page
    labelImg = Label(frame, image = imgTk)
    labelImg.pack()