from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty, ColorProperty
import datetime
import calendar
import random
from kivy.graphics import Color, Rectangle, Line, Ellipse

def add_months(sourcedate, months):
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month // 12
    month = month % 12 + 1
    day = min(sourcedate.day, calendar.monthrange(year, month)[1])
    return datetime.date(year, month, day)

class Tab(MDFloatLayout, MDTabsBase):
    pass

class ItemTable(MDBoxLayout):
    num = StringProperty()
    date = StringProperty()
    payment = StringProperty()
    interest = StringProperty()
    principal = StringProperty()
    debt = StringProperty()
    bg_color = ColorProperty([1, 1, 1, 1])

KV = '''
<ItemTable>:
    size_hint_y: None
    height: "40dp"
    padding: "5dp"
    spacing: "2dp"
    md_bg_color: self.bg_color

    MDLabel:
        text: root.num
        size_hint_x: 0.1
        halign: "center"
        font_style: "Caption"
    MDLabel:
        text: root.date
        size_hint_x: 0.25
        halign: "center"
        font_style: "Caption"
    MDLabel:
        text: root.payment
        size_hint_x: 0.2
        halign: "center"
        font_style: "Caption"
    MDLabel:
        text: root.interest
        size_hint_x: 0.15
        halign: "center"
        font_style: "Caption"
    MDLabel:
        text: root.principal
        size_hint_x: 0.15
        halign: "center"
        font_style: "Caption"
    MDLabel:
        text: root.debt
        size_hint_x: 0.15
        halign: "center"
        font_style: "Caption"

MDNavigationLayout:
    MDScreenManager:
        MDScreen:
            MDBoxLayout:
                orientation: 'vertical'
                MDTopAppBar:
                    title: app.title
                    elevation: 4
                    md_bg_color: 0, 0, 0, 1
                    specific_text_color: 1, 1, 1, 1
                    left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                    right_action_items: [["star-outline", lambda x: None]]
                
                MDTabs:
                    id: tabs
                    background_color: 0.1, 0.1, 0.1, 1
                    text_color_active: 1, 1, 1, 1
                    text_color_normal: 0.6, 0.6, 0.6, 1
                    indicator_color: 1, 0.8, 0, 1
                    
                    Tab:
                        id: input_tab
                        title: "Input"
                        icon: "calculator"
                        MDBoxLayout:
                            orientation: 'vertical'
                            padding: "20dp"
                            spacing: "15dp"
                            adaptive_height: True
                            pos_hint: {"top": 1}

                            MDTextField:
                                id: start_date
                                hint_text: "Start date"
                                icon_left: "calendar"
                                on_focus: if self.focus: app.show_date_picker(self.focus)

                            MDTextField:
                                id: loan_amount
                                hint_text: "Loan"
                                icon_left: "cash"
                                input_filter: "float"
                                text: "5000000"

                            MDTextField:
                                id: loan_term
                                hint_text: "Months"
                                icon_left: "clock-outline"
                                input_filter: "int"
                                text: "120"

                            MDBoxLayout:
                                orientation: 'horizontal'
                                spacing: "20dp"
                                adaptive_height: True

                                MDTextField:
                                    id: interest_rate
                                    hint_text: "Interest, %"
                                    icon_left: "bank"
                                    input_filter: "float"
                                    text: "9.5"

                                MDTextField:
                                    id: drop_item
                                    hint_text: "Payment type"
                                    text: "annuity"
                                    readonly: True
                                    on_focus: if self.focus: app.menu.open()

                            MDBoxLayout:
                                orientation: 'horizontal'
                                spacing: "20dp"
                                padding: [0, "30dp", 0, 0]
                                adaptive_height: True

                                MDRectangleFlatIconButton:
                                    icon: "android"
                                    text: ""
                                    theme_text_color: "Custom"
                                    text_color: 1, 0, 0, 1
                                    icon_color: 1, 0, 0, 1
                                    line_color: 0.5, 0.5, 0.5, 1
                                    size_hint_x: 0.3

                                Widget:
                                    size_hint_x: 0.2

                                MDRaisedButton:
                                    text: "Test Ok"
                                    md_bg_color: 0, 0, 0, 1
                                    text_color: 1, 1, 1, 1
                                    size_hint_x: 0.5
                                    on_release: app.calculate_mortgage()

                    Tab:
                        id: table_tab
                        title: "Table"
                        icon: "grid"
                        MDBoxLayout:
                            orientation: "vertical"
                            ScrollView:
                                MDList:
                                    id: table_list

                    Tab:
                        title: "Graph"
                        icon: "chart-line"
                        MDBoxLayout:
                            orientation: "vertical"
                            MDBoxLayout:
                                size_hint_y: None
                                height: "40dp"
                                md_bg_color: 0.3, 0.3, 0.3, 1
                                MDLabel:
                                    text: "Payment Graph"
                                    halign: "center"
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1
                            MDBoxLayout:
                                orientation: "horizontal"
                                size_hint_y: None
                                height: "40dp"
                                padding: "10dp"
                                MDCheckbox:
                                    size_hint: None, None
                                    size: "24dp", "24dp"
                                    active: True
                                    disabled: True
                                    color_disabled: 0, 0, 1, 1
                                MDLabel:
                                    text: "Principal"
                                MDCheckbox:
                                    size_hint: None, None
                                    size: "24dp", "24dp"
                                    active: True
                                    disabled: True
                                    color_disabled: 1, 0, 0, 1
                                MDLabel:
                                    text: "Interest"
                            MDBoxLayout:
                                id: box_graph

                    Tab:
                        title: "Chart"
                        icon: "chart-pie"
                        MDBoxLayout:
                            orientation: "vertical"
                            MDBoxLayout:
                                size_hint_y: None
                                height: "40dp"
                                md_bg_color: 0.3, 0.3, 0.3, 1
                                MDLabel:
                                    text: "Total Payments"
                                    halign: "center"
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1
                            MDBoxLayout:
                                orientation: "horizontal"
                                size_hint_y: None
                                height: "40dp"
                                padding: "10dp"
                                MDCheckbox:
                                    size_hint: None, None
                                    size: "24dp", "24dp"
                                    active: True
                                    disabled: True
                                    color_disabled: 0, 0, 1, 1
                                MDLabel:
                                    text: "Principal"
                                MDCheckbox:
                                    size_hint: None, None
                                    size: "24dp", "24dp"
                                    active: True
                                    disabled: True
                                    color_disabled: 1, 0, 0, 1
                                MDLabel:
                                    text: "Interest"
                            MDBoxLayout:
                                id: box_chart

                    Tab:
                        title: "Sum"
                        icon: "book-open-outline"

    MDNavigationDrawer:
        id: nav_drawer
        MDNavigationDrawerMenu:
            MDNavigationDrawerHeader:
                title: "MENU"
            MDNavigationDrawerItem:
                icon: "weather-night"
                text: "Toggle Theme"
                on_release: app.toggle_theme()
'''

