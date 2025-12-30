import flet as ft

def main(page: ft.Page):
    text_hello = ft.Text(value="HELLO WORLD")

    text_button = ft.TextButton("SEND")
    elevated_button = ft.ElevatedButton("SEND")

    page.add(text_hello, text_button, elevated_button)

ft.app(target=main)
# ft.run(target=main)