#=====================================================================
#Proof of concept work for SkiJumping project.
#Written by Topi Loytainen and Niko Loytainen.
#Inspiration from:
#https://www.section.io/engineering-education/kivy-python-first-app/
#=====================================================================
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import datetime

#print("Hello World!")

class AgeCalculator(App):

    def getAge(self, event):
        today = datetime.date.today().year 
        dob = self.date.text
        age = int(today) - int(dob) 
        self.ageRequest.text = "You are " + str(int(age)) + " years old"


    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.add_widget(Image(source="logo_image.png"))

        self.ageRequest = Label(
            text = "Enter your date of birth...", 
            font_size = 50,
            color = "#ffffff",
            bold = True
        )
        self.window.add_widget(self.ageRequest)

        self.date = TextInput(
            multiline=False,
            padding_y = (30, 30),
            size_hint = (1, 0.7),
            font_size = 30
        )
        self.window.add_widget(self.date)

        self.button = Button(
            text = "Calculate Age",
            size_hint = (0.5, 0.5),
            bold = True,
            font_size = 30
        )
        self.button.bind(on_press = self.getAge)
        self.window.add_widget(self.button)

        return self.window
    
if __name__ == "__main__":
 AgeCalculator().run()
