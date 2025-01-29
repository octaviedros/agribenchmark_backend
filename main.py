from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import src.models as models
from src.crud_router_generator import create_crud_router
import sys, inspect
import enum

from src.results.export import export_router

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Create a CRUD router for each model
all_models = [cls_name for cls_name, cls_obj in inspect.getmembers(sys.modules['src.models']) \
                    if inspect.isclass(cls_obj) and cls_obj.__module__ == 'src.models' and not issubclass(cls_obj, enum.Enum)]

for model_name in all_models:
    model = getattr(models, model_name)
    router = create_crud_router(model)
    app.include_router(router, prefix=f"/{model.__name__.lower()}", tags=[model.__name__])

app.include_router(export_router)

# Run the FastAPI app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
