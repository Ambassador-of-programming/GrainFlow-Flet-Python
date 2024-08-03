from database.db_manager import Auth
import flet as ft 
import asyncio

# Авторизация
async def login(page: ft.Page):
    class LoginUser:
        def __init__(self) -> None:
            self.login = ft.TextField(
                            label='Логин',
                            width=300,
                            height=56,
                            bgcolor='#FFFFFF',
                            color='#939EB4',
                            prefix_icon=ft.icons.ACCOUNT_BOX,
                            border_color='#F6F6F6'           
                        )
            self.password = ft.TextField(
                                label='Пароль',
                                width=300,
                                height=56,
                                bgcolor='#FFFFFF',
                                color='#939EB4',
                                prefix_icon=ft.icons.LOCK_OUTLINED,
                                border_color='#F6F6F6',
                                can_reveal_password=True,
                                password=True,
                        )
            self.error_text = ft.Text(visible=False, color=ft.colors.RED)
            self.login_button = ft.ElevatedButton( 
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=10)), 
                            bgcolor='#1C3E7D',
                            color=ft.colors.WHITE,
                            width=300,
                            height=52,
                            content=ft.Text(
                                value="Вход", 
                                size=20,
                                font_family='Cutive Mono'),
                            on_click = self.check_user
                        )

        async def check_user(self, event):
            # если пользователь ввел все данные для входа
            if all([self.login.value, self.password.value]):
                auth = Auth()
                check_user_registration = await auth.check_user(
                    username=self.login.value, password=self.password.value)
                if check_user_registration == True:
                    page.go('/home')
                else:
                    self.error_text.visible = True
                    self.error_text.value = 'Неверный логин или пароль'
                    self.error_text.update()

                    await asyncio.sleep(3)

                    self.error_text.visible = False
                    self.error_text.update()
            else:
                self.error_text.visible = True
                self.error_text.value = 'Заполните все поля'
                self.error_text.update()

                await asyncio.sleep(3)

                self.error_text.visible = False
                self.error_text.update()

    enter = LoginUser()
    content = ft.Stack(
    controls=[
        ft.Row([
            ft.Row(height=150),
            ft.Image(
            src=f"assets/image/main.png",
            width=230,
            height=123,
            fit=ft.ImageFit.COVER,
        ),], 
        alignment=ft.MainAxisAlignment.CENTER
        ),

        ft.Column(
            controls=[
                ft.Row(height=140),
                ft.Row(
                    controls=[
                        ft.Image(
                            src='assets/image/logo.png',
                            width=306,
                            height=165,
                            fit=ft.ImageFit.COVER,

                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
   
                ft.Row(height=5),          

                # заполнение номера телефона
                ft.Row(
                    controls=[
                        enter.login
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),

                # заполнение пароля
                ft.Row(
                    controls=[
                        enter.password
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                
                ft.Row(height=5),

                # ошибка текст
                ft.Row(controls=[
                    enter.error_text
                ],
                alignment=ft.MainAxisAlignment.CENTER),

                # кнопка входа
                ft.Row(
                    controls=[
                        enter.login_button
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
        ),
    ],
)
    return content
