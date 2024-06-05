import flet as ft

def main(page: ft.Page):
    page.title = "Login Screen"
    page.window_width = 240
    page.window_height = 300
    page.window_resizable = False
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.vertical_alignment = ft.CrossAxisAlignment.CENTER
    
    def login(e):
        username = username_field.value
        password = password_field.value
        if username == "admin" and password == "password":
            message.value = "Login Successful!"
            message.color = "green"
        else:
            message.value = "Invalid username or password"
            message.color = "red"
        page.update()

    username_field = ft.TextField(label="Username", width=200)

    password_field = ft.TextField(label="Password", width=200, password=True, can_reveal_password=True)

    login_button = ft.ElevatedButton(text="Login", on_click=login)

    message = ft.Text("")

    page.add(
        ft.Column(
            [
                username_field,
                password_field,
                login_button,
                message
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

ft.app(target=main)
