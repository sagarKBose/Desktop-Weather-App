import requests
import tkinter as tk
from tkinter import font
from PIL import Image,ImageTk

root=tk.Tk() 

WIDTH=620
HEIGHT=450

#79de5817a4d223b536ce61a0f630a4b4
#api.openweathermap.org/data/2.5/weather?q={city name}&appid={your api key}

def get_weather(city):
    weather_key="79de5817a4d223b536ce61a0f630a4b4"
    url='https://api.openweathermap.org/data/2.5/weather'
    params={'appid':weather_key, 'q':city, 'units':'Metric'}
    response=requests.get(url,params=params)
    report=response.json()
    
    label['text']=show_weather_report(report)

    """ icon_name=report['weather'][0]['icon']
    open_img(icon_name)
 """

""" def open_img(icon):
     size= int(low_frame.winfo_height()*0.25)
    img= ImageTk.PhotoImage(Image.open('E:\Python programs\PYTHON_with_ardit\project_weatherAPP\for_weather_icons\').resize((size, size)))
    weather_icon.delete(all)
    weather_icon.create_im age(0,0,anchor='s',image=img)
    weather_icon.image=img  """


def show_weather_report(report):
    try:
        city_name= report['name']
        weather_condition= report['weather'][0]['description']
        temp= report['main']['temp']
        output= 'City: %s \nCondition: %s \nTemperature(°C): %s' %(city_name,weather_condition,temp)
    except:
        output='There was a problem while retrieving that information'
    return output


canvas=tk.Canvas(root,width=WIDTH,height=HEIGHT)
canvas.pack()

landscape_img=tk.PhotoImage(file=r'C:\Users\KIIT\PYTHON\project_weatherAPP\landpng.png')
landscape_label=tk.Label(root,image=landscape_img)
landscape_label.place(relheight=1,relwidth=1)

frame=tk.Frame(root,bg='#0B90A9',bd=5)
frame.place(relx=0.5,rely=0.1,relheight=0.1,relwidth=0.75,anchor='n')

entry=tk.Entry(frame,font=('Courier New Baltic',20))
entry.place(relheight=1,relwidth=0.7)

btn=tk.Button(frame,text="Get Weather",relief='raised',bg="gray",font=20,command=lambda: get_weather(entry.get()))
btn.place(relx=0.72,relheight=1,relwidth=0.28)

low_frame=tk.Frame(root,bg='#0B90A9',bd=5)
low_frame.place(relx=0.5,rely=0.25,relheight=0.65,relwidth=0.75,anchor='n')

bg_color='white'
label=tk.Label(low_frame,font=('Calibri',20),justify='center',bd=4)
label.config(font=40,bg=bg_color)
label.place(relheight=1,relwidth=1)

""" weather_icon=tk.Canvas(label,bg=bg_color,bd=0,highlightthickness=0)
weather_icon.place(relx=0.75,rely=0,relwidth=1,relheight=0.5) """




root.mainloop()