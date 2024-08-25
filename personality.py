import tkinter as tk
from tkinter import messagebox

# Function to handle booking process
def pesan():
    try:
        jmlh_item = int(jmlh_item_entry.get())
        num_array = []
        num = int(num_barang_entry.get())
        for i in range(num):
            n = f"Orang ke {i + 1}"
            num_array.append(n)
        total_laundry = jmlh_item * harga
        result = f"Nama Pemesan:\n" + "\n".join(num_array) + f"\n\nTotal Harga: Rp.{total_laundry:,}"
        messagebox.showinfo("Pemesanan Berhasil", result)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# Function to select destination and price
def pilih_item():
    global harga
    item = int(tujuan_var.get())
    if item == 1:
        harga = 10000
    elif item == 2:
        harga = 15000
    elif item == 3:
        harga = 18000
    elif item == 4:
        harga = 20000
    else:
        harga = 0
    pesan()

# Main window
app = tk.Tk()
app.title("Spideric Laundry")
app.configure(bg='#960019')  # Red background

# Title Label
title_label = tk.Label(app, text="Spideric Laundry", font=("Helvetica", 16, "bold"), bg='#000080', fg='white', pady=10)
title_label.grid(row=0, column=0, columnspan=2, sticky="ew")

# Destination Selection
tk.Label(app, text="Select your item:", font=("Helvetica", 12), bg='#CD5C5C', fg='white').grid(row=1, column=0, sticky="w", padx=10, pady=5)
tujuan_var = tk.IntVar()
tk.Radiobutton(app, text="Shirt", variable=tujuan_var, value=1, font=("Helvetica", 12), bg='#CD5C5C', fg='white', selectcolor='#0000FF').grid(row=2, column=0, sticky="w", padx=10)
tk.Radiobutton(app, text="Doll", variable=tujuan_var, value=2, font=("Helvetica", 12), bg='#CD5C5C', fg='white', selectcolor='#0000FF').grid(row=3, column=0, sticky="w", padx=10)
tk.Radiobutton(app, text="Bedcover", variable=tujuan_var, value=3, font=("Helvetica", 12), bg='#CD5C5C', fg='white', selectcolor='#0000FF').grid(row=4, column=0, sticky="w", padx=10)
tk.Radiobutton(app, text="Shoe", variable=tujuan_var, value=4, font=("Helvetica", 12), bg='#CD5C5C', fg='white', selectcolor='#0000FF').grid(row=5, column=0, sticky="w", padx=10)

# Input Fields for Number of Items and Quantity
tk.Label(app, text="Jumlah Item:", font=("Helvetica", 12), bg='#CD5C5C', fg='white').grid(row=6, column=0, sticky="w", padx=10, pady=5)
jmlh_item_entry = tk.Entry(app, font=("Helvetica", 12))
jmlh_item_entry.grid(row=6, column=1, padx=10, pady=5)

tk.Label(app, text="Jumlah Orang:", font=("Fira", 12), bg='#CD5C5C', fg='white').grid(row=7, column=0, sticky="w", padx=10, pady=5)
num_barang_entry = tk.Entry(app, font=("Fira", 12))
num_barang_entry.grid(row=7, column=1, padx=10, pady=5)

# Button to Confirm Booking
pesan_button = tk.Button(app, text="Pesan", command=pilih_item, font=("Helvetica", 12, "bold"), bg='#000080', fg='white', padx=10, pady=5)
pesan_button.grid(row=8, column=0, columnspan=2, pady=10)

# Adjust spacing and alignment
for widget in app.winfo_children():
    widget.grid_configure(padx=10, pady=5)

app.mainloop()