class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Amber"
        self.theme_cls.theme_style = "Light"
        self.title = "Mortgage Calculator"
        
        self.menu_items = [
            {"viewclass": "OneLineListItem", "text": "annuity", "on_release": lambda x="annuity": self.set_item(x)},
            {"viewclass": "OneLineListItem", "text": "differentiated", "on_release": lambda x="differentiated": self.set_item(x)},
        ]
        return Builder.load_string(KV)

    def on_start(self):
        self.menu = MDDropdownMenu(caller=self.root.ids.drop_item, items=self.menu_items, width_mult=4)
        self.root.ids.start_date.text = str(datetime.date.today())

    def show_date_picker(self, focus):
        if not focus:
            return
        self.root.ids.start_date.focus = False
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()

    def on_save(self, instance, value, date_range):
        self.root.ids.start_date.text = str(value)

    def on_cancel(self, instance, value):
        pass

    def set_item(self, text_item):
        self.root.ids.drop_item.text = text_item
        self.root.ids.drop_item.focus = False
        self.menu.dismiss()
        
    def draw_graph(self, widget, graph_data, max_pay):
        widget.canvas.clear()
        if not graph_data or max_pay <= 0:
            return
            
        n = len(graph_data)
        bw = max(1, widget.width / n)
        hf = widget.height / max_pay
        
        with widget.canvas:
            for i, data in enumerate(graph_data):
                principal = data['principal']
                interest = data['interest']
                
                # Principal (Blue) at the bottom
                Color(0, 0, 1, 1)
                Rectangle(pos=(widget.x + i * bw, widget.y), size=(max(1, bw * 0.9), principal * hf))
                
                # Interest (Red) on top
                Color(1, 0, 0, 1)
                Rectangle(pos=(widget.x + i * bw, widget.y + principal * hf), size=(max(1, bw * 0.9), interest * hf))

    def draw_chart(self, widget, principal, interest):
        widget.canvas.clear()
        total = principal + interest
        if total == 0:
            return
            
        angle_p = 360 * principal / total
        
        # Center the pie chart
        d = min(widget.width, widget.height) * 0.9
        px = widget.x + (widget.width - d) / 2
        py = widget.y + (widget.height - d) / 2
        
        with widget.canvas:
            Color(0, 0, 1, 1) # Blue
            Ellipse(pos=(px, py), size=(d, d), angle_start=0, angle_end=angle_p)
            
            Color(1, 0, 0, 1) # Red
            Ellipse(pos=(px, py), size=(d, d), angle_start=angle_p, angle_end=360)

    def calculate_mortgage(self):
        try:
            S = float(self.root.ids.loan_amount.text)
            n = int(self.root.ids.loan_term.text)
            r = float(self.root.ids.interest_rate.text) / 100 / 12
            payment_type = self.root.ids.drop_item.text.lower()
            
            try:
                st_date = datetime.datetime.strptime(self.root.ids.start_date.text, "%Y-%m-%d").date()
            except:
                st_date = datetime.date.today()
            
            # Очищаем таблицу
            self.root.ids.table_list.clear_widgets()
            
            # Добавляем заголовок
            header_bg = [0.3, 0.3, 0.3, 1] if self.theme_cls.theme_style == "Dark" else [0.8, 0.8, 0.8, 1]
            self.root.ids.table_list.add_widget(
                ItemTable(
                    num="No", date="Date", payment="Payment", 
                    interest="Interest", principal="Principal", debt="Balance",
                    bg_color=header_bg
                )
            )
            
            balance = S
            total_interest = 0.0
            
            graph_data = []
            max_monthly_pay = 0.0
            
            if payment_type == "annuity" or payment_type == "аннуитетный":
                monthly_payment = S * (r * (1 + r)**n) / ((1 + r)**n - 1)
                max_monthly_pay = monthly_payment
                for i in range(1, n + 1):
                    interest_pay = balance * r
                    principal_pay = monthly_payment - interest_pay
                    balance -= principal_pay
                    total_interest += interest_pay
                    
                    cur_date = add_months(st_date, i)
                    bg = [1, 1, 1, 1] if i % 2 != 0 else [0.95, 0.95, 0.95, 1]
                    if self.theme_cls.theme_style == "Dark":
                        bg = [0.1, 0.1, 0.1, 1] if i % 2 != 0 else [0.15, 0.15, 0.15, 1]

                    self.root.ids.table_list.add_widget(
                        ItemTable(
                            num=str(i),
                            date=cur_date.strftime("%Y-%m-%d"),
                            payment=f"{monthly_payment:.2f}",
                            interest=f"{interest_pay:.2f}",
                            principal=f"{principal_pay:.2f}",
                            debt=f"{max(0, balance):.2f}",
                            bg_color=bg
                        )
                    )
                    graph_data.append({'principal': principal_pay, 'interest': interest_pay})
            else:
                principal_pay = S / n
                for i in range(1, n + 1):
                    interest_pay = balance * r
                    monthly_payment = principal_pay + interest_pay
                    balance -= principal_pay
                    total_interest += interest_pay
                    if monthly_payment > max_monthly_pay:
                        max_monthly_pay = monthly_payment
                    
                    cur_date = add_months(st_date, i)
                    bg = [1, 1, 1, 1] if i % 2 != 0 else [0.95, 0.95, 0.95, 1]
                    if self.theme_cls.theme_style == "Dark":
                        bg = [0.1, 0.1, 0.1, 1] if i % 2 != 0 else [0.15, 0.15, 0.15, 1]

                    self.root.ids.table_list.add_widget(
                        ItemTable(
                            num=str(i),
                            date=cur_date.strftime("%Y-%m-%d"),
                            payment=f"{monthly_payment:.2f}",
                            interest=f"{interest_pay:.2f}",
                            principal=f"{principal_pay:.2f}",
                            debt=f"{max(0, balance):.2f}",
                            bg_color=bg
                        )
                    )
                    graph_data.append({'principal': principal_pay, 'interest': interest_pay})
                    
            # Рисование графики в соседних табах
            self.draw_graph(self.root.ids.box_graph, graph_data, max_monthly_pay)
            self.draw_chart(self.root.ids.box_chart, S, total_interest)
            
            # Switch to Table tab
            tabs_obj = self.root.ids.tabs
            labels = tabs_obj.get_tab_list()
            if len(labels) > 1:
                tabs_obj.switch_tab(labels[1])
                    
        except Exception as e:
            print(f"Error in calculation: {e}")

    def toggle_theme(self):
        self.theme_cls.theme_style = "Dark" if self.theme_cls.theme_style == "Light" else "Light"

if __name__ == '__main__':
    MainApp().run()