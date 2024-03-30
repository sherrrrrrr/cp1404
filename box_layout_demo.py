from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder


class Converter(BoxLayout):
    def handle_greet(self):
        name = self.ids.input_miles.text
        self.ids.result_label.text = f"Hello {name}" if name else "Hello stranger"

    def handle_clear(self):
        self.ids.input_miles.text = ""
        self.ids.result_label.text = "Hello Guido"


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return Converter()

    def clear_input(self):
        input_name = self.root.ids.input_name  # 获取TextInput组件
        input_name.text = ""  # 清空文本

    def greet(self):
        input_name = self.root.ids.input_name  # 获取TextInput组件
        output_label = self.root.ids.output_label  # 获取Label组件
        name = input_name.text
        output_label.text = f"Hello {name}" if name else "Hello stranger"


if __name__ == '__main__':
    BoxLayoutDemo().run()