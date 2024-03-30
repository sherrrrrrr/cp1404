from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    def build(self):
        main_layout = BoxLayout(orientation='vertical')

        names = ["Alice", "Bob", "Carol", "Danny"]

        for name in names:
            label = Label(text=name)
            main_layout.add_widget(label)

        return main_layout


if __name__ == '__main__':
    DynamicLabelsApp().run()