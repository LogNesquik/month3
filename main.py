# from datetime import date
# pip install flet[all]
import flet as ft 

def main(page: ft.Page):
    page.title = "Мое первое приложение!"
    page.theme_mode = ft.ThemeMode.LIGHT

    greeting_history = []

    greeting_text = ft.Text('История приветствий:') 

    text_hello = ft.Text(value='Hello world')

    def on_button_click(_):
        name = name_input.value.strip()
        print(name)

        if name:
            text_hello.color = None
            text_hello.value = f"Hello {name}"
            name_input.value = None

            greeting_history.append(name)
            # print(greeting_history)
            greeting_text.value = 'История приветствий: \n' + "\n".join(greeting_history)
        else:
            text_hello.value = 'Введите корректное имя'
            text_hello.color = ft.Colors.RED
            
        # page.update() 

    elevated_button = ft.ElevatedButton('SEND', icon=ft.Icons.SEND, on_click=on_button_click)

    def clear_history(_):
        # print(greeting_history)
        greeting_history.clear()
        # print(greeting_history)
        greeting_text.value = 'История приветствий:'

    def clean_last(_):
        if greeting_history:
            greeting_history.pop()
            greeting_text.value = 'История приветствий: \n' + "\n".join(greeting_history)
        else:
            greeting_text.value = 'История пуста:'

    def sort_alphabet(_):
        greeting_history.sort()
        greeting_text.value = 'История приветствий: \n' + "\n".join(greeting_history)

    clean_last_button = ft.IconButton(icon=ft.Icons.CLEANING_SERVICES, on_click=clean_last)

    sort_alphabet_button = ft.IconButton(icon=ft.Icons.SORT_BY_ALPHA, on_click=sort_alphabet)
    clear_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=clear_history)

    name_input = ft.TextField(label='Введите имя', on_submit=on_button_click, expand=True)

    main_object = ft.Row([name_input, elevated_button, clear_button, clean_last_button, sort_alphabet_button])

    text_row = ft.Row([text_hello], alignment=ft.MainAxisAlignment.CENTER)

    page.add(text_row, main_object, greeting_text)


ft.app(target=main)