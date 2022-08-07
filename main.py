#For the gui interface
import tkinter
from tkinter import Scale, Tk
from tkinter import *
from tkinter.ttk import *
#for the text to speech functionality
import pyttsx3
#for the speech recognition
import speech_recognition as sr
#for googling,Youtube,wikipedia
from googlesearch import *
import webbrowser
#for weather
import requests

#defining voices
engine=pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def get_audio():
    def speak(audio):
        engine.say(audio)
        engine.runAndWait()
    text1 = "How may I help you?"
    mylabel = Label(root, text=f"VA:{text1}", style='Label')
    mylabel.pack()
    speak(text1)
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception:" + str(e))
    mylabel1 = Label(root, text=f"User:{said}", style='Label')
    mylabel1.pack()
    # time functionality
    if "time" in said:
        from datetime import datetime
        now = datetime.now()
        current_time = now.strftime("%I:%M %p")
        speak(f"the current time is {str(current_time)}")
        label2 = Label(root, text=f"VA: The time is {current_time}" + "\n", style='Label')
        label2.pack()
    #date and tym
    if "day" in said:
        from datetime import date
        today=date.today()
        d=today.strftime("%B %d, %Y")
        import calendar
        curr_date = date.today()
        i = calendar.day_name[curr_date.weekday()]
        speak(f"Today is {d} and {i}")
        label4 = Label(root, text=f"VA: Today is {d} and {i}"+"\n", style='Label')
        label4.pack()
    # seraching google
    if "Google" in said:
        k=said.split()
        l = len(k)
        for q in range(0, l):
            if k[q] == "Google":
                rest = k[(q + 1)::]
                v = ""
                for i in rest:
                    v = v + " " + i
        speak("Here you go \n")
        label5 = Label(root, text=f"VA: Googling {v}" + "\n", style='Label')
        label5.pack()
        chrome_path = r'C:\Program Files\Google\Chrome\Application'
        for url in search(v, tld="co.in", num=1, stop=1, pause=2):
            webbrowser.open("https://google.com/search?q=%s" % v)
    # searching up youtube
    if "YouTube" in said:
        k=said.split()
        l = len(k)
        #say search youtube for
        for q in range(0, l):
            if k[q] == "YouTube":
                rest = k[(q + 2)::]
                v = ""
                for i in rest:
                    v = v + " " + i
        speak("Here you go \n")
        label5 = Label(root, text=f"VA: searching youtube for {v}"+"\n", style='Label')
        label5.pack()
        chrome_path = r'C:\Program Files\Google\Chrome\Application'
        for url in search(v, tld="co.in", num=1, stop=1, pause=2):
            webbrowser.open("https://youtube.com/search?q=%s" % v)
    if "Wikipedia" in said:
        k = said.split()
        l = len(k)
        # say search wikipedia for
        for q in range(0, l):
            if k[q] == "Wikipedia":
                rest = k[(q + 2)::]
                v = ""
                for i in rest:
                    v = v + " " + i
                speak("Here you go \n")
            label5 = Label(root, text=f"VA: searching wikipedia for {v}" + "\n", style='Label')
            label5.pack()
            chrome_path = r'C:\Program Files\Google\Chrome\Application'
            for url in search(v, tld="co.in", num=1, stop=1, pause=2):
                webbrowser.open(f"https://en.wikipedia.org/wiki/{v}")
    #weather
    if "weather" in said:
        k = said.split()
        l = len(k)
        for q in range(0, l):
            if k[q] == "weather":
                city_name = k[q + 2]
        apikey = "b6bac8eb78b81ff6c718c1ce54d0e25d"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        # city_name = input("Enter city name : ")
        complete_url = base_url + "appid=" + apikey + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            speak(
                f"The temperature is {str(current_temperature - 273)} Celsius, The atmospheric pressure is {current_pressure} hectopascals,"
                f" There is {current_humidity} percent humidity and {weather_description} is expected")
            label3 = Label(root, text=f"VA: Temperature (in kelvin unit) = " + str(current_temperature)
                                      + "\n    atmospheric pressure (in hPa unit) = " + str(current_pressure)
                                      + "\n    humidity (in percentage) = " + str(current_humidity)
                                      + "\n    description = " + str(weather_description) + "\n", style='Label')
            label3.pack()
    #all the classes in that day
    #makes use of the json file t2(timetable)
    if "classes" in said:
        from datetime import date
        import calendar
        curr_date = date.today()
        day = calendar.day_name[curr_date.weekday()]
        print(day)

        import json
        f = open('t2.json')
        data = json.load(f)
        for i in data:
            if i['Day '] == day:
                speak(f"First period  {i['1st period']}\n" +
                      f"Second period  {i['2nd period']}\n" +
                      f"Third period  {i['3rd period']}\n" +
                      f"Fourth period  {i['4th period']}\n" +
                      f"Fifth period  {i['5th period']}\n" +
                      f"Sixth period  {i['6th period']}\n" +
                      f"Seventh period  {i['7th period']}\n" +
                      f"Eighth period  {i['8th period']}\n")
                label6 = Label(root, text=f"First period  {i['1st period']}\n" +
                                          f"Second period  {i['2nd period']}\n" +
                                          f"Third period  {i['3rd period']}\n" +
                                          f"Fourth period  {i['4th period']}\n" +
                                          f"Fifth period  {i['5th period']}\n" +
                                          f"Sixth period  {i['6th period']}\n" +
                                          f"Seventh period  {i['7th period']}\n" +
                                          f"Eighth period  {i['8th period']}\n", style='Label')
                label6.pack()
        # Closing file
        f.close()
    #the next period
    if "period" in said:
        from datetime import datetime
        now = datetime.now()
        current_time = int(now.strftime("%H"))
        print(current_time)
        from datetime import date
        import calendar
        curr_date = date.today()
        day = calendar.day_name[curr_date.weekday()]
        print(day)
        import json
        f = open('t2.json')
        data = json.load(f)
        for i in data:
            if i['Day '] == day:
                if current_time == 8:
                    speak(f"next up {i['2nd period']}")
                    label7 = Label(root, text=f"next up  {i['2nd period']}", style='Label')
                    label7.pack()
                if current_time == 9:
                    speak(f"next up {i['3rd period']}")
                    label7 = Label(root, text=f"next up  {i['3rd period']}", style='Label')
                    label7.pack()
                if current_time == 10:
                    speak(f"next up {i['4th period']}")
                    label7 = Label(root, text=f"next up  {i['4th period']}", style='Label')
                    label7.pack()
                if current_time == 11:
                    speak(f"next up lunch")
                    label7 = Label(root, text=f"next up  lunch", style='Label')
                    label7.pack()
                if current_time == 12:
                    speak(f"next up {i['5th period']}")
                    label7 = Label(root, text=f"next up  {i['5th period']}", style='Label')
                    label7.pack()
                if current_time == 13:
                    speak(f"next up {i['6th period']}")
                    label7 = Label(root, text=f"next up  {i['6th period']}", style='Label')
                    label7.pack()
                if current_time == 14:
                    speak(f"next up {i['7th period']}")
                    label7 = Label(root, text=f"next up  {i['7th period']}", style='Label')
                    label7.pack()
                if current_time == 15:
                    speak(f"next up {i['8th period']}")
                    label7 = Label(root, text=f"next up  {i['8th period']}", style='Label')
                    label7.pack()
                if current_time >= 16:
                    speak(f"no classes today")
                    label7 = Label(root, text=f"no classes today", style='Label')
                    label7.pack()
                if current_time <= 8:
                    speak(f"next up {i['1st period']}")
                    label7 = Label(root, text=f"next up  {i['1st period']}", style='Label')
                    label7.pack()
        f.close()

    #recalling from a json file instead of a json file
    if "recall" in said:
        k = said.split()
        l = len(k)
        for q in range(0, l):
            if k[q] == "recall":
                rest = k[(q + 1)::]
                v = ""
                for i in rest:
                    v = v + " " + i
                v=v.strip()
                print(v)
                import json
                f=open('info2.json')
                json_load = json.load(f)
                for i in json_load:
                    if v in i['information']:
                        speak(i['information'])
                        label8 = Label(root, text= i['information'], style='Label')
                        label8.pack()
                

    if "remember" in said:
        import tkinter as tk
        from tkinter import simpledialog

        ROOT = tk.Tk()
        ROOT.wm_attributes("-topmost", 1)

        ROOT.withdraw()
        # the input dialog
        USER_INP = simpledialog.askstring(title="Test",
                                          prompt="What do you wanna remember?:")

        # check it out
        e = {'information': USER_INP}
        import json
        with open('info2.json', 'r+') as file:
            file_data = json.load(file)
            file_data.append(e)
            file.seek(0)
            json.dump(file_data, file, indent=4)
def clear():
    import sys
    import os
    python = sys.executable
    os.execl(python, python, *sys.argv)

# create root window
root= Tk()
root.title("Virtual assistant")
root.iconbitmap('C:/Users/Hi/PycharmProjects/pythonProject')
root.geometry("300x500")
photo=PhotoImage(file=r"C:/Users/Hi/PycharmProjects/pythonProject/mike4.png")
delete=PhotoImage(file=r"C:/Users/Hi/PycharmProjects/pythonProject/realchaata.png")
root.wm_attributes("-topmost",1)


#button style
style = Style()
style.configure('W.TButton', font=('magneto', 30, 'bold'),foreground='red')
#label style
style.configure('Label', font=('Arial',15 ),foreground='blue')
# mike button
button1 = Button(root,text='m',image=photo,style='W.TButton',command=get_audio)
button1.pack()
#clear button
button2 = Button(root,text='clear',image=delete,style='W.TButton',command=clear)
button2.pack()
root.mainloop()

