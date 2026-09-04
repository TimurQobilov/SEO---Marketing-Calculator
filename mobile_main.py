import webbrowser
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView

class SEOMobileCalc(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=10, spacing=10, **kwargs)

        self.add_widget(Label(text="[b]SEO Калькулятор[/b]", markup=True, font_size='22sp', size_hint_y=None, height=40))

        # Ввод данных
        self.cost = TextInput(hint_text="Расходы (руб)", input_filter='float', multiline=False)
        self.clicks = TextInput(hint_text="Клики", input_filter='float', multiline=False)
        self.impressions = TextInput(hint_text="Показы", input_filter='float', multiline=False)
        self.revenue = TextInput(hint_text="Выручка / Доход (руб)", input_filter='float', multiline=False)

        self.add_widget(self.cost)
        self.add_widget(self.clicks)
        self.add_widget(self.impressions)
        self.add_widget(self.revenue)

        # Кнопка расчета
        btn = Button(text="Рассчитать", size_hint_y=None, height=50, background_color=(0.2, 0.6, 1, 1))
        btn.bind(on_press=self.calculate)
        self.add_widget(btn)

        # Вывод результатов
        self.result_label = Label(text="Заполните поля и нажмите Рассчитать", font_size='14sp')
        self.add_widget(self.result_label)

        # Разработчик и ТГ
        dev_btn = Button(text="Разработчик: @timurqobilov", size_hint_y=None, height=40, background_color=(0, 0, 0, 0))
        dev_btn.bind(on_press=lambda x: webbrowser.open("https://t.me/timurqobilov"))
        self.add_widget(dev_btn)

    def calculate(self, instance):
        try:
            c = float(self.cost.text or 0)
            cl = float(self.clicks.text or 0)
            imp = float(self.impressions.text or 0)
            rev = float(self.revenue.text or 0)

            ctr = (cl / imp * 100) if imp > 0 else 0
            cpc = (c / cl) if cl > 0 else 0
            cpm = (c / imp * 1000) if imp > 0 else 0
            roi = ((rev - c) / c * 100) if c > 0 else 0

            res = f"CTR: {ctr:.2f}%\nCPC: {cpc:.2f} руб.\nCPM: {cpm:.2f} руб.\nROI: {roi:.2f}%"
            self.result_label.text = res
        except Exception:
            self.result_label.text = "Ошибка ввода данных"

class MainApp(App):
    def build(self):
        return SEOMobileCalc()

if __name__ == '__main__':
    MainApp().run()