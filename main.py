from fastapi import FastAPI
import src.models as models
from src.crud_router_generator import create_crud_router
import sys, inspect

app = FastAPI()

# Create a CRUD router for each model
all_models = [cls_name for cls_name, cls_obj in inspect.getmembers(sys.modules['src.models']) \
                    if inspect.isclass(cls_obj) and cls_obj.__module__ == 'src.models']

for model_name in all_models:
    model = getattr(models, model_name)
    router = create_crud_router(model)
    app.include_router(router, prefix=f"/{model.__name__.lower()}", tags=[model.__name__])

# Run the FastAPI app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
