from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout

# Установка размера окна для ПК
Window.size = (360, 640)

# Класс для закладок
class Tab(MDFloatLayout, MDTabsBase):
    pass

KV = '''
MDNavigationLayout:
    ScreenManager:
        Screen:
            BoxLayout:
                orientation: 'vertical'

                # Верхняя панель
                MDToolbar:
                    title: "Mortgage Calculator"
                    elevation: 10
                    left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

                # Закладки
                MDTabs:
                    id: tabs
                    background_color: app.theme_cls.primary_color
                    indicator_color: 1, 1, 0, 1 # Желтый индикатор

                # Основной контент
                MDLabel:
                    text: "Контент страницы"
                    halign: "center"

    # Боковое меню
    MDNavigationDrawer:
        id: nav_drawer
        
        BoxLayout:
            orientation: "vertical"
            padding: "16dp"
            spacing: "8dp"

            # Хедер (Заголовок меню)
            MDLabel:
                text: "KIVYMD LIBRARY"
                font_style: "H6"
                size_hint_y: None
                height: self.texture_size[1]
                
            MDLabel:
                text: "kivydevelopment@gmail.com"
                font_style: "Caption"
                theme_text_color: "Secondary"
                size_hint_y: None
                height: self.texture_size[1]

            MDSeparator:

            # Список иконок
            ScrollView:
                MDList:
                    OneLineIconListItem:
                        text: "My files"
                        IconLeftWidget:
                            icon: "folder"
                    
                    OneLineIconListItem:
                        text: "Shared with me"
                        IconLeftWidget:
                            icon: "account-multiple"
                            
                    OneLineIconListItem:
                        text: "Starred"
                        IconLeftWidget:
                            icon: "star"
            
            # Распорка, чтобы прижать список к верху
            Widget:
'''

class MainApp(MDApp):
    def build(self):
        # Настройка темы
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"
        return Builder.load_string(KV)

    def on_start(self):
        # Список данных для закладок (иконка, текст)
        tabs_data = [
            ("folder", "My files"),
            ("account-multiple", "Shared with me"),
            ("star", "Starred"),
            ("history", "Recent"),
            ("check-bold", "Shared with me"),
            ("upload", "Upload"),
        ]
        
        # Добавляем виджеты закладок
        for icon_name, tab_text in tabs_data:
            self.root.ids.tabs.add_widget(
                Tab(text=tab_text, icon=icon_name)
            )

if __name__ == "__main__":
    MainApp().run()