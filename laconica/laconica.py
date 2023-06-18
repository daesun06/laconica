import pynecone as pc

city_name = "Almatyt"


class AppState(pc.State):
    text: str = "Type something..."
    input_text: str
    def search_weather(self):
        self.text = self.input_text

def index():
    return pc.vstack(
        pc.hstack(
            pc.input(on_change=AppState.set_input_text),
            pc.button(
                "Go",
                color_scheme="blue",
                border_radius="1em",
                on_click=AppState.search_weather(),
            ),
        ),
        pc.text(AppState.text),
    )


app = pc.App(state=AppState)
app.add_page(index)
app.compile()
