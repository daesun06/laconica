import pynecone as pc

class LaconicaConfig(pc.Config):
    pass

config = LaconicaConfig(
    app_name="laconica",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)