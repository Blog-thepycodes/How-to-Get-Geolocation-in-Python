import tkinter as tk
from tkinter import messagebox
from geopy.geocoders import Nominatim
 
 
class GeocodingApp(tk.Tk):
   def __init__(self):
       super().__init__()
 
 
       self.geocoder = Nominatim(user_agent="geoapp")
       self.title("Geocoding Application - The Pycodes")
       self.geometry("660x300")
 
 
       # Labels for user instruction
       tk.Label(self, text="Enter address for geocoding:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
       tk.Label(self, text="Enter latitude and longitude for reverse geocoding:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
       tk.Label(self, text="Latitude:").grid(row=3, column=0, padx=10, pady=5)
       tk.Label(self, text="Longitude:").grid(row=3, column=2, padx=10, pady=5)
 
 
       # Entry for Forward Geocoding
       self.address_entry = tk.Entry(self, width=40)
       self.address_entry.grid(row=1, column=0, columnspan=3, padx=10, sticky="we")
 
 
       # Entries for Reverse Geocoding
       self.latitude_entry = tk.Entry(self, width=20)
       self.latitude_entry.grid(row=4, column=0, padx=10, pady=5)
       self.longitude_entry = tk.Entry(self, width=20)
       self.longitude_entry.grid(row=4, column=2, padx=10, pady=5, sticky="we")
 
 
       # Buttons
       self.geocode_button = tk.Button(self, text="Geocode Address", command=self.geocode_address)
       self.geocode_button.grid(row=1, column=3, padx=10, pady=5)
       self.reverse_geocode_button = tk.Button(self, text="Reverse Geocode", command=self.reverse_geocode)
       self.reverse_geocode_button.grid(row=4, column=3, padx=10, pady=5)
 
 
       # Result Text Widget
       self.result_text = tk.Text(self, height=4, wrap='word')
       self.result_text.grid(row=5, column=0, columnspan=4, padx=10, pady=10, sticky="we")
 
 
   def geocode_address(self):
       address = self.address_entry.get()
       try:
           location = self.geocoder.geocode(address)
           if location:
               result = f"Address: {address}\nLatitude: {location.latitude}, Longitude: {location.longitude}"
               self.result_text.delete('1.0', tk.END)
               self.result_text.insert(tk.END, result)
           else:
               messagebox.showinfo("Result", "Address not found")
       except Exception as e:
           messagebox.showerror("Error", f"An error occurred: {e}")
 
 
   def reverse_geocode(self):
       latitude = self.latitude_entry.get()
       longitude = self.longitude_entry.get()
       try:
           location = self.geocoder.reverse(f"{latitude}, {longitude}")
           if location:
               result = f"Coordinates: {latitude}, {longitude}\nAddress: {location.address}"
               self.result_text.delete('1.0', tk.END)
               self.result_text.insert(tk.END, result)
           else:
               messagebox.showinfo("Result", "No address found for these coordinates")
       except Exception as e:
           messagebox.showerror("Error", f"An error occurred: {e}")
 
 
if __name__ == "__main__":
   app = GeocodingApp()
   app.mainloop()
