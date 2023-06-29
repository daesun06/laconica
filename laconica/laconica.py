import pynecone as pc
import requests

API_KEY = ""  # <----- insert your own Weather API key


class AppState(pc.State):
    text: str = "To get forecast info, type your city's name"
    city: str
    country: str
    input_text: str
    icon: str
    show: bool = True

    def search_weather(self):
        try:
            response = requests.get(
                f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={self.input_text}&days=1&aqi=no&alerts=no"
            )

            self.text = f"{response.json()['current']['temp_c']}"
            self.city = f"{response.json()['location']['name']}"
            self.country = f"{response.json()['location']['country']}"
            self.icon = f"{response.json()['current']['condition']['icon']}"
            self.show = not (self.show)
        except Exception:
            ## Add code that will trigger opening a dialog component
            self.text = "Error city not found try something else"

            # Task 2 - Done
            # Format into a nicely styled box component that displays
            # Country name, city name, weather in celcius AND it should be placed
            # inside a box component similar to https://i.imgur.com/dtKFDY1.png

            # Task 3
            # 1. Handle errors gracefully, if city was not found, display a custom dialog component that says `City not found try something else`. Read about try except in python
            # 2. When city is found clear the city from search input
            # 3. When city is not found, clear state set all variables to empty string
            # 4. Style and user new components (see screenshot in telegram for reference)
            # 5. Center align the components in the middle of the screen


def index():
    return pc.vstack(
        pc.hstack(
            pc.input(on_change=AppState.set_input_text),
            pc.button(
                "Search",
                color_scheme="blue",
                border_radius="1em",
                on_click=AppState.search_weather(),
            ),
        ),
        pc.cond(
            AppState.show,
            pc.text("To get forecast info, type your city's name"),
            pc.hstack(
                pc.vstack(
                    pc.text(AppState.city),
                    pc.text(AppState.country),
                    pc.image(
                        src=AppState.icon,
                        width="100px",
                        height="auto",
                    ),
                ),
                pc.text(AppState.text),
            ),
        ),
    )


app = pc.App(state=AppState)
app.add_page(index)
app.compile()
