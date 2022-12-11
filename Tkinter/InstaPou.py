import customtkinter
import tkinter


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x440")

def login():
    print("Username")


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx = 60, fill="both", expand=True("In english please"))

root.mainloop()