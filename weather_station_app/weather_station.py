# Import the required libraries
from random import randint
from tkinter import *

import customtkinter

# Set default color themes and modes
customtkinter.set_appearance_mode("system")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
# customtkinter.set_window_scaling(10.0)
# customtkinter.set_widget_scaling(2.0)

# Define app window
app = customtkinter.CTk()
app.geometry("1450x900")
app.title("Weather Station")

# Variables
global last_uplink_time
last_uplink_time = IntVar()
last_uplink_time.set(randint(1, 10))
print(last_uplink_time.get())


# Functions: Menu
def duplicate_window():
    pass


def reconnect():
    connect()


def battery_life():
    pass


def soil_data():
    pass


def connect():
    hide_frames()
    global dashboard_frame
    dashboard_frame.pack(fill="both", expand=1)
    customtkinter.CTkLabel(dashboard_frame,
                           text="Welcome to the live dashboard viewer of Tektelic's Smart Agricultural Sensor",
                           font=("Open Sans", 40)).grid(pady=10, padx=60)
    customtkinter.CTkLabel(dashboard_frame, text="Last sensor update time is " + str(last_uplink_time.get()),
                           font=("Open Sans", 20)).grid(pady=10, padx=600, sticky=W)


def home_page():
    hide_frames()
    # Define frame for homepage
    global home_frame
    home_frame = customtkinter.CTkFrame(app, width=1450, height=900, fg_color="transparent",
                                        border_width=0)
    home_frame.pack(pady=50, fill=BOTH, expand=1, side=BOTTOM)
    customtkinter.CTkLabel(home_frame, text="Welcome to the Smart Agricultural Sensor \n Live Dashboard",
                           font=("Open Sans", 60)).pack(pady=10)
    customtkinter.CTkLabel(home_frame, text="By Adedolapo Adegboye", font=("Open Sans", 30)).pack(pady=40)
    customtkinter.CTkButton(home_frame, text="Click here to view live dashboard", command=connect).pack()


# Define Menu bar
menu = Menu(app)
app.config(menu=menu)

# Create menu bar
file_menu = Menu(menu)
sensor_menu = Menu(menu)
edit_menu = Menu(menu)
help_menu = Menu(menu)

# Add options for "File" menu option
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Home", command=home_page)
file_menu.add_command(label="Duplicate window", command=duplicate_window)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=app.quit)

# Add options for "Sensor" menu option
menu.add_cascade(label="Sensor", menu=sensor_menu)
sensor_menu.add_command(label="Reconnect", command=reconnect)
sensor_menu.add_command(label="Sensor Battery Life", command=battery_life)
sensor_menu.add_separator()
sensor_menu.add_command(label="Advanced: Soil Data", command=soil_data)

# Add options for "Edit" menu option
menu.add_cascade(label="Edit", menu=edit_menu)

# Add options for "Help" menu option
menu.add_cascade(label="Help", menu=help_menu)

# Instantiate all required frames for hide_frames() to work
home_frame = customtkinter.CTkFrame(app, width=1450, height=900, fg_color="transparent", border_width=0)
dashboard_frame = customtkinter.CTkFrame(app, width=1450, height=900, fg_color="transparent", border_width=0)


# Clear old frames when page is refreshed or new frame is loaded
def hide_frames():
    for widget in home_frame.winfo_children():
        widget.destroy()
    home_frame.pack_forget()
    for widget in dashboard_frame.winfo_children():
        widget.destroy()
    dashboard_frame.pack_forget()


# Initiate home page
home_page()

# Initiate app loop
app.mainloop()
