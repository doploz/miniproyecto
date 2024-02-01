import psutil
import tkinter as tk
import geopy.geocoders

class CPU_Monitor:
    def __init__(self, master):
        self.master = master
        self.master.title("MONITOR DE USO DE CPU")
        
        self.usage = tk.StringVar()
        self.update_cpu_usage()
        
        self.label_location = tk.Label(master, fg="white", background="black", textvariable=self.location)
        self.label_location.pack(pady=10)
        
        self.label = tk.Label(master, fg="blue", textvariable=self.usage)
        self.label.pack(pady=20)
        
    def update_location(self):
        geolocator = geopy.geocoders.Nominatim(user_agent="myGeocoder")
        location = geolocator.reverse("0.0, 0.0", exactly_one=True)
        self.location.set(f'Ubicación: {location.latitude}, {location.longitude}')
        self.master.after(1000, self.update_location)    
        
    def update_cpu_usage(self):
        usage = psutil.cpu_percent()
        self.usage.set(f'Uso de CPU:{usage}%')
        
        self.master.after(1000, self.update_cpu_usage)
        
        
if __name__ == "__main__":
    ventana = tk.Tk()
    ventana.geometry("300x300")
    monitor = CPU_Monitor(ventana)
    ventana.mainloop()
    
