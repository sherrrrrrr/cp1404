from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout


class Converter(BoxLayout):
    def convert(self):
        try:
            # 获取输入的英里数
            miles = float(self.ids.input_miles.text)
            # 将英里转换为公里
            km = miles * 1.60934
            # 显示转换后的公里数
            self.ids.result_label.text = f'{km:.2f} km'
        except ValueError:
            self.ids.result_label.text = "Invalid input"

    def increment(self, increment_value):
        try:
            # 获取当前输入的英里数
            current_miles = float(self.ids.input_miles.text)
            # 增加或减少英里数
            new_miles = current_miles + increment_value
            # 更新输入框中的值
            self.ids.input_miles.text = str(new_miles)
        except ValueError:
            pass


class ConvertMilesKmApp(App):
    def build(self):
        Builder.load_file('convert_miles_km.kv')
        return Converter()


if __name__ == '__main__':
    ConvertMilesKmApp().run()