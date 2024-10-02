import reflex as rx



def index() -> rx.Component:
    return rx.container(
        rx.box(
            "que es reflex",
            text_align="right"
        ),
        rx.box(
            "un aplicativo de python para crear aplicaciones web",
            text_align="left"
        ),
    )










app = rx.App()
app.add_page(index)