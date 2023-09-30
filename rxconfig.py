import reflex as rx


class LaconicaConfig(rx.Config):
    pass


config = LaconicaConfig(
    app_name="laconica",
    backend_port=5009,
    api_url="http://localhost:5009",
    db_url="sqlite:///reflex.db",
    env=rx.Env.DEV,
)
