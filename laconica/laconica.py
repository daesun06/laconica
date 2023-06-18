import pynecone as pc
import requests

API_KEY = ""


class AppState(pc.State):
    text: str = "Type something..."
    input_text: str

    def search_weather(self):
        response = requests.get(
            f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={self.input_text}&days=1&aqi=no&alerts=no"
        )

        self.text = f"{response.json()['current']}"

        # Task 2
        # Format into a nicely styled box component that displays
        # Country name, city name, weather in celcius AND it should be placed
        # inside a box component similar to https://i.imgur.com/dtKFDY1.png


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
