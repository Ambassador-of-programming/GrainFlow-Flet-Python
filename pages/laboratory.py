import flet as ft

async def lab(page: ft.Page):

    result = ft.ResponsiveRow(controls=[
        ft.ResponsiveRow(controls=[
            ft.IconButton(
                icon=ft.icons.ARROW_BACK,
                col=1,
                alignment=ft.alignment.center,
                on_click=None,
            ),

            ft.Text(
                col=3,
                value='Склад 1. Лаборатория',
                    color='#000000',
                    size=22,
                    width=206,
                    height=39,
                    
            ),
        ], alignment=ft.MainAxisAlignment.CENTER),

        ft.ResponsiveRow(controls=[
            ft.GridView(
        expand=1,
        runs_count=5,
        max_extent=150,
        child_aspect_ratio=1.0,
        spacing=5,
        run_spacing=5,
        controls=[
            ft.Image(
                src=f"https://picsum.photos/150/150?{0}",
                fit=ft.ImageFit.NONE,
                repeat=ft.ImageRepeat.NO_REPEAT,
                border_radius=ft.border_radius.all(10),
               ),
            ft.Image(
                src=f"https://picsum.photos/150/150?{0}",
                fit=ft.ImageFit.NONE,
                repeat=ft.ImageRepeat.NO_REPEAT,
                border_radius=ft.border_radius.all(10),
               ),
        ]
    )
        ])
            
    ], alignment=ft.MainAxisAlignment.CENTER)
    return result