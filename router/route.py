import flet as ft
from pages.login import login
from pages.production import production
from pages.laboratory import lab

class Router:
    async def init(self, page: ft.Page):
        self.routes = {
            '/login': await login(page),
            '/home': await production(page),
            '/lab': await lab(page),
            # '/home': await login(page),
            # '/home/production': await production(page),
            # '/home/login': await login(page),


        }
        self.body = ft.Container()

    async def route_change(self, route):
        self.body.content = self.routes[route.route]
        self.body.update()