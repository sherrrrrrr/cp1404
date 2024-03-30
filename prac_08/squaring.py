from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_file('squaring.kv')


class MainBoxLayout(BoxLayout):
    def calculate_square(self):
        try:
            input_value = float(self.ids.input_number.text)
            squared_value = input_value ** 2
            self.ids.output_label.text = str(squared_value)
        except ValueError:
            self.ids.output_label.text = 'Invalid input'


class SquareNumberApp(App):
    def build(self):
        self.title = 'Square Number 2'
        return MainBoxLayout()


if __name__ == '__main__':
    SquareNumberApp().run()
