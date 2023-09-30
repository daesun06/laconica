import reflex as rx
import requests

API_KEY = "c8479639257c4e53ab805054232305"  # <----- insert your own Weather API key


class AppState(rx.State):
    text: str = ""
    city: str
    country: str
    temp: str
    show: bool = True

    def search_weather(self):
        try:
            response = requests.get(
                f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={self.text}&days=1&aqi=no&alerts=no"
            )

            self.temp = f"{response.json()['current']['temp_c']}"
            self.city = f"{response.json()['location']['name']}"
            self.country = f"{response.json()['location']['country']}"
            self.show = not (self.show)
        except Exception:
            ## Add code that will trigger opening a dialog component
            self.city = None
            self.country = None
            self.temp = "Error city not found try something else"
            # Task 3
            # 1. Handle errors gracefully, if city was not found, display a custom dialog component that says `City not found try something else`. Read about try except in python
            # 2. When city is found clear the city from search input
            # 3. When city is not found, clear state set all variables to empty string
            # 4. Style and user new components (see screenshot in telegram for reference)
            # 5. Center align the components in the middle of the screen

    def clear_input_text(self):
        self.text = ""


def index():
    return rx.vstack(
        rx.hstack(
            rx.text("ㅤㅤ"),
            rx.badge(
                "Weather Forecast by Daesun",
                variant="subtle",
                color_scheme="blue",
                bg="black",
                color="white",
            ),
            rx.text("ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ"),  # TODO: Use alignment
            rx.link(
                "GitHub",
                href="https://github.com/daesun06/laconica",
                color="rgb(107,99,246)",
            ),
            rx.text("ㅤㅤㅤ"),
            bg="black",
            color="white",
            height="5vh",
        ),
        rx.box("", height="40vh", bg=""),
        rx.cond(
            AppState.show,
            rx.text("To get forecast info, type your city's name"),
            rx.hstack(
                rx.box(
                    rx.vstack(
                        rx.heading(AppState.city, size="xl", color="orange"),
                        rx.heading(AppState.country, size="2xl", color="white"),
                        rx.heading(AppState.temp, size="3xl", color="orange"),
                        rx.icon(
                            tag="sun",
                            size="xl",
                        ),
                        bg="black",
                        border_radius="lg",
                        width="100%",
                    ),
                ),
            ),
        ),
        rx.hstack(
            rx.input(on_change=AppState.set_text, value=AppState.text),
            rx.button(
                "Search",
                color_scheme="blue",
                on_click=AppState.search_weather,
            ),
            rx.button(
                "Clear",
                color_scheme="blue",
                on_click=AppState.clear_input_text,
            ),
        ),
        rx.box("", height="44.5vh", bg="#1D2330"),
        center_content=True,
        bg="#1D2330",
        color="white",
    )


app = rx.App(state=AppState)
app.add_page(index)
app.compile()
