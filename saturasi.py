import tkinter as tk
from tkinter import messagebox

class AplikasiSaturasiOksigen:
    def __init__(self, master):
        self.master = master
        master.title("Pengukuran Saturasi Oksigen")

        self.label__instruksi = tk.Label(master, text="Masukkan nilai saturasi oksigen dalam darah:")
        self.label__instruksi.pack()

        self.entry__saturasi = tk.Entry(master)
        self.entry__saturasi.pack()

        self.tombol__hitung = tk.Button(master, text="Hitung", command=self.hitung__saturasi)
        self.tombol__hitung.pack()

    def hitung__saturasi(self):
        try:
            saturasi = float(self.entry__saturasi.get())
            if 0 <= saturasi <= 100:
                if saturasi >= 95:
                    hasil = "Tingkat saturasi oksigen normal."
                else:
                    hasil = "Tingkat saturasi oksigen rendah. Segera konsultasikan dengan dokter."
            else:
                hasil = "Masukkan nilai yang valid (0-100)."
        except ValueError:
            hasil = "Masukkan angka yang valid."

        messagebox.showinfo("Hasil Pengukuran", hasil)

if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiSaturasiOksigen(root)
    root.config(background="red")
    root.mainloop()