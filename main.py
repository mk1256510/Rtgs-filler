from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

class AppUI(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        
        self.input = TextInput(hint_text="Enter Name")
        layout.add_widget(self.input)

        btn = Button(text="Generate")
        btn.bind(on_press=self.click)
        layout.add_widget(btn)

        self.label = Label(text="")
        layout.add_widget(self.label)

        return layout

    def click(self, instance):
        self.label.text = "App Working!"

AppUI().run()
