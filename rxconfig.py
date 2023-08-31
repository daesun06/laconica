import reflex as rx


class LaconicaConfig(rx.Config):
    pass


config = LaconicaConfig(
    app_name="laconica",
    db_url="sqlite:///reflex.db",
    env=rx.Env.DEV,
)
