# Import the required tkinter libraries
from tkinter import *
import customtkinter

# Import the required libraries for weather data
import requests
import json
import time


########################################### Real time variables #######################################
def get_data():
    # last Temperature update and update time
    url = "https://api.tago.io/data?variable=ambient_temperature&device=64a916f7179863000942a6c5&query=last_item&qty=1&details=false"
    payload = {}
    headers = {
        'device-token': 'a0388c6e-118d-47fd-a2a5-0d12a3bebd7c'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
    temperature_response = json.loads(response.text)
    global temperature_value
    temperature_value = temperature_response['result'][0]['value']
    global temperature_update_time
    temperature_update_time = temperature_response['result'][0]['time']
    print("Temp: ", temperature_value, type(temperature_value))
    print("Temp update time: ", temperature_update_time, type(temperature_update_time))

    # last Humidity update and update time
    url = "https://api.tago.io/data?variable=relative_humidity&device=64a916f7179863000942a6c5&query=last_item&qty=1&details=false"
    payload = {}
    headers = {
        'device-token': 'a0388c6e-118d-47fd-a2a5-0d12a3bebd7c'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
    humidity_response = json.loads(response.text)
    global humidity_value
    humidity_value = humidity_response['result'][0]['value']
    global humidity_update_time
    humidity_update_time = humidity_response['result'][0]['time']
    print("Humidity: ", humidity_value, type(humidity_value))
    print("Humidity update time: ", humidity_update_time, type(humidity_update_time))

    # last Pressure update and update time
    url = "https://api.tago.io/data?variable=rfu_2&device=64a916f7179863000942a6c5&query=last_item&qty=1&details=false"
    payload = {}
    headers = {
        'device-token': 'a0388c6e-118d-47fd-a2a5-0d12a3bebd7c'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
    pressure_response = json.loads(response.text)
    global pressure_value
    global pressure_update_time
    pressure_value = pressure_response['result'][0]['value']
    pressure_update_time = pressure_response['result'][0]['time']
    print("pressure: ", pressure_value, type(pressure_value))
    print("pressure update time: ", pressure_update_time, type(pressure_update_time))

    # last Illuminance update and update time
    url = "https://api.tago.io/data?variable=light_intensity&device=64a916f7179863000942a6c5&query=last_item&qty=1&details=false"
    payload = {}
    headers = {
        'device-token': 'a0388c6e-118d-47fd-a2a5-0d12a3bebd7c'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
    illuminance_response = json.loads(response.text)
    global illuminance_value
    global illuminance_update_time
    illuminance_value = illuminance_response['result'][0]['value']
    illuminance_value = str(illuminance_value)
    illuminance_update_time = illuminance_response['result'][0]['time']
    print("illuminance: ", illuminance_value, type(illuminance_value))
    print("illuminance update time: ", illuminance_update_time, type(illuminance_update_time))

    # last 1-wire update and update time
    url = "https://api.tago.io/data?variable=input4_temperature&device=64a916f7179863000942a6c5&query=last_item&qty=1&details=false"
    payload = {}
    headers = {
        'device-token': 'a0388c6e-118d-47fd-a2a5-0d12a3bebd7c'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
    onewire_temperature_response = json.loads(response.text)
    global onewire_temperature_value
    onewire_temperature_value = onewire_temperature_response['result'][0]['value']
    global onewire_temperature_update_time
    onewire_temperature_value = str(onewire_temperature_value)
    onewire_temperature_update_time = onewire_temperature_response['result'][0]['time']
    print("onewire_temperature: ", onewire_temperature_value, type(onewire_temperature_value))
    print("onewire_temperature update time: ", onewire_temperature_update_time, type(onewire_temperature_update_time))

    # last Thermistor Temperature update and update time
    url = "https://api.tago.io/data?variable=input3_voltage_to_temp&device=64a916f7179863000942a6c5&query=last_item&qty=1&details=false"
    payload = {}
    headers = {
        'device-token': 'a0388c6e-118d-47fd-a2a5-0d12a3bebd7c'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
    thermistor_temperature_response = json.loads(response.text)
    global thermistor_temperature_value
    global thermistor_temperature_update_time
    thermistor_temperature_value = thermistor_temperature_response['result'][0]['value']
    thermistor_temperature_value = str(thermistor_temperature_value)
    thermistor_temperature_update_time = thermistor_temperature_response['result'][0]['time']
    print("thermistor_temperature: ", thermistor_temperature_value, type(thermistor_temperature_value))
    print("thermistor_temperature update time: ", thermistor_temperature_update_time,
          type(thermistor_temperature_update_time))

    # last Sensor battery (%) update and update time
    url = "https://api.tago.io/data?variable=rem_batt_capacity&device=64a916f7179863000942a6c5&query=last_item&qty=1&details=false"
    payload = {}
    headers = {
        'device-token': 'a0388c6e-118d-47fd-a2a5-0d12a3bebd7c'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
    battery_capacity_percentage_response = json.loads(response.text)
    global battery_capacity_percentage_value
    global battery_capacity_percentage_update_time
    battery_capacity_percentage_value = battery_capacity_percentage_response['result'][0]['value']
    battery_capacity_percentage_value = str(battery_capacity_percentage_value)
    battery_capacity_percentage_update_time = battery_capacity_percentage_response['result'][0]['time']
    print("battery_capacity_percentage: ", battery_capacity_percentage_value, type(battery_capacity_percentage_value))
    print("battery_capacity_percentage update time: ", battery_capacity_percentage_update_time,
          type(battery_capacity_percentage_update_time))

    # last Sensor battery (days) update and update time
    url = "https://api.tago.io/data?variable=rem_batt_days&device=64a916f7179863000942a6c5&query=last_item&qty=1&details=false"
    payload = {}
    headers = {
        'device-token': 'a0388c6e-118d-47fd-a2a5-0d12a3bebd7c'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
    battery_capacity_days_response = json.loads(response.text)
    global battery_capacity_days_value
    global battery_capacity_days_update_time
    battery_capacity_days_value = battery_capacity_days_response['result'][0]['value']
    battery_capacity_days_value = str(battery_capacity_days_value)
    battery_capacity_days_update_time = battery_capacity_days_response['result'][0]['time']
    print("battery_capacity_days: ", battery_capacity_days_value, type(battery_capacity_days_value))
    print("battery_capacity_days update time: ", battery_capacity_days_update_time,
          type(battery_capacity_days_update_time))


get_data()

########################################### APP CODE #######################################

# Set default color themes and modes for the app
customtkinter.set_appearance_mode("system")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
customtkinter.set_window_scaling(1.0)
customtkinter.set_widget_scaling(1.0)

# Define app window properties
app = customtkinter.CTk()
app.geometry("1400x900")
app.title("Ade's Weather Station")


# Define functions for app menu

def refresh():
    get_data()
    time.sleep(6)
    hide_frames()
    connect()


def connect():
    hide_frames()
    # Header frame
    global dashboard_header_frame
    dashboard_header_frame = customtkinter.CTkFrame(app, width=400, height=100, fg_color="transparent",
                                                    border_width=0)
    dashboard_header_frame.grid(row=0, column=0, padx=1, pady=1, sticky="SEWN", columnspan=3, rowspan=1)
    app.grid_columnconfigure(0, weight=1)
    customtkinter.CTkLabel(dashboard_header_frame,
                           text="Welcome to the live dashboard viewer of \n Tektelic's Smart Agricultural Sensor",
                           font=("Open Sans", 20)).pack(pady=50, padx=10)

    # Variable frames
    variable_text_frame = customtkinter.CTkFrame(app, width=40, height=10, fg_color="black",
                                                 border_width=0)
    variable_text_frame.grid(row=1, column=0, padx=1, pady=1, sticky="ESNW")
    customtkinter.CTkLabel(variable_text_frame, text="Sensor Type",
                           font=("Open Sans", 12), anchor="center").grid(row=0, column=0, pady=15, padx=1)

    temperature_text_frame = customtkinter.CTkFrame(app, width=400, height=100, fg_color="brown",
                                                    border_width=0)
    temperature_text_frame.grid(row=2, column=0, padx=1, pady=1, sticky="ESNW")
    customtkinter.CTkLabel(temperature_text_frame, text="Ambient Temperature (°C)",
                           font=("Open Sans", 12)).grid(row=0, column=0, pady=15, padx=1)

    humidity_text_frame = customtkinter.CTkFrame(app, width=400, height=100, fg_color="brown",
                                                 border_width=0)
    humidity_text_frame.grid(row=3, column=0, padx=1, pady=1, sticky="ESNW")
    customtkinter.CTkLabel(humidity_text_frame, text="Humidity (%)",
                           font=("Open Sans", 12)).grid(row=0, column=0, pady=15, padx=1)

    pressure_text_frame = customtkinter.CTkFrame(app, width=400, height=100, fg_color="brown",
                                                 border_width=0)
    pressure_text_frame.grid(row=4, column=0, padx=1, pady=1, sticky="ESNW")
    customtkinter.CTkLabel(pressure_text_frame, text="Pressure (hPa)",
                           font=("Open Sans", 12)).grid(row=0, column=0, pady=15, padx=1)

    illuminance_text_frame = customtkinter.CTkFrame(app, width=400, height=100, fg_color="brown",
                                                    border_width=0)
    illuminance_text_frame.grid(row=5, column=0, padx=1, pady=1, sticky="ESNW")
    customtkinter.CTkLabel(illuminance_text_frame, text="Illuminance (lx)",
                           font=("Open Sans", 12)).grid(row=0, column=0, pady=15, padx=1)

    one_wire_temperature_text_frame = customtkinter.CTkFrame(app, width=400, height=100, fg_color="brown",
                                                             border_width=0)
    one_wire_temperature_text_frame.grid(row=6, column=0, padx=1, pady=1, sticky="ESNW")
    customtkinter.CTkLabel(one_wire_temperature_text_frame, text="1-wire Temperature Probe (°C)",
                           font=("Open Sans", 12)).grid(row=0, column=0, pady=15, padx=1)

    thermistor_temperature_text_frame = customtkinter.CTkFrame(app, width=400, height=100, fg_color="brown",
                                                               border_width=0)
    thermistor_temperature_text_frame.grid(row=7, column=0, padx=1, pady=1, sticky="ESNW")
    customtkinter.CTkLabel(thermistor_temperature_text_frame, text="Thermistor Temperature Probe (°C)",
                           font=("Open Sans", 12)).grid(row=0, column=0, pady=15, padx=1)

    battery_capacity_percentage_text_frame = customtkinter.CTkFrame(app, width=400, height=100, fg_color="brown",
                                                                    border_width=0)
    battery_capacity_percentage_text_frame.grid(row=8, column=0, padx=1, pady=1, sticky="ESNW")
    customtkinter.CTkLabel(battery_capacity_percentage_text_frame, text="Remaining Battery Capacity (%)",
                           font=("Open Sans", 12)).grid(row=0, column=0, pady=15, padx=1)

    battery_capacity_days_text_frame = customtkinter.CTkFrame(app, width=400, height=100, fg_color="brown",
                                                              border_width=0)
    battery_capacity_days_text_frame.grid(row=9, column=0, padx=1, pady=1, sticky="ESNW")
    customtkinter.CTkLabel(battery_capacity_days_text_frame, text="Remaining Battery Capacity (days)",
                           font=("Open Sans", 12)).grid(row=0, column=0, pady=15, padx=1)

    # Value frames
    variable_value_frame = customtkinter.CTkFrame(app, width=400, height=100, fg_color="black",
                                                  border_width=0)
    variable_value_frame.grid(row=1, column=1, padx=1, pady=1, sticky="ESNW")
    app.grid_columnconfigure(1, weight=2)
    customtkinter.CTkLabel(variable_value_frame, text="Sensor Value",
                           font=("Open Sans", 12)).grid(row=0, column=0, pady=15, padx=1)

    temperature_value_frame = customtkinter.CTkFrame(app, width=400, height=100, fg_color="green",
                                                     border_width=0)
    temperature_value_frame.grid(row=2, column=1, padx=1, pady=1, sticky="ESNW")
    customtkinter.CTkLabel(temperature_value_frame, text=temperature_value,
                           font=("Open Sans", 12)).grid(row=0, column=0, pady=15, padx=1)

    humidity_value_frame = customtkinter.CTkFrame(app, width=400, height=100, fg_color="green",
                                                  border_width=0)
    humidity_value_frame.grid(row=3, column=1, padx=1, pady=1, sticky="ESNW")
    customtkinter.CTkLabel(humidity_value_frame, text=humidity_value,
                           font=("Open Sans", 12)).grid(row=0, column=0, pady=15, padx=1)

    pressure_value_frame = customtkinter.CTkFrame(app, width=400, height=100, fg_color="green",
                                                  border_width=0)
    pressure_value_frame.grid(row=4, column=1, padx=1, pady=1, sticky="ESNW")
    customtkinter.CTkLabel(pressure_value_frame, text=pressure_value,
                           font=("Open Sans", 12)).grid(row=0, column=0, pady=15, padx=1)

    illuminance_value_frame = customtkinter.CTkFrame(app, width=400, height=100, fg_color="green",
                                                     border_width=0)
    illuminance_value_frame.grid(row=5, column=1, padx=1, pady=1, sticky="ESNW")
    customtkinter.CTkLabel(illuminance_value_frame, text=illuminance_value,
                           font=("Open Sans", 12)).grid(row=0, column=0, pady=15, padx=1)

    one_wire_temperature_value_frame = customtkinter.CTkFrame(app, width=400, height=100, fg_color="green",
                                                              border_width=0)
    one_wire_temperature_value_frame.grid(row=6, column=1, padx=1, pady=1, sticky="ESNW")
    customtkinter.CTkLabel(one_wire_temperature_value_frame, text=onewire_temperature_value,
                           font=("Open Sans", 12)).grid(row=0, column=0, pady=15, padx=1)

    thermistor_temperature_value_frame = customtkinter.CTkFrame(app, width=400, height=100, fg_color="green",
                                                                border_width=0)
    thermistor_temperature_value_frame.grid(row=7, column=1, padx=1, pady=1, sticky="ESNW")
    customtkinter.CTkLabel(thermistor_temperature_value_frame, text=thermistor_temperature_value,
                           font=("Open Sans", 12)).grid(row=0, column=0, pady=15, padx=1)

    battery_capacity_percentage_value_frame = customtkinter.CTkFrame(app, width=400, height=100, fg_color="green",
                                                                     border_width=0)
    battery_capacity_percentage_value_frame.grid(row=8, column=1, padx=1, pady=1, sticky="ESNW")
    customtkinter.CTkLabel(battery_capacity_percentage_value_frame, text=battery_capacity_percentage_value,
                           font=("Open Sans", 12)).grid(row=0, column=0, pady=15, padx=1)

    battery_capacity_days_value_frame = customtkinter.CTkFrame(app, width=400, height=100, fg_color="green",
                                                               border_width=0)
    battery_capacity_days_value_frame.grid(row=9, column=1, padx=1, pady=1, sticky="ESNW")
    customtkinter.CTkLabel(battery_capacity_days_value_frame, text=battery_capacity_days_value,
                           font=("Open Sans", 12)).grid(row=0, column=0, pady=15, padx=1)

    # Update time frames
    variable_update_time_frame = customtkinter.CTkFrame(app, width=400, height=100, fg_color="black",
                                                        border_width=0)
    variable_update_time_frame.grid(row=1, column=2, padx=1, pady=1, sticky="ESNW")
    app.grid_columnconfigure(2, weight=2)
    customtkinter.CTkLabel(variable_update_time_frame, text="Sensor last update time",
                           font=("Open Sans", 12)).grid(row=0, column=0, pady=15, padx=1)

    temperature_update_time_frame = customtkinter.CTkFrame(app, width=400, height=100, fg_color="gray",
                                                           border_width=0)
    temperature_update_time_frame.grid(row=2, column=2, padx=1, pady=1, sticky="ESNW")
    customtkinter.CTkLabel(temperature_update_time_frame, text=temperature_update_time,
                           font=("Open Sans", 12)).grid(row=0, column=0, pady=15, padx=1)

    humidity_update_time_frame = customtkinter.CTkFrame(app, width=400, height=100, fg_color="gray",
                                                        border_width=0)
    humidity_update_time_frame.grid(row=3, column=2, padx=1, pady=1, sticky="ESNW")
    customtkinter.CTkLabel(humidity_update_time_frame, text=humidity_update_time,
                           font=("Open Sans", 12)).grid(row=0, column=0, pady=15, padx=1)

    pressure_update_time_frame = customtkinter.CTkFrame(app, width=400, height=100, fg_color="gray",
                                                        border_width=0)
    pressure_update_time_frame.grid(row=4, column=2, padx=1, pady=1, sticky="ESNW")
    customtkinter.CTkLabel(pressure_update_time_frame, text=pressure_update_time,
                           font=("Open Sans", 12)).grid(row=0, column=0, pady=15, padx=1)

    illuminance_update_time_frame = customtkinter.CTkFrame(app, width=400, height=100, fg_color="gray",
                                                           border_width=0)
    illuminance_update_time_frame.grid(row=5, column=2, padx=1, pady=1, sticky="ESNW")
    customtkinter.CTkLabel(illuminance_update_time_frame, text=illuminance_update_time,
                           font=("Open Sans", 12)).grid(row=0, column=0, pady=15, padx=1)

    one_wire_temperature_update_time_frame = customtkinter.CTkFrame(app, width=400, height=100, fg_color="gray",
                                                                    border_width=0)
    one_wire_temperature_update_time_frame.grid(row=6, column=2, padx=1, pady=1, sticky="ESNW")
    customtkinter.CTkLabel(one_wire_temperature_update_time_frame, text=onewire_temperature_update_time,
                           font=("Open Sans", 12)).grid(row=0, column=0, pady=15, padx=1)

    thermistor_temperature_update_time_frame = customtkinter.CTkFrame(app, width=400, height=100, fg_color="gray",
                                                                      border_width=0)
    thermistor_temperature_update_time_frame.grid(row=7, column=2, padx=1, pady=1, sticky="ESNW")
    customtkinter.CTkLabel(thermistor_temperature_update_time_frame, text=thermistor_temperature_update_time,
                           font=("Open Sans", 12)).grid(row=0, column=0, pady=15, padx=1)

    battery_capacity_percentage_update_time_frame = customtkinter.CTkFrame(app, width=400, height=100, fg_color="gray",
                                                                           border_width=0)
    battery_capacity_percentage_update_time_frame.grid(row=8, column=2, padx=1, pady=1, sticky="ESNW")
    customtkinter.CTkLabel(battery_capacity_percentage_update_time_frame, text=battery_capacity_percentage_update_time,
                           font=("Open Sans", 12)).grid(row=0, column=0, pady=15, padx=1)

    battery_capacity_days_update_time_frame = customtkinter.CTkFrame(app, width=400, height=100, fg_color="gray",
                                                                     border_width=0)
    battery_capacity_days_update_time_frame.grid(row=9, column=2, padx=1, pady=1, sticky="ESNW")
    customtkinter.CTkLabel(battery_capacity_days_update_time_frame, text=battery_capacity_days_update_time,
                           font=("Open Sans", 12)).grid(row=0, column=0, pady=15, padx=1)

    # Refresh button
    customtkinter.CTkButton(app, text="Refresh", command=refresh).grid(row=10, column=0, columnspan=3, pady=20, padx=100)

    # footer
    customtkinter.CTkLabel(app,
                           text="A freestyle project by \n Adedolapo Adegboye (adedolapo.adegboye@alumni.ucalgary.ca)",
                           font=("Open Sans", 10)).grid(row=11, column=0, columnspan=3, pady=20, padx=100)


def home_page():
    hide_frames()
    # Define frame for homepage
    global home_frame
    home_frame = customtkinter.CTkFrame(app, width=400, height=500, fg_color="transparent",
                                        border_width=0)
    home_frame.grid(row=0, column=0, padx=20, pady=20, sticky="")
    customtkinter.CTkLabel(home_frame, text="Welcome to the Smart Agricultural Sensor \n Live Dashboard",
                           font=("Open Sans", 20)).pack()
    customtkinter.CTkLabel(home_frame, text="By Adedolapo Adegboye", font=("Open Sans", 10)).pack(padx=10, pady=10)
    customtkinter.CTkButton(home_frame, text="Click here to view live dashboard", command=connect).pack(padx=10,
                                                                                                        pady=10)


# Define Menu bar
menu = Menu(app)
app.config(menu=menu)

# Create menu bar
file_menu = Menu(menu)
sensor_menu = Menu(menu)

# Add options for "File" menu option
menu.add_cascade(label="File", menu=file_menu)
# file_menu.add_command(label="Home", command=home_page)
# file_menu.add_separator()
file_menu.add_command(label="Exit", command=app.quit)

# Add options for "Sensor" menu option
menu.add_cascade(label="Sensor", menu=sensor_menu)
sensor_menu.add_command(label="Refresh", command=refresh)

# Instantiate all required frames for hide_frames() to work
home_frame = customtkinter.CTkFrame(app, width=400, height=100, fg_color="green", border_width=0)
dashboard_header_frame = customtkinter.CTkFrame(app, width=400, height=100, fg_color="green", border_width=0)
temperature_value_frame = customtkinter.CTkFrame(app, width=400, height=100, fg_color="green", border_width=0)
humidity_value_frame = customtkinter.CTkFrame(app, width=400, height=100, fg_color="green", border_width=0)
pressure_value_frame = customtkinter.CTkFrame(app, width=400, height=100, fg_color="green", border_width=0)
illuminance_value_frame = customtkinter.CTkFrame(app, width=400, height=100, fg_color="green", border_width=0)
onewire_temperature_value_frame = customtkinter.CTkFrame(app, width=400, height=100, fg_color="green", border_width=0)
thermistor_temperature_value_frame = customtkinter.CTkFrame(app, width=400, height=100, fg_color="green",
                                                            border_width=0)
battery_capacity_percentage_value_frame = customtkinter.CTkFrame(app, width=400, height=100, fg_color="green",
                                                                 border_width=0)
battery_capacity_days_value_frame = customtkinter.CTkFrame(app, width=400, height=100, fg_color="green", border_width=0)
temperature_update_time_frame = customtkinter.CTkFrame(app, width=400, height=100, fg_color="green", border_width=0)
humidity_update_time_frame = customtkinter.CTkFrame(app, width=400, height=100, fg_color="green", border_width=0)
pressure_update_time_frame = customtkinter.CTkFrame(app, width=400, height=100, fg_color="green", border_width=0)
illuminance_update_time_frame = customtkinter.CTkFrame(app, width=400, height=100, fg_color="green", border_width=0)
onewire_temperature_update_time_frame = customtkinter.CTkFrame(app, width=400, height=100, fg_color="green",
                                                               border_width=0)
thermistor_temperature_update_time_frame = customtkinter.CTkFrame(app, width=400, height=100, fg_color="green",
                                                                  border_width=0)
battery_capacity_percentage_update_time_frame = customtkinter.CTkFrame(app, width=400, height=100, fg_color="green",
                                                                       border_width=0)
battery_capacity_days_update_time_frame = customtkinter.CTkFrame(app, width=400, height=100, fg_color="green",
                                                                 border_width=0)


# Clear old frames when page is refreshed or new frame is loaded
def hide_frames():
    for widget in home_frame.winfo_children():
        widget.destroy()
    home_frame.grid_forget()
    for widget in dashboard_header_frame.winfo_children():
        widget.destroy()
    dashboard_header_frame.grid_forget()
    for widget in temperature_value_frame.winfo_children():
        widget.destroy()
    temperature_value_frame.grid_forget()
    for widget in humidity_value_frame.winfo_children():
        widget.destroy()
    humidity_value_frame.grid_forget()
    for widget in pressure_value_frame.winfo_children():
        widget.destroy()
    pressure_value_frame.grid_forget()
    for widget in illuminance_value_frame.winfo_children():
        widget.destroy()
    illuminance_value_frame.grid_forget()
    for widget in onewire_temperature_value_frame.winfo_children():
        widget.destroy()
    onewire_temperature_value_frame.grid_forget()
    for widget in thermistor_temperature_value_frame.winfo_children():
        widget.destroy()
    thermistor_temperature_value_frame.grid_forget()
    for widget in battery_capacity_percentage_value_frame.winfo_children():
        widget.destroy()
    battery_capacity_percentage_value_frame.grid_forget()
    for widget in battery_capacity_days_value_frame.winfo_children():
        widget.destroy()
    battery_capacity_days_value_frame.grid_forget()
    for widget in temperature_update_time_frame.winfo_children():
        widget.destroy()
    temperature_update_time_frame.grid_forget()
    for widget in humidity_update_time_frame.winfo_children():
        widget.destroy()
    humidity_update_time_frame.grid_forget()
    for widget in pressure_update_time_frame.winfo_children():
        widget.destroy()
    pressure_update_time_frame.grid_forget()
    for widget in illuminance_update_time_frame.winfo_children():
        widget.destroy()
    illuminance_update_time_frame.grid_forget()
    for widget in onewire_temperature_update_time_frame.winfo_children():
        widget.destroy()
    onewire_temperature_update_time_frame.grid_forget()
    for widget in thermistor_temperature_update_time_frame.winfo_children():
        widget.destroy()
    thermistor_temperature_update_time_frame.grid_forget()
    for widget in battery_capacity_percentage_update_time_frame.winfo_children():
        widget.destroy()
    battery_capacity_percentage_update_time_frame.grid_forget()
    for widget in battery_capacity_days_update_time_frame.winfo_children():
        widget.destroy()
    battery_capacity_days_update_time_frame.grid_forget()


# Initiate home page
connect()

# Initiate app loop
app.mainloop()
