import psutil
import tkinter as tk
from tkinter import messagebox
from bd2 import insert_monitoring_data

class MONITOR:
    def __init__(self, master):
        self.master = master
        self.master.title("MONITOR DE USO DE CPU")
        self.master.config(bg='black')
         
        self.boton_guardar = tk.Button(self.master, text="Guardar", command=self.guardar)
        self.boton_guardar.pack(side=tk.BOTTOM, pady=10)

        self.usage = tk.StringVar()
        self.memory = tk.StringVar()
        self.storage = tk.StringVar()
        self.update_cpu_usage()
        self.update_memory_usage()
        self.update_storage_usage()
        
        self.label_usage = tk.Label(master, fg="white", background="black",textvariable=self.usage)
        self.label_usage.pack(pady=10)
        
        self.label_memory = tk.Label(master, fg="white", background="black", textvariable=self.memory)
        self.label_memory.pack(pady=10)
        
        self.label_storage = tk.Label(master, fg="white", background="black", textvariable=self.storage)
        self.label_storage.pack(pady=10)
    
    def update_cpu_usage(self):
        usage = psutil.cpu_percent()
        self.usage.set(f'Uso de CPU:{usage}%')
        self.master.after(1000, self.update_cpu_usage)
    
    def update_memory_usage(self):
        mem = psutil.virtual_memory()
        total = mem.total / (1024 ** 3)
        used = mem.used / (1024 ** 3)
        free = mem.free / (1024 ** 3)
        percent = mem.percent
      
        self.memory.set(f'Memoria RAM:\nTotal: {total:.2f} GB\nUsada: {used:.2f} GB\nLibre: {free:.2f} GB\n % RAM usada:{percent}%')
        self.master.after(1000, self.update_memory_usage)
    
    def update_storage_usage(self):
        disk = psutil.disk_usage('/')
        total = disk.total / (1024 ** 3)
        used = disk.used / (1024 ** 3)
        free = disk.free / (1024 ** 3)
        self.storage.set(f'Almacenamiento:\nTotal: {total:.2f} GB\nUsado: {used:.2f} GB\nLibre: {free:.2f} GB')
        self.master.after(1000, self.update_storage_usage)
    
    def guardar(self):
        messagebox.showinfo("Guardar", "Datos guardados correctamente")
        insert_monitoring_data()
    

if __name__ == "__main__":
    ventana = tk.Tk()
    ventana.geometry("100x275")
    monitor = MONITOR(ventana)
    ventana.mainloop()