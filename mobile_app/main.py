from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json
import glob
from pathlib import Path
from datetime import datetime
import random
from hoverable import HoverBehavior
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior


Builder.load_file("design.kv")

class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = "sign_up_screen"
    def login(self, uname, pword):
        with open("users.json", "r") as file:
            users = json.load(file)
        if uname in users and users[uname]["password"] == pword:
            self.manager.current = "login_success"
        else:
            self.ids.login_wrong.text = "Wrong username or Password"


class RootWidget(ScreenManager):
    pass

class SignUpScreen(Screen):
    def add_user(self, uname, pword):
        with open("users.json") as file:
            users = json.load(file)
        users[uname] = {"username": uname, "password": pword,
                        "created": datetime.now()}
        with open("users.json", "w") as file:
            json.dump(users, file)
        self.manager.current = "sign_up_success"

class SignUpSuccess(Screen):
    def return_to_login(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"

class LoginSuccess(Screen):
    def log_out(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"
    def get_quote(self, feel):
        feel = feel.lower()
        available_feelings = glob.glob("*txt")
        available_feelings = [Path(filename).stem for filename in available_feelings]
        if feel in available_feelings:
            with open(f"{feel}.txt") as file:
                quote = file.readlines()
            self.ids.quote.text = random.choice(quotes)
        else:
            self.ids.quote.text = "This feeling is not currently allowed."

class ImageButton(ButtonBehavior, HoverBehavior, Image):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()
