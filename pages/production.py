import flet as ft

async def production(page: ft.Page):

    result = ft.ResponsiveRow(controls=[
        ft.Row(controls=[
            ft.Text(value='Производство', 
                size=48,
                weight=353,
                height=58,
                color='#000000'
            ),
        ], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(),

        ft.ResponsiveRow(controls=[
            ft.TextButton(
                col=3,
                content=ft.Text(value='с. Песьянное',
                    color='#000000',
                    size=22,
                    width=206,
                    height=39,
                    )
            ),

            ft.TextButton(
                col=3,
                content=ft.Text(value='с. Камыши',
                    color='#000000',
                    size=22,
                    width=206,
                    height=39,
                    )
            ),

            ft.ElevatedButton(text='История отгрузок', 
                col=3,
                width=206,
                height=39,
                color='#000000',
                bgcolor='#D9D9D9'
            ),
        ], alignment=ft.MainAxisAlignment.CENTER),

        ft.ResponsiveRow(controls=[
            ft.Container(
                content=ft.Text("Non clickable", color='#000000'),
                margin=10,
                padding=10,
                alignment=ft.alignment.center,
                bgcolor='#C0D3FF',
                width=200,
                height=200,
                border_radius=10,
                col=3
            ),
            ft.Container(
                content=ft.Text("Non clickable", color='#000000'),
                margin=10,
                padding=10,
                alignment=ft.alignment.center,
                bgcolor='#FEE2A2',
                width=200,
                height=200,
                border_radius=10,
                col=3
            ),
            ft.Container(
                content=ft.Text("Non clickable", color='#000000'),
                margin=10,
                padding=10,
                alignment=ft.alignment.center,
                bgcolor='#D9D9D9',
                width=200,
                height=200,
                border_radius=10,
                col=3
            ),
            ft.Container(
                content=ft.Text("Non clickable", color='#000000'),
                margin=10,
                padding=10,
                alignment=ft.alignment.center,
                bgcolor='#D9D9D9',
                width=200,
                height=200,
                border_radius=10,
                col=3
            ),
        ]),
        ft.ResponsiveRow(controls=[
            ft.Container(
                content=ft.Text("Non clickable", color='#000000'),
                margin=10,
                padding=10,
                alignment=ft.alignment.center,
                bgcolor='#D9D9D9',
                width=200,
                height=200,
                border_radius=10,
                col=3
            ),
            ft.Container(
                content=ft.Text("Non clickable", color='#000000'),
                margin=10,
                padding=10,
                alignment=ft.alignment.center,
                bgcolor='#D9D9D9',
                width=200,
                height=200,
                border_radius=10,
                col=3
            ),
            ft.Container(
                content=ft.Text("Non clickable", color='#000000'),
                margin=10,
                padding=10,
                alignment=ft.alignment.center,
                bgcolor='#D9D9D9',
                width=200,
                height=200,
                border_radius=10,
                col=3
            ),
            ft.Container(
                content=ft.Text("Non clickable", color='#000000'),
                margin=10,
                padding=10,
                alignment=ft.alignment.center,
                bgcolor='#D9D9D9',
                width=200,
                height=200,
                border_radius=10,
                col=3
            ),
        ])
            
    ], alignment=ft.MainAxisAlignment.CENTER)
    return result