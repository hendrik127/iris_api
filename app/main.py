from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.main import api_router

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     """
#     Checks whether the database is populated.
#     Populates if necessary.
#     """
#     with Session(engine) as session:
#         irises = select(Iris)
#         result = session.exec(irises).first()
#         if not result:
#             populate_database()
#     yield


app = FastAPI()


# def get_session():
#     with Session(engine) as session:
#         yield session


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix='/v1')





