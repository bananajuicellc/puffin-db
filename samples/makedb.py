import sqlalchemy
import models

engine = sqlalchemy.create_engine("sqlite:///pikov.db", future=True)
models.Base.metadata.create_all(engine)
