# pip install flet[all]
import flet as ft

def main(page: ft.Page):
    page.title = 'My first Flet app'
    page.theme_mode = ft.ThemeMode.LIGHT
    text_hello = ft.Text(value="HELLO WORLD", color =ft.Colors.BLUE)

    text_hello.value = 'Hello'

    def on_button_click(e):
        name = name_input.value.strip()
        print(name)
        if name:
            text_hello.value = f'Hello, {name}!'
            text_hello.color = ft.Colors.GREEN
            name_input.value = None
        else:
            text_hello.value = "Введите корректное имя!"
            text_hello.color = ft.Colors.RED
            name_input.value = None
        page.update()
        # page.update()

    elevated_button = ft.ElevatedButton("SEND", icon=ft.Icons.SEND, on_click=on_button_click)
    name_input = ft.TextField(label='Введите имя', on_submit=on_button_click)

    page.add(text_hello, name_input, elevated_button)


ft.app(target=main)
# ft.run(target=main)