import flet as ft
from screen.user_control.app_bar import NavBar
from screen.router_manager import Router


__version__ = '0.7b'


def __main__(page: ft.Page) -> ft.FletApp:
    page.title = f'MangaYouKnow {__version__}'
    page.theme_mode = 'dark'
    page.window_min_width = 770
    page.window_min_height = 600
    page.vertical_alignment = ft.CrossAxisAlignment.CENTER
    router = Router(page)
    page.on_route_change = router.route_change
    page.add(
        ft.ResponsiveRow([
            ft.Column([
                NavBar(page)
            ],
            col=1),
            ft.Column([
                router.body
            ],
            col=11)
        ])
    )
    page.go('/')
    def resize(e:ft.ControlEvent):
        page.update()
    page.on_resize = resize
    page.update()


if __name__ == '__main__':
    ft.app(target=__main__)
    