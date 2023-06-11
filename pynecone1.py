import pynecone as pc

class State(pc.State):
    '''The app state''' 
city_name = str(input("Enter the name of the city you are in: "))
def reaction():
    pc.box(
        city_name,
        color_scheme="light_blue",
        border_radius="1em",
        )

def index():
    return pc.hstack(
        pc.box(
            city_name,
            color_scheme="light_blue",
            border_radius="1em",            
        ),

        pc.button(
            "Go",
            color_scheme="light_blue",
            border_radius="1em",
            on_click=reaction(),
        ),
    )

app = pc.App(state=State)
app.add_page(index)
app.compile()